from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
from model_Gaussian import Model_NLP
import re
app = Flask(__name__)
api = Api(app)

# create new model object
model = Model_NLP()
# load trained classifier
clf_path = '..\\models\\Gaussian_model.pkl'
with open(clf_path, 'rb') as f:
    model.clf = pickle.load(f)
# load trained vectorizer
vec_path = '..\\models\\TFIDFVectorizer.pkl'
with open(vec_path, 'rb') as f:
    model.vectorizer = pickle.load(f)


# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')


def parse_query(text):
   

    text=re.sub(r'[!@#$()—,\n"%^*?:;0-9)]','',text)
    text=re.sub(r'[[]]','',text)
    text=text.lower()
    text=text.strip()
    return text

class Predict_Lang(Resource):
    def post(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']
        user_query= parse_query(user_query)
        # vectorize the user's query and make a prediction
        uq_vectorized = model.vectorizer_transform(
            np.array([user_query]))
        prediction = model.predict(uq_vectorized)
        prob_prediction=model.predict_proba()
        
        # Output 'Negative' or 'Positive' along with the score
        if prediction == 0:
            pred_text = 'Not italian'
        else:
            pred_text = 'Italian'

        confidence = round(prob_prediction[0], 3)
            
        # round the predict proba value and set to new variable
        # create JSON object
        output = {'Language': pred_text, 'Confidence':confidence}
        
        return output

# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(Predict_Lang, '/')


if __name__ == '__main__':
    app.run(debug=True)