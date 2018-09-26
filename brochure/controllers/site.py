"""Site controller for all pages (for now)."""

from datetime import datetime

from brochure import app
from brochure import login_manager
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
import flask_login
from flask_login import current_user
from flask_login import UserMixin

META_DATA = {
    'theme_color': '#2c292d',
    'ga_tracking_id': 'UA-30649284-1',
    'google_site_verification_token': app.config['GOOGLE_SITE_VERIFICATION_TOKEN'],
}


class User(UserMixin):
    """Not sure why this is here. Makes login work, though? #notapythondeveloper."""

    pass


@login_manager.user_loader
def user_loader(username):
    """Username is defaulted to 'user' for all cases in authorization."""
    if username != 'user':
        return
    user = User()
    user.id = username
    return user


@login_manager.request_loader
def request_loader(request):
    """Check password against global envar. Username does not exist."""
    username = request.form.get('username')
    if username != 'user':
        return
    user = User()
    user.id = username
    user.is_authenticated = request.form['password'] == app.config['CV_PASSWORD']


@login_manager.unauthorized_handler
def unauthorized_callback():
    """Redirect to login page if trying to access an a page and aren't authorized."""
    return redirect(url_for('login_page'))


@app.context_processor
def current_date():
    """Make date accessible on any template. Used primarily for copyright (lol)."""
    return {'date': datetime.utcnow()}


@app.route('/', methods=['GET'])
def splash_page():
    """Generic splash page."""
    meta = META_DATA
    meta['title'] = 'Adam Kliegman'
    meta['description'] = (
        'Adam Kliegman is a Senior Product Manager and '
        'Creative Technologist in New York, NY.'
    )

    adjectives = [
        "Product Designer",
        "Leader",
        "Frontend Ninja",
        "UX/UI Loyalist"
    ]
    return render_template('pages/splash.html', theme='splash', meta=meta, adjectives=adjectives)


@app.route('/cv', methods=['GET'])
@app.route('/resume', methods=['GET'])
@flask_login.login_required
def cv_page():
    """Resume page."""
    meta = META_DATA
    meta['title'] = 'Resume | Adam Kliegman'
    meta['description'] = ''

    return render_template('pages/cv.html', theme='cv', meta=meta)


@app.route('/contact', methods=['GET'])
def contact_page():
    """Contact form page."""
    meta = META_DATA
    meta['title'] = 'Contact | Adam Kliegman'
    meta['description'] = ''

    return render_template('pages/contact.html', theme='contact', meta=meta)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    """Login page. Posts password which checks against envar."""
    meta = META_DATA
    meta['title'] = 'Log In | Adam Kliegman'

    if current_user.is_authenticated:
        return redirect(url_for('cv_page'))

    if request.method == 'POST':
        username = 'user'
        if request.form.get('password') == app.config['CV_PASSWORD']:
            user = User()
            user.id = username
            flask_login.login_user(user)
            return redirect(url_for('cv_page'))
    return render_template('pages/login.html', theme='login', meta=meta)


@app.route('/logout')
def logout():
    """Logout function and redirect. Probably won't be used."""
    flask_login.logout_user()
    return redirect(url_for('splash_page'))
