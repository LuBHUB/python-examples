#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A pipeline for learning from the partisan news data.
"""

# Standard library.
from collections import deque
from datetime import datetime
import math
import re

# External.
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.feature_selection import chi2, SelectPercentile
from sklearn.metrics import confusion_matrix, make_scorer, precision_recall_curve
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import spacy

# Local.
import quotes


#%% Parameters

parameters = {

# Whether to remove quoted text.
# Mainstream articles presumably sometimes quote partisan opinions.
'remove_quotes': True,

# Whether to replace the special 'curly' quote characters (‘’ and “”).
# These may confuse the text parsing algorithms.
'replace_curly_quotes': True,

# Whether to strip surrounding punctuation from words.
'strip_punctuation': True,

# Which parts of speech to retain.
# ADJectives
# ADVerbs
# INTerJections
# NOUNs
# VERBs
'POS': ['ADJ', 'ADV', 'INTJ', 'NOUN', 'VERB'],

# Whether to make all words lowercase.
'lowercase': True,

# Whether to discard words containing non-letter characters.
# (Web addresses for example.)
'letters_only': True,

# Specific words to discard.
# (For example words that happen to occur in a lot of partisan texts,
# but clearly for arbitrary reasons like notices about ad blockers, etc.)
'ignore': [
'ad',
'address',
'article',
'below',
'blocker',
'comment',
'continue',
'daily',
'disable',
'dose',
'email',
'image',
'podcast',
'read',
'story',
'video',
'watch'
],

# Maximum length of ngrams.
'max_ngram': 2,

# Minimum document frequency for a term to be retained.
# Terms that occur in fewer documents than this will be discarded.
'min_occurrences': 10,

# Maximum document frequency for a term to be retained.
# Terms that occur in a greater proportion of documents than this will be discarded.
'max_frequency': 0.9,

# What proportion best features to retain (0.0 to 1.0).
'p_best_features': 0.9,

# How many folds to use in cross-validation.
'k_folds': 5

}


#%% Results file

# File name.
timestamp = datetime.now().strftime('%d_%_b_%Y_%H%M')
results_filename = timestamp + '.log'

# Encoding.
# (Stick to utf-8.)
results_encoding = 'utf-8'

# Open the file for writing.
with open(results_filename, mode='w', encoding=results_encoding) as f:
    f.write('PARTISAN NEWS\n{}\n\n'.format(timestamp))

# Define a logging function for messages.
# Writes the message to the results file and prints it out to the console.
def log_print(*msgs):
    with open(results_filename, mode='a', encoding=results_encoding) as f:
        f.write('\n')
        for msg in msgs:
            f.write(str(msg))
            f.write('\n')
        f.write('\n')
        print('\n', *msgs, sep='\n')

# Start by logging the parameters.
log_print('[parameters]', *['{}: {}'.format(*x) for x in parameters.items()])


#%% Data

# Names of the text files to read from.
# Also used as the category labels for the two types of text.
filenames = ['mainstream', 'partisan']

# Lists to hold the texts and their labels.
items = []
labels = []

# Read the file contents into the lists.
for filename in filenames:
    texts = re.findall('.+(?=\n+)', open(filename+'.txt', encoding='utf-8').read())
    items = items + texts
    labels = labels + [filename] * len(texts)

# How many texts?
log_print('[n texts]', len(items))


#%% Pipeline components: text preprocessing with spacy

# Define a function to replace the curly quote characters.
def replace_curlies(text):
    text_new = text
    for char in '‘’':
        text_new = text_new.replace(char, "'")
    for char in '“”':
        text_new = text_new.replace(char, '"')
    return text_new

# Define a function to strip a word of leading and trailing punctuation.
word_re = re.compile('[a-zA-Z].*[a-zA-Z]')
def strip_punctuation(word):
    match = word_re.search(word)
    if match:
        return match.group(0)
    return ''

# Load the spacy English language model.
# Disable the dependency parser
# and the named entity recognizer.
# We only need the part of speech tagger.
nlp = spacy.load('en', disable=['parser', 'ner'])

# Define a function that preprocesses a text.
# Use the functions defined above and the spacy language model.
# Remove quoted text.
# Replace some troublesome characters.
# Discard punctuation.
# Extract only the requested parts of speech.
# Lemmatize to standard forms.
# Make lowercase.
# Get unigrams.
# Get bigrams where valid tokens are adjacent.
def preprocess(text):
    if parameters['remove_quotes']:
        text = quotes.remove(text)
    if parameters['replace_curly_quotes']:
        text = replace_curlies(text)
    features = []
    ngram = deque([], parameters['max_ngram'])
    for token in nlp(text):
        lemma = token.lemma_
        if parameters['strip_punctuation']:
            lemma = strip_punctuation(lemma)
        valid_pos = token.pos_ in parameters['POS']
        valid_chars = lemma.isalpha() or not parameters['letters_only']
        valid_word = lemma not in parameters['ignore']
        if valid_pos and valid_chars and valid_word:
            if parameters['lowercase']:
                lemma = lemma.lower()
            features.append(lemma)
            ngram.append(lemma)
            if len(ngram) > 1:
                features.append(' '.join(ngram))
        else:
            ngram.clear()
    return features


#%% Pipeline components: scikit-learn

# Create a vectorizer component to turn the texts into counts of features.
vectorizer = CountVectorizer(analyzer=preprocess,
                             min_df=parameters['min_occurrences'],
                             max_df=parameters['max_frequency'])

# Create a transform component.
# tf-idf transform.
transformer = TfidfTransformer()

# Create a feature selection component.
feature_selecter = SelectPercentile(chi2, percentile=math.ceil(parameters['p_best_features']*100))

# Add the final naive Bayes classifier.
# Don't try to learn the prior probability of text types.
classifier = MultinomialNB(fit_prior=False)

# Put the components in a pipeline.
# Make the pipeline verbose so we can check its progress.
# This is useful because the spacy preprocessing is very slow.
model = Pipeline([('vectorize', vectorizer),
                  ('transform', transformer),
                  ('select', feature_selecter),
                  ('classify', classifier)],
                 verbose=True)


#%% Train-test split

# Split texts and labels into training and test sets.
# Stratify so that training and test sets have equal proportions of text types.
# Set the state of the random number generator so the result is replicable.
(train_items,
 test_items,
 train_labels,
 test_labels) = train_test_split(items, labels, stratify=labels, random_state=0)


#%% Fit

# Fit the model to the training data.
model.fit(train_items, train_labels)

# Get the order of categories used.
label_order = list(classifier.classes_)

# Get the names of the features and selected features.
features = np.array(vectorizer.get_feature_names())
features_used = features[feature_selecter.get_support()]

# Get the feature coefficients.
coefs = np.squeeze(classifier.coef_)

# Get the predicted labels and probabilities of partisanship.
predicted_labels = model.predict(train_items)
predicted_probs = model.predict_proba(train_items)[:, label_order.index('partisan')]


#%% Check

# Number of features to list in summaries.
n_show = 20

# How many features were retained?
log_print('[n features]', len(features_used))

# What are the features that occur in the most and fewest texts?
# (Low and high idf.)
idf = transformer.idf_
features_by_idf = features[np.argsort(idf)]
log_print('[most frequent terms]', *features_by_idf[:n_show])
log_print('[least frequent terms]', *features_by_idf[-n_show:])


# What are the most informative features?
features_by_coef = features_used[np.argsort(coefs)]
n_tied = sum(coefs == min(coefs))
if n_tied > n_show:
    extra_msg = ' ({} tied)'.format(n_tied)
    n_show_temp = n_tied
else:
    extra_msg = ''
    n_show_temp = n_show
log_print('[terms most indicative of partisanship{}]'.format(extra_msg),
          *features_by_coef[:n_show_temp])
log_print('[terms least indicative of partisanship]',
          *features_by_coef[-n_show:])

# Confusion matrix.
confusion = confusion_matrix(train_labels, predicted_labels,
                             labels=filenames)
log_print('[confusion matrix]', confusion)

# Precision-recall trade-off.
precision, recall, threshold = precision_recall_curve(train_labels, predicted_probs,
                                                      pos_label=filenames[-1])
threshold = np.append(threshold, 1)
plt.plot(threshold, precision, label='precision')
plt.plot(threshold, recall, label='recall')
plt.vlines(0.5, 0, 1, linestyles='dashed')
plt.xlabel('threshold')
plt.legend()
plt.show()

# Which texts did the model rate as most and least partisan?
items_by_prob = np.array(train_items)[np.argsort(predicted_probs)]
probs_sorted = predicted_probs[np.argsort(predicted_probs)]

for i in [0, -1]:
    log_print('[{} partisan text]'.format(['least', 'most'][i]),
              items_by_prob[i],
              '* P(partisan) = {:.2f}'.format(probs_sorted[i]))

# Define a convenience function for assigning a probability of partisanship.
# Take a raw text as input.
def prob_partisan(text):
    return model.predict_proba([text])[0, label_order.index('partisan')]

# Define exemplary mainstream and partisan texts.
exemplars = {'mainstream': 'Earlier today a political event occurred. \
Government officials were not available for comment, \
but experts have speculated that the event was important \
and may have a significant impact on the economy.',
'partisan': 'These liberal snowflake cucks \
are a fucking disgrace to the American nation. \
They make me sick to the stomach with their degeneracy. \
We should round them all up and shoot them.'}

# Does the model appropriately classify the exemplar texts?
for category, exemplar in exemplars.items():
    log_print('[test on exemplary {} text]'.format(category),
              exemplar,
              '* P(partisan) = {:.2f}'.format(prob_partisan(exemplar)))


#%% Validate

# Organize some performance metrics.
scorers = {'accuracy': make_scorer(accuracy_score),
           'precision': make_scorer(precision_score, pos_label=filenames[-1]),
           'recall': make_scorer(recall_score, pos_label=filenames[-1]),
           'ROC_AUC': make_scorer(roc_auc_score, needs_threshold=True)}

# Check the performance metrics in k-fold cross-validation.
cv_result = cross_validate(model, train_items, train_labels,
                           cv=parameters['k_folds'],
                           scoring=scorers)

log_print('[{}-fold cross-validation]'.format(parameters['k_folds']),
          *['{}\t{:.2f}\t{}'.format(key, np.mean(value), value) for key, value in cv_result.items()])


#%% Final test

#print('\nScores on test data:')
#for name, func in scorers.items():
#    print('{}\t{}'.format(name, func(model, test_items, test_labels)))
