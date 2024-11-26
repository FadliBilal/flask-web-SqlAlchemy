#  Web Flask No Database

Web sederhana menggunakan Framework Python **Flask**.

## Prasyarat

Sebelum menjalankan aplikasi, pastikan Anda sudah menginstal:

- **Python 3**: Anda dapat mengunduhnya dari [python.org](https://www.python.org/downloads/). //disini saya menggunakan versi 3.12
- **pip**: Biasanya sudah terinstal bersama Python. Untuk memastikan, jalankan perintah berikut:
  
  ```bash
  pip --version
  ```

## Cara Menjalankan

Ikuti langkah-langkah berikut untuk menjalankan aplikasi ini di komputer Anda.

### 1. Clone Repository
Clone proyek ini ke dalam folder lokal Anda dengan perintah:

```bash
git clone https://github.com/FadliBilal/flask-web-noDB.git
cd flask-web-noDB
```

### 2. Setup Virtual Environment (Opsional)
Virtual environment membantu menjaga agar dependensi proyek terisolasi dari sistem Anda. Ini adalah langkah opsional, tetapi sangat disarankan.

Untuk membuat dan mengaktifkan virtual environment:

- **Linux/macOS**:

  ```bash
  python3 -m venv my_venv //virtual environtment terinstall dengan nama my_venv
  source venv/bin/activate //setelah active maka install flasknya
  ```

- **Windows**:

  ```bash
  python -m venv venv //virtual environtment terinstall dengan nama my_venv
  venv\Scripts\activate //setelah active maka install flasknya
  ```

### 3. Install Dependensi
Setelah virtual environment aktif, instal semua dependensi yang dibutuhkan oleh proyek:

```bash
pip install flask
```

### 4. Jalankan Aplikasi
Setelah dependensi terinstal, jalankan aplikasi Flask dengan perintah berikut:

```bash
python app.py atau flask run
```

Flask akan berjalan di alamat [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Struktur Proyek

Berikut adalah struktur folder dan file dalam proyek ini:

```bash
.
├── app.py            # Aplikasi utama Flask / biasa disebut controller nya
├── my_venv           # virtual environtment / install sesuai yang dibutuhkan untuk web ini hanya flask
├── templates/        # Folder untuk template HTML
└── static/           # Folder untuk file statis (CSS, JS, gambar)
```
