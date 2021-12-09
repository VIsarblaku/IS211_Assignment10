CREATE DATABASE music;

CREATE TABLE music.dbo.artist(
id int IDENTITY(1,1) PRIMARY KEY,
name text NOT NULL,
)

CREATE TABLE music.dbo.album(
album_id int IDENTITY(1,1) PRIMARY KEY,
album_name text NOT NULL,
artist_name text NOT NULL
)

CREATE TABLE music.dbo.song(
song_id int IDENTITY(1,1) PRIMARY KEY,
song_name text NOT NULL,
album_name text NOT NULL,
track_number int NOT NULL,
song_duration int NOT NULL
)
