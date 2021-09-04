from flask import Flask, request, jsonify
import joblib
import pandas as pd
import sklearn

app  = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data)
    df = df.reindex(columns=col_names)

    preds = list(model.predict(df))
    return jsonify({'prediction':str(preds)})

if __name__ == '__main__':
    model = joblib.load('my_final_model.pkl')
    col_names = joblib.load('my_cols.pkl')

    app.run(debug=True)







