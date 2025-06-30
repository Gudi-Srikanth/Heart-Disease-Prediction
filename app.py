from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    try:
        int_features = [float(x) if x.replace('.', '', 1).isdigit() else x for x in request.form.values()]
        final = [np.array(int_features)]
        print(final)
        prediction = model.predict(final)
        output=prediction[0]
        prediction = model.predict(final)
        output = prediction[0]
        print(output)
        if output == 1:
            return render_template("index.html", prediction_text='Based on the information provided, our analysis suggests a potential risk of heart disease. We urge you to consult with a healthcare professional promptly for a thorough assessment and personalized care plan.')
        else:
            return render_template("index.html", prediction_text='Great news! According to our analysis, you appear to have a low risk of heart disease based on the provided information. Keep up the good work with healthy lifestyle choices and regular check-ups to maintain your heart health.')
    except Exception as e:
        print(str(e))
        return render_template("index.html", prediction_text='An error occurred. Please check your input.')

if __name__ == '__main__':
    app.run(debug=True)
