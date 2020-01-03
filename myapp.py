from flask import Flask, redirect, url_for, request
from flask import render_template
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello_form.html')

@app.route('/predict',methods= ['POST'])
def get_result():
    poly=pickle.load(open('Poly.pkl','rb'))
    model=pickle.load(open('model.pkl','rb'))
    query=[[float(request.form['text2'])]]
    X_query=poly.transform(query)
    sal=model.predict(X_query)
    return 'Dear'+request.form['text1']+'Your predicted salary after'+request.form['text2']+'Experience is :'+str(sal)
   
''' 
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
'''
if __name__ =="__main__":
    app.run(debug=True, port=8080)
