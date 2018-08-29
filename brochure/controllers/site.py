"""Site controller for all pages (for now)."""

from brochure import app
from flask import render_template


meta_data = {
    'subject': 'Adam Kliegman is a Senior Product Manager in New York, NY.',
    'theme_color': '#2c292d',
    'ga_tracking_id': 'UA-30649284-1',
    'google_site_verification_token': 'c7P0SFEg16UGqJfn8rq6CbtxT84bcPiqDswU4xSgFWA',
}


@app.route('/', methods=['GET'])
def splash_page():
    """Generic splash page."""
    meta_data['title'] = 'Adam Kliegman'
    meta_data['description'] = 'It \'s me, Goobie!'

    return render_template('splash/index.html', theme='splash', meta=meta_data)
