from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/works')
def works():
    return render_template('h_works.html')

@app.route('/hire')
def hire():
    return render_template('h_hire.html')

@app.route('/about')
def about():
    return render_template('h_aboutme.html')

if __name__ == '__main__':
    app.run(debug=True)

