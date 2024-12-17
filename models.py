from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50), nullable=False)
    umur = db.Column(db.Integer, nullable=False)
    tempat_lahir = db.Column(db.String(50), nullable=False)
    tanggal_lahir = db.Column(db.Date, nullable=False)
    jurusan = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    mata_kuliah = db.relationship('MataKuliah', backref='user_mata_kuliah', lazy=True)
    krs = db.relationship('KRS', back_populates='user', lazy=True)  # Changed to back_populates
    laporan_nilai = db.relationship('LaporanNilai', backref='user_laporan', lazy=True)  # Relasi ke LaporanNilai

    def __repr__(self):
        return f"<User {self.username}, {self.nama}, {self.jurusan}>"

class MataKuliah(db.Model):
    __tablename__ = 'mata_kuliah'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    kode_matkul = db.Column(db.String(20), unique=True, nullable=False)
    nama_matkul = db.Column(db.String(100), nullable=False)
    sks = db.Column(db.Integer, nullable=False)
    nilai = db.Column(db.Float, nullable=True)  # Nullable agar bisa kosong
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    krs = db.relationship('KRS', back_populates='mata_kuliah', lazy=True)  # Changed to back_populates

    def __repr__(self):
        return f"<MataKuliah {self.kode_matkul} - {self.nama_matkul}>"

class KRS(db.Model):
    __tablename__ = 'krs'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    mata_kuliah_id = db.Column(db.Integer, db.ForeignKey('mata_kuliah.id'), nullable=False)

    user = db.relationship('User', back_populates='krs')  # Changed to back_populates
    mata_kuliah = db.relationship('MataKuliah', back_populates='krs')  # Changed to back_populates

    def __repr__(self):
        return f"<KRS User {self.user_id} MataKuliah {self.mata_kuliah_id}>"

class LaporanNilai(db.Model):
    __tablename__ = 'laporan_nilai'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ipk = db.Column(db.Float, nullable=False)
    total_sks = db.Column(db.Integer, nullable=False)
    status_mahasiswa = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('laporan_nilai_user', lazy=True))  # Ganti backref

    def __repr__(self):
        return f"<LaporanNilai User {self.user_id} IPK {self.ipk}>"
