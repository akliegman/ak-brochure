"""Site controller for all pages (for now)."""

from brochure import app
from datetime import datetime
from flask import render_template


meta_data = {
    'theme_color': '#2c292d',
    'ga_tracking_id': 'UA-30649284-1',
    'google_site_verification_token': 'c7P0SFEg16UGqJfn8rq6CbtxT84bcPiqDswU4xSgFWA',
}


@app.context_processor
def current_date():
    """Make data accessible on any template"""
    return {'date': datetime.utcnow()}


@app.route('/', methods=['GET'])
def splash_page():
    """Generic splash page."""
    meta_data['title'] = 'Adam Kliegman'
    meta_data['description'] = (
        'Adam Kliegman is a Senior Product Manager and Creative Technologist in New York, NY.'
    )
    return render_template('pages/splash.html', theme='splash', meta=meta_data)


@app.route('/cv', methods=['GET'])
@app.route('/resume', methods=['GET'])
def cv_page():
    """Resume page."""
    meta_data['title'] = 'Javascript: Learn How to do awesome things and break everything'
    meta_data['description'] = ''

    return render_template('pages/cv.html', theme='cv', meta=meta_data)


@app.route('/contac', methods=['GET'])
def contact_page():
    """Resume page."""
    meta_data['title'] = 'Javascript: Learn How to do awesome things and break everything'
    meta_data['description'] = ''

    return render_template('pages/contact.html', theme='contact', meta=meta_data)
