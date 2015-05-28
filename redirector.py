from flask import Flask, redirect
app = Flask(__name__)

def test_expander(short_url):
    if 'g' in short_url:
        return "http://www.google.com"
    else:
        return "http://www.facebook.com"
    
app_expander = test_expander

@app.route('/<short_url>')
def redirect_url(short_url):
    return redirect(location=app_expander(short_url),code=302)

if __name__ == '__main__':
    app.run(debug=True)