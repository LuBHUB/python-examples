-- Some example SQL commands from SQL.ipynb gathered in one place for reference.
-- You can see the examples in action in the terminal by running the bash script SQL_examples.sh

-- This file contains example commands for writing to a new database.

-- Comments in SQL are preceded by two dashes.


-- When writing to a database, it is a good idea to group changes as a transaction.
-- Then when the changes are all made and checked, the transaction can be committed.
-- Begin a transaction.
BEGIN TRANSACTION;

-- Create a table with column names, data types, and constraints.
CREATE TABLE artists
(id INTEGER PRIMARY KEY,
artist TEXT UNIQUE,
country TEXT);

-- Create a second table with a foreign key referencing the first table.
CREATE TABLE albums
(id INTEGER PRIMARY KEY,
artist_id INTEGER,
album TEXT,
year INTEGER,
FOREIGN KEY(artist_id) REFERENCES artists(id),
UNIQUE(artist_id, album));

-- Insert values into a table.
INSERT INTO artists (artist, country) VALUES('Geier Sturzflug', 'DE');

-- Check the result.
SELECT * FROM artists;

-- See that repeating a value in a column declared as UNIQUE results in an error.
INSERT INTO artists (artist, country) VALUES('Geier Sturzflug', 'DE');

-- Avoid the error by inserting or ignoring if the insert violates constraints.
INSERT OR IGNORE INTO artists (artist, country) VALUES('Geier Sturzflug', 'DE');

-- Commit the changes made during the current transaction so that they are definitely written to the database.
COMMIT;

