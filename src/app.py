import numpy as np
from flask import Flask, request, render_template
import pickle
from parser_request import Parser
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

#Creting an app obj using Flask class
app=Flask(__name__)

#loading the model using pickle
model_path='Language-Detection\\models\\Gaussian_model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)

#loading the tfidf embedding
emb_path='Language-Detection\\models\\embeddings-tfIdf.pkl'
with open(emb_path, 'rb') as f:
    emb = pickle.load(f)


#definition of the route url
@app.route('/')
def home():
    return render_template('index.html')

#definition of the predinct function
@app.route('/predict',methods=['GET','POST'])
def predict():

    if request.method=='POST':
        text=request.form.get('frase')
        #parsing the input values using class Parser()
        parser=Parser()
        
        text=request.form.get('frase')
        print('RICHIESTA',text)
        text=parser.parseText(text)

        #computing the embedding for the input text
        input_text=[text]
        embedding=emb.transform(input_text).toarray()

        #prediction 
        prediction=model.predict(embedding)[0]

        prediction_text='Prediction: '
        #creating a string giving the prediction made by the model
        if prediction==0:
            prediction_text+='Not italian'
        else:
            prediction_text+='Italian'
        return render_template('index.html',prediction_text=prediction_text)
    
        


if __name__=="__main__":
    app.run(debug=True)

