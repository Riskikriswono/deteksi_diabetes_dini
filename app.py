from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Muat model deteksi diabetes dini
model = joblib.load('D:/Documents/Py/myapp/model/rf_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Ambil data dari form
    data = request.form
    # Konversi data ke format yang diperlukan oleh model
    # Misalnya, jika model memerlukan array numpy
    input_data = np.array([
        int(data['age']),
        int(data['gender']),
        int(data['polyuria']),
        int(data['polydipsia']),
        int(data['sudden_weight_loss']),
        int(data['weakness']),
        int(data['polyphagia']),
        int(data['genital_thrush']),
        int(data['visual_blurring']),
        int(data['itching']),
        int(data['iritabilitas']),
        int(data['delayed_healing']),
        int(data['partial_paresis']),
        int(data['muscle_stiffness']),
        int(data['alopecia']),
        int(data['obesity'])
    ]).reshape(1, -1)
     # Cetak data yang telah dikonversi
    # Lakukan prediksi
    prediction = model.predict(input_data)
    # Kembalikan hasil prediksi
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
