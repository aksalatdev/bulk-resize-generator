# 🖼️ Resize Gambar 224x224 px Online

Aplikasi web sederhana untuk me-resize banyak gambar sekaligus menjadi ukuran 224x224 pixel. Cocok untuk persiapan dataset machine learning atau keperluan lainnya.

## ✨ Fitur Utama

-   📁 **Upload ZIP**: Upload file ZIP berisi banyak gambar (JPEG/PNG)
-   🔄 **Auto Resize**: Otomatis resize semua gambar menjadi 224x224 pixel
-   📊 **Progress Bar**: Tampilan progress real-time saat proses resize
-   📥 **Download ZIP**: Download hasil resize dalam format ZIP
-   👀 **Preview**: Tampilan preview 4-6 gambar hasil resize
-   🚀 **Responsif**: Interface yang user-friendly dan responsif

## 🛠️ Teknologi

-   **Framework**: Python Streamlit
-   **Image Processing**: Pillow (PIL)
-   **File Handling**: zipfile, io
-   **UI Components**: Streamlit native widgets

## 📋 Persyaratan Sistem

-   Python 3.7+
-   Pip package manager
-   Browser modern (Chrome, Firefox, Safari, Edge)

## 🚀 Instalasi & Menjalankan

### 1. Clone Repository

```bash
git clone <repository-url>
cd resizeBulk
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi

```bash
streamlit run app.py
```

### 4. Buka Browser

Aplikasi akan otomatis terbuka di browser atau akses: `http://localhost:8501`

## 📁 Struktur Project

```
resizeBulk/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Dokumentasi project
├── assets/            # Static files (images, icons)
│   └── images/
├── uploads/           # Temporary upload folder
├── outputs/           # Processed images folder
└── utils/            # Utility functions
    └── image_processor.py
```

## 🎯 Cara Penggunaan

1. **Upload ZIP File**

    - Gunakan widget file uploader Streamlit
    - Drag & drop atau klik untuk memilih file ZIP
    - File ZIP harus berisi gambar format JPEG/PNG
    - Maksimal ukuran file: 200MB

2. **Proses Resize**

    - Klik tombol "Start Resize Process"
    - Progress bar akan menampilkan kemajuan real-time
    - Sistem akan otomatis resize semua gambar ke 224x224px

3. **Preview & Download**
    - Setelah proses selesai, preview gambar akan ditampilkan
    - Klik tombol "Download Resized Images" untuk mengunduh ZIP
    - File hasil akan berformat: `resized_images_TIMESTAMP.zip`

## 🔧 Konfigurasi

### Pengaturan Ukuran Default

Ubah ukuran default di file `utils/image_processor.py`:

```python
DEFAULT_SIZE = (224, 224)  # Ubah sesuai kebutuhan
```

### Pengaturan Upload

Ubah konfigurasi di `app.py`:

```python
# Streamlit file uploader config
MAX_FILE_SIZE = 200  # MB
ALLOWED_EXTENSIONS = ['zip']
```

## 📊 Format File yang Didukung

### Input

-   **ZIP File**: Berisi gambar-gambar
-   **Format Gambar**: JPEG (.jpg, .jpeg), PNG (.png)

### Output

-   **Format**: Sama dengan input (JPEG/PNG)
-   **Ukuran**: 224x224 pixel
-   **Kompresi**: Otomatis optimized

## 🚨 Troubleshooting

### Error: "File too large"

-   Pastikan ukuran ZIP file tidak melebihi 200MB
-   Kompres gambar sebelum di-zip jika perlu

### Error: "Streamlit connection error"

-   Restart aplikasi dengan `streamlit run app.py`
-   Clear browser cache dan refresh halaman

### Error: "Memory error"

-   Reduce jumlah gambar dalam ZIP
-   Restart aplikasi jika perlu

## 🔒 Keamanan

-   File upload dibatasi format dan ukuran
-   Temporary files dibersihkan otomatis
-   Validasi file extension dan MIME type
-   Sanitization nama file

## 📈 Performance

-   **Streamlit Caching**: Optimized dengan st.cache untuk performa
-   **Memory Management**: Efficient handling untuk file besar
-   **Progress Tracking**: Real-time progress dengan st.progress
-   **Session State**: Maintain state untuk user experience yang baik

## 🤝 Kontribusi

1. Fork repository ini
2. Buat branch feature (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📄 Lisensi

Project ini menggunakan lisensi MIT. Lihat file `LICENSE` untuk detail lengkap.

## 📞 Kontak & Support

-   **Issues**: Gunakan GitHub Issues untuk bug report
-   **Discussions**: Gunakan GitHub Discussions untuk pertanyaan
-   **Email**: [emailgw@domain.com]

## 🎯 Roadmap

-   [ ] Support format gambar tambahan (GIF, BMP, TIFF)
-   [ ] Multiple size options (512x512, 1024x1024)
-   [ ] Sidebar untuk pengaturan advanced
-   [ ] Custom watermark option
-   [ ] Batch processing dengan multiple ZIP files
-   [ ] Export ke Google Drive/OneDrive

## 📝 Changelog

### v1.0.0 (Current)

-   ✅ Streamlit file uploader untuk ZIP files
-   ✅ Real-time progress bar dengan st.progress
-   ✅ Image preview dengan st.image
-   ✅ Download button untuk hasil resize
-   ✅ Clean dan intuitive Streamlit interface

---

**🌟 Jika project ini membantu, jangan lupa kasih star di GitHub!**
