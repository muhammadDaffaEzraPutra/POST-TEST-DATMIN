# Reneweble energy Prediction API
(https://drive.google.com/drive/folders/1KKtD6_tlwz-SdP5VI7hzkBPWOy35jhZI?usp=sharing) **folder lengkap fast api**

Sebuah mini-proyek berbasis **FastAPI** yang dapat memprediksi kemungkinan **stok energy beberapa tahun ke depan**, berdasarkan data energy.


## 📁 Struktur File

```
├── main.py                               # Endpoint API utama
├── linear_regression_model.pkl           # File model Machine Learning yang telah dilatih                           
├── requirements.txt                      # Daftar dependency yang dibutuhkan
```

## 🚀 Fitur API

- Prediksi stok energy
- Menerima input melalui metode POST
- Hasil prediksi: "prediction_result"
- Ringan, cepat, dan siap diintegrasikan ke aplikasi lain

## ⚙️ Cara Menjalankan


### 1. Buat Virtual Environment

```bash
python -m venv .env
source .env/bin/activate  # Command Prompt: .env\Scripts\activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Jalankan API

```bash
fastapi dev
```

### 5. Akses Swagger UI

Buka browser ke:  
👉 (http://127.0.0.1:8000/docs)

## 🧪 Contoh JSON Input

```json
{
  "Year": 2025,
  "Hydroelectric_power": 4.5,
  "Wind_wave_tidal": 7.2,
  "Solar_photovoltaic": 3.9,
  "Bioenergy": 5.1
}
```

## ✅ Contoh Output

```json
{
  "input": {
    "Year": 2025,
    "Hydroelectric power": 4.5,
    "Wind, wave, tidal": 7.2,
    "Solar photovoltaic": 3.9,
    "Bioenergy": 5.1
  },
  "prediction_result": 32.42895008710519,
  "unit": "GWh",
  "model_version": "1.0"
}
```


> Dibuat sebagai bagian dari praktik tahap **Deployment** dalam metode **CRISP-DM**.  
> Proyek ini dapat dijadikan dasar pengembangan API prediksi sederhana lainnya.
