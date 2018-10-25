from flask import Flask
from flask import request
import requests
from bs4 import BeautifulSoup
from flask import jsonify
from flask import render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField,SubmitField
from wtforms.validators import Required
from CrawlSearchEngine import crawler
import json



# def metaSearchEngine(keyword):

#     res=requests.get("https://https://www.google.com.tw/search?q=dcard")
#     parser = BeautifulSoup(res.text,"html.parser") 

#     a = parser.find('div',attrs={'class','rc'})

#     return a


app = Flask(__name__)


@app.route('/index',methods=['POST','GET'])

def index():

    if request.method=='POST':
        postdata = request.data
        return postdata


    elif request.method=='GET':
        return render_template("index.html")




@app.route('/')
def hello():
    return render_template('index.html')



@app.route('/search',methods=['POST'])

def metasearch():

    inputvalue = request.form['inputvalue']

    result = crawler(inputvalue)

    return render_template("resultpage.html", searchvalue = inputvalue , searchresult = result)
   



@app.route('/index2')
def index2():
    user = {'nickname': 'Miguel','suckname': 'jeffese'} 
    return render_template("templatetest.html",
        title = 'Home',
        user = user)


# -----------------------------------------------------------------------------------------------

app.run(host='127.0.0.1' , port=80, debug=True)


