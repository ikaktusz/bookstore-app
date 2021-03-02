from flask import (
    Blueprint, url_for, render_template,
    flash, redirect, request, session
)


bp = Blueprint('catalog', __name__)


@bp.route('/catalog')
def catalog():
    return render_template('catalog/catalog.html')