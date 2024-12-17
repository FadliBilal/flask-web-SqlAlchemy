from flask import Flask, render_template, request, redirect, session, url_for, flash
from models import db, User, MataKuliah
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.secret_key = 'kunci'

# Konfigurasi database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/db_mahasiswa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Membuat tabel jika belum ada
with app.app_context():
    db.create_all()

# Routes
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            print(f"User logged in: {user.id}")  # Debug log
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nama = request.form.get('nama')
        umur = request.form.get('umur', type=int)
        tempat_lahir = request.form.get('tempat_lahir')
        tanggal_lahir = request.form.get('tanggal_lahir')
        jurusan = request.form.get('jurusan')
        email = request.form.get('email')
        username = request.form.get('username')
        password = generate_password_hash(request.form.get('password'))

        # Validasi input
        if not all([nama, umur, tempat_lahir, tanggal_lahir, jurusan, email, username, password]):
            flash('All fields are required', 'danger')
            return redirect(url_for('register'))

        user = User(nama=nama, umur=umur, tempat_lahir=tempat_lahir, tanggal_lahir=tanggal_lahir, 
                    jurusan=jurusan, email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        print("User not logged in.")  # Debug log
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    print(f"User accessing dashboard: {user.id}")  # Debug log
    mata_kuliah = MataKuliah.query.filter_by(user_id=user.id).all()

    if request.method == 'POST':
        kode_matkul = request.form.get('kode_matkul')
        nama_matkul = request.form.get('nama_matkul')
        sks = request.form.get('sks', type=int)
        nilai = request.form.get('nilai', type=float)

        # Create MataKuliah object and save to database
        matkul = MataKuliah(user_id=user.id, kode_matkul=kode_matkul, nama_matkul=nama_matkul, sks=sks, nilai=nilai)
        db.session.add(matkul)
        db.session.commit()
        flash('Mata kuliah added successfully.', 'success')
        return redirect(url_for('dashboard'))  # Refresh the dashboard after adding the mata kuliah

    return render_template('dashboard.html', user=user, mata_kuliah=mata_kuliah)

@app.route('/krs')
def krs():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    mata_kuliah = MataKuliah.query.filter_by(user_id=user.id).all()
    return render_template('krs.html', user=user, mata_kuliah=mata_kuliah)

@app.route('/data_diri', methods=['GET', 'POST'])
def data_diri():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])

    if request.method == 'POST':
        user.nama = request.form.get('nama')
        user.umur = request.form.get('umur', type=int)
        user.tempat_lahir = request.form.get('tempat_lahir')
        user.tanggal_lahir = request.form.get('tanggal_lahir')
        user.jurusan = request.form.get('jurusan')
        user.email = request.form.get('email')
        db.session.commit()
        flash('Data updated successfully.', 'success')
        return redirect(url_for('data_diri'))

    return render_template('data_diri.html', user=user)

@app.route('/nilai')
def daftar_nilai():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    mata_kuliah = MataKuliah.query.filter_by(user_id=user.id).all()
    return render_template('daftar_nilai.html', user=user, mata_kuliah=mata_kuliah)

@app.route('/laporan')
def laporan_nilai():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    mata_kuliah = MataKuliah.query.filter_by(user_id=user.id).all()

    # Menghitung total nilai dan IPK
    total_nilai = sum(matkul.nilai * matkul.sks for matkul in mata_kuliah if matkul.nilai is not None)
    total_sks = sum(matkul.sks for matkul in mata_kuliah)
    ipk = total_nilai / total_sks if total_sks > 0 else 0
    status = 'Aktif' if ipk >= 2 else 'Tidak Aktif'

    return render_template('laporan_nilai.html', user=user, mata_kuliah=mata_kuliah, ipk=ipk, total_sks=total_sks, status=status)

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)