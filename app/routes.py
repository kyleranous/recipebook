from app import app


@app.route('/')
@app.route('/index')
def index():
    return "<h1>Welcome to Recipe Book!</h1>"
