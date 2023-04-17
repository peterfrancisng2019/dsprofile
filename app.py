
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/myprofile')
def myprofile():
    return render_template('myprofile.html')

@app.route('/project1')
def project1():
    return render_template('project1.html')

@app.route('/project2')
def project2():
    return render_template('project2.html')

@app.route('/project3')
def project3():
    return render_template('project3.html')

@app.route('/moreprojects')
def moreprojects():
    return render_template('moreprojects.html')

@app.route('/predict',methods=['POST'])
def predict():
    """Grabs the input values and uses them to make prediction"""
    distance = int(request.form["distance_to_metro"])
    conv = int(request.form["nos_of_conv"])
    prediction = model.predict([[distance, conv]])  # this returns a list e.g. [127.20488798], so pick first element [0]
    output = round(prediction[0], 2) 

    return render_template('index.html', prediction_text=f'A house surrounded by {conv} stores and located {distance} meters from the city metro station has a value of ${output}')

if __name__ == "__main__":
    app.run()
