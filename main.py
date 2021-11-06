import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model.
with open(f'model/diabetes.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))

    if flask.request.method == 'POST':
        patient_name = flask.request.form.get("patient-name") + ","
        glucose = flask.request.form.get("glucose")
        blood_pressure = flask.request.form.get("blood-pressure")
        skin_thickness = flask.request.form.get("skin-thickness")
        insulin = flask.request.form.get("insulin")
        bmi = flask.request.form.get("bmi")
        diabetes_pedigree_function = flask.request.form.get(
            "diabetes-pedigree-function")
        age = flask.request.form.get("age")
        prediction = model.predict(
            [[glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])

        if prediction == 1:
            prediction = "Positive (Diabetic)"
        else:
            prediction = "Negative (Not diabetic)"

        prediction_text = "the result of your Diabetes prediction test is:"

        return(flask.render_template('main.html', patient_name=patient_name, prediction_text=prediction_text, result=prediction))


if __name__ == '__main__':
    app.run()
