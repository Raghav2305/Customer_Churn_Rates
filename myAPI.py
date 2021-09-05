from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import sklearn

app = Flask(__name__)
model = joblib.load('my_final_model.pkl')
columns = joblib.load('my_cols.pkl')



@app.route('/display', methods = ['POST'])
def predict():
    if request.method == 'POST':
        name = request.form['nm']
        age = request.form['age']
        gender = request.form['gender']
        tenure = request.form['tenure']
        monthly_charges = request.form['m_charges']

        preds = model.predict([[tenure, monthly_charges]])

    return render_template('display.html', preds = preds)

@app.route('/')
def home():
    return render_template('predict.html')



if __name__ == '__main__':
    app.run(debug=True)







