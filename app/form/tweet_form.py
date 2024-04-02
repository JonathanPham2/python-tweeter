from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm


class Tweet(FlaskForm):
    author=StringField("Author:")
    tweet= StringField("Tweet:")
    submit = SubmitField("Create Tweet")
    update = SubmitField("Update Tweet")
