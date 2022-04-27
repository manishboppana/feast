import datetime
from flask import Flask, render_template, flash, request, redirect, url_for,send_file



app=Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    x = datetime.datetime.now()

    y=int(x.strftime("%H"))
    if 0<=y<=6:
        filename = 'ok.jpg'
    elif 7<=y<=12:
        filename = 'cloths.pdf'
    elif 13<=y<=18:
        filename = 'ok.gif'

    else:
        filename = 'food.jpg'
    return send_file(filename, mimetype='image/gif')
        



if __name__=="__main__":
    app.run(host='0.0.0.0',port=5002)




