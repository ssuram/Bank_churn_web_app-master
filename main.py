from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def home():
    if request.method == 'POST':
        CreditScore = int(request.form['CreditScore'])
        Geography=request.form['Geography']
        if(Geography=='France'):
            Geography=0
        elif(Geography=='Spain'):
            Geography=2
        else:
            Geography=1

        gender=request.form['gender']
        if (gender == 'Female'):
            gender = 0
        else:
            gender = 1

        Balance=int(request.form['Balance'])
        Age=int(request.form['Age'])
        Tenure=int(request.form['Tenure'])

        NumofProducts=int(request.form['NumofProducts'])

        HasCrCard=request.form['HasCrCard']

        isActiveMember=request.form['isActiveMember']
        EstimatedSalary=int(request.form['EstimatedSalary'])

        prediction=np.array([[CreditScore,Geography,gender,Balance,Age,Tenure,NumofProducts,HasCrCard,isActiveMember,EstimatedSalary]])

        pred = model.predict(prediction)

        return render_template('after.html', data=pred)


    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)