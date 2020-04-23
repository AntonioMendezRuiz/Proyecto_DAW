from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html') 
    
app.run(debug=True)

#html = urlopen("https://www.google.es/")
#res = BeautifulSoup(html.read(),"html5lib")
#print(res.title)
