from flask import Flask, render_template , request
import pandas as pd
import pickle
import numpy as np
app = Flask(__name__)
df = pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open('LassoModel.pkl','rb'))
@app.route('/')


def index():
    locations = sorted(df["Location"].unique())
    return render_template("index.html", locations = locations)

@app.route('/predict', methods=['POST'])
def predict():
    locations = request.form.get('location')
    bhk  = request.form.get('BHK')
    sqft = request.form.get('sqr-feet')
    print(locations,bhk,sqft)
    input = pd.DataFrame([[sqft,locations, bhk]],columns=['Area','Location','No. of Bedrooms'])
    prediction = pipe.predict(input)[0]
    return str(np.round(prediction,2))

if __name__ == "__main__":
    app.run(debug=True, port=5001)

