-- Some example SQL commands from SQL.ipynb gathered in one place for reference.
-- You can see the examples in action in the terminal by running the bash script examples.sh

-- This file contains example commands for reading from an existing database.

-- Comments in SQL are preceded by two dashes.


-- Select all columns from a table.
SELECT * FROM artists;

-- Specify which columns to select.
SELECT artist, country FROM artists;

-- Join information from two tables using a linking key column.
SELECT artist, album FROM albums JOIN artists ON albums.artist_id = artists.id;

-- Join information from more than two tables.
SELECT artist, album, song FROM songs
JOIN albums ON songs.album_id = albums.id
JOIN artists ON songs.artist_id = artists.id;

-- Select a subset of rows based on a condition.
SELECT song, number FROM songs WHERE number = 1;

-- Combine selecting, joining, and subsetting.
SELECT artist, album, song, number FROM songs
JOIN albums ON songs.album_id = albums.id
JOIN artists ON songs.artist_id = artists.id
WHERE number = 1;

