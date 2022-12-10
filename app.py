from flask import Flask, request, render_template
import numpy as np
import pickle
import joblib

app = Flask(__name__)

model = joblib.load('covid.pkl')
model ='covid.pkl'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def results():

    tinggi = [150]
    sedang = [100]
    
    data=request.form['daerah']
    data1=int(request.form['odp'])
    data2=int(request.form['proses'])
    data3=int(request.form['masih'])
    data4=int(request.form['pdp'])
    
    prediksi=np.array(data1+data2+data3+data4)
    
    if prediksi > tinggi:
        hasil="Zona Merah"
    elif prediksi > sedang:
        hasil="Zona Kuning"
    else :
        hasil="Zona Hijau"
    
    return render_template('index.html', hasil=hasil, prediksi=prediksi, daerah=data,  odp=data1, proses=data2, pdp=data3, masih=data4)

if __name__ == '__main__':
    app.run(debug=True)