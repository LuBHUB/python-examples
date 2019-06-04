#!/bin/bash

# This is a convenient single script that displays all the example SQL commands and their results.
# The following lines pass the contents of the example .sql files on to sqlite3.

# The reading examples.
cat reading.sql | sqlite3 music.db

# The writing examples.
rm -f example.db
cat writing.sql | sqlite3 example.db

