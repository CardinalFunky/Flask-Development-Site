from flaskblog import db
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
        validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', 
        validators = [DataRequired(), Email()])
    password = PasswordField('Password', 
        validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
        validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        count = 0
        users = db.get_collection("users").find({ "username": username.data })
        for user in users:
            count = count + 1
        if count > 0:
            raise ValidationError('That username is taken. Please choose a different username.')

    def validate_email(self, email):
        count = 0
        users = db.get_collection("users").find({ "email": email.data })
        for user in users:
            count = count + 1
        if count > 0:
            raise ValidationError('That email is taken. Please choose a different email.')

class LoginForm(FlaskForm):
    username = StringField('Username', 
        validators = [DataRequired(), Length(min = 2, max = 20)])
    password = PasswordField('Password', 
        validators = [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', 
        validators = [DataRequired(), Length(min = 2, max = 20)])
    email = StringField('Email', 
        validators = [DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.user['username']:
            user = db.users.find_one(current_user.user['username'])
            if user:
                raise ValidationError('That username is taken. Please choose a different username.')

    def validate_email(self, email):
         if email.data != current_user.user['email']:
            user = db.users.find_one(current_user.user['email'])
            if user:
                raise ValidationError('That email is taken. Please choose a different email.')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class VideoGameForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = FileField('Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add Game')