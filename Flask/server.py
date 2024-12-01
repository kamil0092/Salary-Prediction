from PIL.ImageFile import ERRORS
from flask import Flask, render_template, request
import  pickle
app = Flask(__name__)

with open('salary_model.pkl', 'rb') as f1:
    model = pickle.load(f1)

#decorator
@app.route("/", methods=['GET'])
def root():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            experience = float(request.form.get("experience"))
            print(f"experience = {experience}, type = {type(experience)}")

            salary = model.predict([[experience]])
            round_salary = round(salary[0], 2)

            return render_template('result.html', experience=experience, salary=round_salary)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app.run(debug=True)

