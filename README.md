# Aplikasi Web Flask Sederhana

Aplikasi web sederhana menggunakan **Flask**.

## Prasyarat

Sebelum menjalankan aplikasi, pastikan Anda sudah menginstal:

- **Python 3**: Anda dapat mengunduhnya dari [python.org](https://www.python.org/downloads/).
- **pip**: Biasanya sudah terinstal bersama Python. Untuk memastikan, jalankan perintah berikut:
  
  ```bash
  pip --version
  ```

## Cara Menjalankan

Ikuti langkah-langkah berikut untuk menjalankan aplikasi ini di komputer Anda.

### 1. Clone Repository
Clone proyek ini ke dalam folder lokal Anda dengan perintah:

```bash
git clone <URL_REPOSITORY>
cd <nama_folder_repositori>
```

### 2. Setup Virtual Environment (Opsional)
Virtual environment membantu menjaga agar dependensi proyek terisolasi dari sistem Anda. Ini adalah langkah opsional, tetapi sangat disarankan.

Untuk membuat dan mengaktifkan virtual environment:

- **Linux/macOS**:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **Windows**:

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Install Dependensi
Setelah virtual environment aktif, instal semua dependensi yang dibutuhkan oleh proyek:

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
Setelah dependensi terinstal, jalankan aplikasi Flask dengan perintah berikut:

```bash
python app.py
```

Aplikasi Flask akan berjalan di alamat [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Struktur Proyek

Berikut adalah struktur folder dan file dalam proyek ini:

```bash
.
├── app.py            # Aplikasi utama Flask
├── requirements.txt  # Daftar dependensi Python
├── templates/        # Folder untuk template HTML
└── static/           # Folder untuk file statis (CSS, JS, gambar)
```

### Penjelasan File dan Folder

- **app.py**: File utama untuk menjalankan aplikasi Flask.
- **requirements.txt**: Berisi daftar semua dependensi Python yang dibutuhkan untuk menjalankan aplikasi.
- **templates/**: Berisi file HTML yang digunakan untuk rendering halaman.
- **static/**: Digunakan untuk menyimpan file statis seperti gambar, CSS, dan JavaScript.

## Catatan

- Jika Anda menggunakan virtual environment, pastikan untuk mengaktifkannya setiap kali Anda bekerja dengan proyek ini.
- Jangan lupa untuk menambahkan file atau folder yang diperlukan ke dalam direktori **static/** dan **templates/** untuk pengembangan lebih lanjut.
