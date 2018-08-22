"""Site controller for all pages (for now)."""

from brochure import app
from flask import render_template


meta_data = {
    'subject': 'Product Management',
    'theme_color': '#000000',
    'ga_tracking_id': 'UA-30649284-1',
}


@app.route('/', methods=['GET'])
def splash_page():
    """Generic splash page."""
    meta_data['title'] = 'Hello World'
    meta_data['description'] = 'It \'s me, Goobie!'

    return render_template('splash/index.html', theme='splash', meta=meta_data)
