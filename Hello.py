from flask import Flask, redirect, url_for, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['GET', 'POST'])
@cross_origin()
def login():
    if request.method == 'POST':
        data = request.data
        print "Your data is %s" % data
        return "Got your data: %s!" % data
    else:
        return "Just visiting!"
 
    

if __name__ == '__main__':
   app.run(debug = True)