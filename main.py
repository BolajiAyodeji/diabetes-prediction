import flask
import pickle

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
        age = flask.request.form.get("age")
        glucose = flask.request.form.get("glucose")
        blood_pressure = flask.request.form.get("blood-pressure")
        skin_thickness = flask.request.form.get("skin-thickness")
        insulin = flask.request.form.get("insulin")
        bmi = flask.request.form.get("bmi")
        prediction = model.predict(
            [[age, glucose, blood_pressure, skin_thickness, insulin, bmi]])

        if prediction == 1:
            prediction = "Positive (Diabetic)"
        else:
            prediction = "Negative (Not diabetic)"

        prediction_text = "the result of your Diabetes prediction test is:"
        result_class = "text-green-700 text-lg font-bold border mt-4 mb-8"

        return(flask.render_template('main.html', patient_name=patient_name, prediction_text=prediction_text, result_class=result_class, result=prediction))


if __name__ == '__main__':
    app.run()
