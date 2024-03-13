"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
__tablename__ = "playlists"

id = db.Column(db.Integer,
                    primary_key=True)
name = db.Column(db.Text,
                      nullable=False,
                      unique=True)
desc = db.Column(db.Text)


class Song(db.Model):
    """Song."""
__tablename__ = "songs"

id = db.Column(db.Integer,
                    primary_key=True)
title = db.Column(db.Text,
                       nullable=False)
artist = db.Column(db.Text,
                        unique=True,
                        nullable=False)

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
__tablename__ = "playlist_songs"

id = db.Column(db.Integer,
                   primary_key=True)
play_id = db.Column(db.Integer,
                    db.ForeignKey('playlists.id'))
song_id = db.Column(db.Integer,
                    db.ForeignKey('songs.id'))

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
