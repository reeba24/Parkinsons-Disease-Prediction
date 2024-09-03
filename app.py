from flask import Flask, request, render_template
import sys
sys.path.append("D:/miniproj/main_project.py")
import main_project


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    fo = float(request.form['MDVP:Fo(Hz)'])
    fhi = float(request.form['MDVP:Fhi(Hz)'])
    flo = float(request.form['MDVP:Flo(Hz)'])
    
    dfa = float(request.form['DFA'])
    sp1 = float(request.form['spread1'])
    sp2 = float(request.form['spread2'])
    d2 = float(request.form['D2'])
    
    input_data = [
        fo,
        fhi,
        flo,   dfa,
        sp1,
        sp2,
        d2
    ]
    # Call your machine learning code to make a prediction
    prediction = main_project.predict(input_data)

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)