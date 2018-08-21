"""Site controller for all pages (for now)."""

from brochure import app
from flask import render_template


meta_data = {
    'subject': 'Product Management',
    'theme-color': '#000000',
    'google-analytics': 'xxxxxxxxxx',
}


@app.route('/', methods=['GET'])
def splash_page():
    """Generic splash page."""
    meta_data['title'] = 'Sup'
    meta_data['description'] = 'Hey'

    return render_template('splash/index.html', theme='splash', meta=meta_data)
