import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

#creating an app
app = Flask(__name__)

#loading the model
model = pickle.load(open("delhi_house_prediction.pickle",'rb'))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    location = request.form['Location']
    Area = float(request.form['Area'])
    Bhk = int(request.form['BHK'])
    Bathrooms = int(request.form['Bathrooms'])
    rate = float(request.form['rate'])
    Parking = request.form['park']
    stat = request.form['stat']
    rtm = request.form['rtm']
    nw = request.form['nw']
    ty = request.form['ty']

    loc = [ "alaknanda", "budh vihar", "chhattarpur", "chittaranjan park", "commonwealth games village", "dilshad garden", "dwarka", "friends colony", "greater kailash", "hauz khas", "kalkaji", "karol bagh", "kirti nagar", "lajpat nagar", "laxmi nagar", "mahavir enclave", "malviya nagar", "mehrauli", "narela", "okhla", "paschim vihar", "patel nagar", "punjabi bagh", "rohini", "safdarjung enclave", "saket", "sarita vihar", "shahdara", "sheikh sarai", "sultanpur", "uttam nagar", "vasant kunj", "vasundhara enclave"]

    try:
        loc_index = loc.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(loc)+10)
    x[0] = Area
    x[1] = Bathrooms
    x[2] = Bhk
    if(Parking=='Yes'):
        x[3]=1
    else:
        x[3]=0
    x[4]=rate
    if(stat=="Fully-Furnished"):
        x[5]=1
        x[6]=0
    elif(stat=="Semi-Furnished"):
        x[5]=0
        x[6]=1
    else:
        x[5]=0
        x[6]=0
    if(rtm=="Yes"):
        x[7]=1
    if(nw=="Yes"):
        x[8]=1
    if(ty=='Apartment'):
        x[9]=0
    else:
        x[9]=1
    if loc_index>=0:
        x[loc_index+10] = 1


    prediction = model.predict([x])

    return render_template("index.html", prediction_text = "The estimated price is Rs.{}".format(round(prediction[0],2)))

if __name__ == '__main__':
    app.run(debug=True)