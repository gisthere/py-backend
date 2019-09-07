from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    # return app.make_response('Hello Universe!')
    user = {"username": "System"}
    mani = [
        {'datetime': '2019-09-06 22:37', 'status': ['up', 'dowm']},
        {'datetime': '2019-09-06 22:37', 'status': ['up', 'dowm']},
        {'datetime': '2019-09-06 22:37', 'status': ['up', 'dowm']},
        {'datetime': '2019-09-06 22:39', 'status': ['up', 'dowm']},
        {'datetime': '2019-09-06 22:39', 'status': ['up', 'dowm']},
        {'datetime': '2019-09-06 22:39', 'status': ['up', 'dowm']}        
    ]

    controller = [
        {'datetime': '2019-09-06 22:37', 'status': ['up', 'dowm'], 'decision':'10:05'},
        {'datetime': '2019-09-06 22:37', 'status': ['up', 'dowm'], 'decision':'11:25'},
        {'datetime': '2019-09-06 22:39', 'status': ['up', 'dowm'], 'decision':'3:25'},
        {'datetime': '2019-09-06 22:39', 'status': ['up', 'dowm'], 'decision':'7:25'},
        {'datetime': '2019-09-06 22:39', 'status': ['up', 'dowm'], 'decision':'12:25'}        
    ]

    return render_template("index.html", title="Python Backend - Test", user=user, mani=mani, controller=controller)

if __name__ == "__main__":
    app.run(debug=True)
