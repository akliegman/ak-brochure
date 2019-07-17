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
    'theme_color': '#365060',
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
def get_configs():
    return {
            'debug': app.config['DEBUG'],
            'date': datetime.utcnow(),
            'sr_only': app.config['SR_ONLY']
            }


@app.route('/', methods=['GET'])
def splash_page():
    """Homepage."""
    meta = META_DATA
    meta['title'] = 'Kliegman Design Co.'
    meta['description'] = (
        'The Kliegman Design Co. provides product consultancy, '
        'UX/UI expertise, and frontend development, specializing '
        'in brass tacks product strategiy with and design technique '
        'that focuses on maximizing OKRs and other performance objectives.'
    )

    return render_template('pages/splash.html', theme='splash', meta=meta)


@app.route('/privacy-policy', methods=['GET'])
def privacy_page():
    """Privacy Policy page."""
    meta = META_DATA
    meta['title'] = 'Privacy Policy | Kliegman Design Co.'

    return render_template('pages/privacy.html', theme='default', meta=meta)


@app.route('/terms-of-use', methods=['GET'])
def terms_page():
    """Privacy Policy page."""
    meta = META_DATA
    meta['title'] = 'Terms Of Use | Kliegman Design Co.'

    return render_template('pages/terms.html', theme='default', meta=meta)


@app.route('/ajax/contact', methods=['POST'])
def contact_post():
    """Contact form ajax submit."""
    data = request.form.to_dict()

    msg = Message(
        'New Contact Form Submission from kliegmandesign.com',
        sender=app.config['MAIL_USERNAME'],
        recipients=[app.config['AK_EMAIL']]
    )

    msg.html = render_template('email/email.html', data=data)
    mail.send(msg)

    return json.dumps({'status': 'success'})
