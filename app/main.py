from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)

# pip install virtualenv
# python -m venv virtual
# virtual\Scripts\pip install flask
# virtual\Scripts\python app\main.py

# RUN ON CMD only

# heroku login
# virtual\Scripts\pip install gunicorn
# virtual\Scripts\pip freeze > requirements.txt
# virtual\Scripts\python --version

# git config --global user.email “prateekclaregd@gmail.com”
# git config --global user.name "prateekclare"
# git init
# git add .
# git commit –m “First commit”
# heroku create pythonflaskclassprateek
# git push heroku master
# heroku ps:scale web=1