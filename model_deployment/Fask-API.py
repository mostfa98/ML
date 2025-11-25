from flask import Flask, request,jsonify
import joblib
import pandas as pd

#Create Flask app

app = Flask(__name__)




#Connect post API cell ---> predict() Function #gttp://Localhost:500/predict
@app.route('/predict',methods = ['POST'])
def predict():

    # GET JSON Request 
    feat_data = request.json

    #Connect JSON to Pandas sd (col names)
    df = pd.DataFrame(feat_data)
    df = df.reindex(columns=col_names)

    #predict
    prediction = list(model.predict(df))

    return jsonify({'prediction':str(prediction)})



#load my model and col 

if __name__ == '__main__':

    model =joblib.load('Final_model.pkl')
    col_names = joblib.load('COL.NAME_FINAL.pkl')

    app.run(debug=True)








