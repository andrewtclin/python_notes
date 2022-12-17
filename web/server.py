# Flask

from flask import Flask, render_template

# Use Flask to instantiate the app

app = Flask(__name__) # __name__ is "__main__" in this case as this is the main file that we are running

@app.route('/') # decorator - In this case, anytime we hit "/", define this function and run
def hello_world():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return 'This is blog.'


@app.route('/blog/2022/dogs')
def blog2():
    return 'blog2'