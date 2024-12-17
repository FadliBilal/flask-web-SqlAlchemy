# Web Flask 

Web sederhana menggunakan Framework Python **Flask**.

## Prasyarat

Sebelum menjalankan aplikasi, pastikan Anda sudah menginstal:

- **Python 3.12**: Anda dapat mengunduhnya dari [python.org](https://www.python.org/downloads/).
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
  python3 -m venv my_venv  # Virtual environment terinstal dengan nama my_venv
  source my_venv/bin/activate  # Mengaktifkan virtual environment
  ```

- **Windows**:

  ```bash
  python -m venv my_venv  # Virtual environment terinstal dengan nama my_venv
  my_venv\Scripts\activate  # Mengaktifkan virtual environment
  ```

### 3. Install Dependensi
Setelah virtual environment aktif, instal semua dependensi yang dibutuhkan oleh proyek:

```bash
pip install flask
```

### 4. Jalankan Aplikasi
Setelah dependensi terinstal, jalankan aplikasi Flask dengan perintah berikut:

```bash
python app.py  # Menjalankan aplikasi
```

Atau, jika Anda lebih memilih menggunakan Flask CLI, jalankan perintah:

```bash
flask run  # Menjalankan aplikasi menggunakan Flask CLI
```

Flask akan berjalan di alamat [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Struktur Proyek

Berikut adalah struktur folder dan file dalam proyek ini:

```bash
.
├── app.py            # Aplikasi utama Flask / biasa disebut controller-nya
├── my_venv           # Virtual environment / hanya berisi Flask sebagai dependensi
├── templates/        # Folder untuk template HTML
└── static/           # Folder untuk file statis (CSS, JS, gambar)
```

## Catatan

- Pastikan virtual environment aktif saat bekerja dengan proyek ini untuk menghindari masalah dependensi.

**Selamat mencoba dan semangat!**
