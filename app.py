from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import pyodbc, urllib
    
app=Flask(__name__)
app.secret_key = "thisissecretkey"

params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=DESKTOP-HUMUQNN\SQLEXPRESS;DATABASE=portfolioDb;Trusted_Connection=yes;')
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params

db = SQLAlchemy(app)


class review_table(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    bookTitle = db.Column(db.String(80), unique=False, nullable=False)
    bookAuthor = db.Column(db.String(50), nullable=False)
    bookReview = db.Column(db.String(800), nullable=False)
    slug = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(50), nullable=False)


class tech_projects(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    details = db.Column(db.String(200), nullable=False)
    img = db.Column(db.String(1000), nullable=False)
    link = db.Column(db.String(200), nullable=False)
    

# Home Page    
@app.route('/home', methods=['GET','POST'])
def home():
    fetch=review_table.query.all()
    proj=tech_projects.query.all()
    return render_template('index.html', fetch=fetch, proj=proj)

@app.route('/review/<slug>', methods=['GET'])
def review_route(slug):
    review=review_table.query.filter_by(slug=slug).first()
    return render_template('review.html', review=review)





