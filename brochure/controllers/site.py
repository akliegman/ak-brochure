from brochure import app

@app.route('/')
def index():
  return 'Hello World I guess...'

@app.route('/otherpage')
def otherpage():
  return 'Some other page'
