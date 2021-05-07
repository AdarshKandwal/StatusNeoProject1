import sys
import os
import glob
import re
from fbprophet import Prophet
import pandas as pd 
import flask
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

def facebook_propher(days):
  df=pd.read_csv('BTC-USD (1).csv')
  df.dropna(axis=0,inplace=True)
  df['Date'] = pd.to_datetime(df['Date'])
  df=df[['Date','Close']]
  df.columns = ['ds','y']
  # Initialize the Model
  model=Prophet() 
  model.fit(df)
  ### Create future dates of 365 days
  future_dates=model.make_future_dataframe(periods=days)
  ### plot the predicted projection
  prediction=model.predict(future_dates)

  model.plot(prediction).savefig('static/img/prophetplot.jpg')
  #### Visualize Each Components[Trends,yearly]
  model.plot_components(prediction).savefig('static/img/prophetplot2.jpg')


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/bitcoin', methods=['GET'])
def bitcoin():
    # Main page
    return render_template('index.html')

@app.route('/images', methods=['GET'])
def sentiment():
    # Main page
    return render_template('prediction.html')



@app.route('/bitcoin_pred', methods = ['POST', "GET"])
def bitcoinpred():
    if request.method=='POST':
        text = request.form['text']
        day=int(text)
        facebook_propher(day)
           
        
    return render_template('images.html') 
#   return render_template('home.html', text=text, sentiment=sentiment, probability=probability, image=img_filename) 


if __name__ == '__main__':
    app.run(debug=True)


