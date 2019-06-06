#!/bin/bash

# This is a convenient single script that displays all the example SQL commands and their results.
# The following lines pass the contents of the example .sql files on to sqlite3 with the | 'pipe'.
# The options to sqlite3 specify which database files the commands should be executed with
# and tell sqlite3 to 'echo' the commands (i.e. print them out as they are executed).

# The reading examples.
cat reading.sql | sqlite3 music.db -echo

# The writing examples.
rm -f example.db
cat writing.sql | sqlite3 example.db -echo

