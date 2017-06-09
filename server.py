'''Main server page for Coding Dojo Flask Fundamentals "What's My Name" assignment
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''
#pylint: disable=C0103

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')

def landingpage():
    return render_template("index.html")

@app.route('/process', methods=['GET', 'POST'])
def processpage():
    print "Got Post Info"
    print request.form
    name = request.form['name']
    return render_template("process.html", name=name)
app.run(debug=True)

