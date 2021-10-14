from flask import Flask, render_template, url_for, request, redirect
import runpy
from flask.helpers import flash

app = Flask(__name__)

 
@app.route('/')
def home():
    return render_template("stock.html")

@app.route('/done')
def done():
    return render_template("done.html")

@app.route('/crawling') 
def start_crawling():
    try:
        file_globals = runpy.run_path('stock_webcrawling.py')
    except SystemExit:
        pass

@app.route('/insight001')
def insight001():
    return render_template("insight001.html")

@app.route('/insight002')
def insight002():
    return render_template("insight002.html")

@app.route('/insight003')
def insight003():
    return render_template("insight003.html")

@app.route('/insight004')
def insight004():
    return render_template("insight004.html")

@app.route('/insight005')
def insight005():
    return render_template("insight005.html")
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)