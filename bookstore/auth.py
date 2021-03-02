from flask import (
    Blueprint, url_for, render_template,
    flash, redirect, request, session
)
from .forms import ContactForm


bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():

    
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    return 'gg'

@bp.route('/register')
def register():
    return render_template('auth/register.html')