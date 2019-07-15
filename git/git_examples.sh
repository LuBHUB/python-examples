#!/bin/bash -v

# The following example commands illustrate some basic uses of bash and git.
# They use an example GitHub repository with not much in it.
# You can even run this whole file to see the commands in the terminal along with their effects.
# Note that these are all commands for the bash terminal, not Python.


# See your current git configuration.
# The - indicates an 'option' for the command.
# In this case, the -l option lists all config info.
git config -l

# Clone a repository from GitHub into a directory.
# The first argument to the 'clone' command is the url to the .git file of the repository.
# The optional second argument is the directory to clone into (this defaults to the name of the repository).
git clone https://github.com/luketudge/example.git

# Change directory.
cd example

# List current directory contents.
ls

# Check git status.
# This tells you what branch you are on, whether files have changed, etc.
# It is a good idea to keep checking git status as you go along.
git status

# Switch to another branch.
git checkout dev

# View the branches of the repository.
# The branch you are on is marked with an asterisk *.
git branch

# Pull in any changes from the remote GitHub repository to your local repository.
# It is a good idea to do this before starting work on any changes.
git pull


# It is at this point in the workflow that you would change some files in the project.
# You would do this in the normal way in your preferred editor.
# git will be aware of the changes the next time that you use a git command.
# Here we will just use a bash command to change one file.
# We also check the change.
# This is just for demonstration purposes.
echo "And an example added line." >> 1.txt
cat 1.txt


# It is a good idea to check git status after each action.
git status

# Add changed files to the set of 'staged' changes that will go into the next commit.
git add 1.txt
git status

# If you change your mind about files you have added, you can 'unstage' changes with reset.
git reset
git status

# If you have changed your mind about the changes themselves you can even undo them.
# The --hard option to git reset not only unstages changes but undoes them on the local computer.
git reset --hard
git status


# (We can see that the change is now undone in the file.)
cat 1.txt


# Now let's create some new files, in a subdirectory.
# (Again, this is just for the purposes of the demo; you would do this in your normal editor.)
mkdir subdirectory
for file in 2 3
do
> "subdirectory/$file.txt"
done


# You can use the * wildcard in bash to name multiple files matching a pattern.
# This is useful for adding several files of the same kind or in the same folder.
git add subdirectory/*.txt
git status

# Gather the current added changes as a commit.
# The -m option adds a descriptive message to the commit.
git commit -m "an example commit"
git status

# At this stage, the changes have merely been 'packaged' as a single commit.
# They have not yet been sent back to the remote repository.
# If you want to discard the current commit, you can reset the 'HEAD'.
# The HEAD is a reference to the current branch in its most up-to-date state with all your commits.
# The ~1 parameter discards the 1 most recent commit.
git reset HEAD~1
git status

# Now let's add back and commit the new files for one last demonstration.
git add subdirectory/*.txt
git commit -m "an example commit"
git status

# Send (or 'push') the changes to the remote repository on GitHub.
# This command is commented out here in case you run this script in one go.
# (The push would fail because it requires a username and password for the GitHub site.)
#git push

# This is the final step in the basic local workflow.


# (To remove the cloned repository after running these example commands just delete the 'example' directory it was cloned into.)

