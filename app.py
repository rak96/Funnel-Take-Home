from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer


app = Flask(__name__)


@app.route('/api', methods=['POST'])
def pred():
    
    data = request.get_json()
    vectorizer = CountVectorizer(min_df=1,lowercase=True)                      
    test=vectorizer.fit_transform([data])
    result = model.fit_transform(test)
    return jsonify(result.tolist())

if __name__ == '__main__':
    
    modelfile = 'lda_topic.pkl'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0', port="8989")