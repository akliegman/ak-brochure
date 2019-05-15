"""Site controller for all pages (for now)."""

from datetime import datetime
import json

from brochure import app
from brochure import login_manager
from brochure import mail
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
import flask_login
from flask_login import current_user
from flask_login import UserMixin
from flask_mail import Message

META_DATA = {
    'theme_color': '#2c292d',
    'ga_tracking_id': 'UA-30649284-1',
    'google_site_verification_token': app.config['GOOGLE_SITE_VERIFICATION_TOKEN'],
    'recaptcha_site_key': app.config['RECAPTCHA_SITE_KEY'],
    'colors': {
        'blue': '#365060',
        'red': '#D03C3C',
        'gray': '#DCE0E2',
        'white': '#FFFFFF',
        'black': '#111111',
    }
}


@app.context_processor
def current_date():
    """Make date accessible on any template. Used primarily for copyright (lol)."""
    return {'date': datetime.utcnow()}


@app.context_processor
def get_debug():
    return {'debug': False}


@app.route('/', methods=['GET'])
def splash_page():
    """Generic splash page."""
    meta = META_DATA
    meta['title'] = 'Kliegman Design Co.'
    meta['description'] = (
        'Adam Kliegman is a Senior Product Manager and '
        'Creative Technologist in New York, NY.'
    )

    return render_template('pages/splash.html', theme='splash', meta=meta)


@app.route('/ajax/contact', methods=['POST'])
def contact_post():
    """Contact form ajax submit."""
    data = request.form.to_dict()

    msg = Message(
        'New Contact from AdamKliegman.com',
        sender=app.config['MAIL_USERNAME'],
        recipients=[app.config['AK_EMAIL']]
    )

    msg.html = render_template('email/email.html', data=data)
    mail.send(msg)

    return json.dumps({'status': 'success'})
