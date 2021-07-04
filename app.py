import nltk

# download these model from nltk
nltk.download('wordnet')
nltk.download('punkt')

from logging import debug
from flask import Flask,render_template,request
from textblob import Word

# create a flask app
app = Flask(__name__)

# define an api
@app.route('/')
def home():
    return render_template('base.html') 

@app.route("/explain", methods = ["POST"])
def explain():
    # get the info:
    word = request.form.get('Word')

    # take the word to explain and give its definition
    meaning = Word(word).definitions

    # check :
    if not meaning:
        return render_template('base.html',Explaination = f"Please enter a valid word")
    else:
        return render_template('base.html',Explaination = f"{word} means : {meaning}")


if __name__ == '__main__':
    
    app.run(host="0.0.0.0",port=5000,debug=True)