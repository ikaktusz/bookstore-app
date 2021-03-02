from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (
    DataRequired, Length, Email,
    EqualTo, Optional
)


class RegistrationForm(FlaskForm):
    '''User Refistration page.'''
    name = StringField(
        'Name',
        validators=[DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message=('Not a valid email adress.')),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Select strong password.')
        ]
    )
    confirm = PasswordField(
        'Confirm your password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Password must match.')
        ]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    '''User Login form.'''
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Enter a valid email.')
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField('Login')