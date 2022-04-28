from flask import Flask
import os

app = Flask(__name__)
h = os.getenv(env)
@app.route('/')
def sample():
    return h
    #return '<h1>' + app.config['assign'] + '</h1>'
if __name__ == '__main__' :
    app.run('debug' == True)
    
