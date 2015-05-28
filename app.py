from flask import Flask
from flask import redirect, render_template
from expander import sqlitedb_expander

app = Flask(__name__)

app_expander = sqlitedb_expander

@app.route('/<short_url>')
def redirect_url(short_url):
    long_url = app_expander(short_url)
    if long_url is not None:
        return redirect(location=long_url,code=302)
    else:
        return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)