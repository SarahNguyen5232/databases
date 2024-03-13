"""Forms for playlist app."""

from wtforms import SelectField, StringField, Optional, InputRequired
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField("Playlist Name",
                       validators = [InputRequired(message="Playlist name can't be blank")] )
    desc = StringField("Description",
                       validators = [Optional()])

    # Add the necessary code to use this form (almost finsihed)


class SongForm(FlaskForm):
    """Form for adding songs."""
    name = StringField("Song name",
                       validators = [InputRequired(message="Add song name")])
    artist = StringField("Artist name",
                         validators = [InputRequired(message="Artist name needed")])
    # Add the necessary code to use this form (almost finsihed)


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
