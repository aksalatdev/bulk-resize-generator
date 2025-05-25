# 🖼️ Resize Gambar 224x224 px Online

Aplikasi web sederhana untuk me-resize banyak gambar sekaligus menjadi ukuran yang dapat disesuaikan. Cocok untuk persiapan dataset machine learning atau keperluan lainnya.

## 📸 Preview Aplikasi

🔗 **[Lihat Semua Screenshot](https://imgur.com/a/vtkkooD)**

<div align="center">
  
###  ⚡ Proses & Hasil
![Interface Utama - Upload & Settings](https://i.imgur.com/kb5KUgw.png)

### 🖼️ Interface Utama(Sidebar) - Preview

![Proses Resize & Download](https://i.imgur.com/ygGazMT.png)

</div>

---

## ✨ Fitur Utama

-   📁 **Upload ZIP**: Upload file ZIP berisi banyak gambar (JPEG/PNG)
-   🔄 **Auto Resize**: Otomatis resize semua gambar dengan ukuran yang dapat disesuaikan
-   🏷️ **Custom Prefix**: Penamaan file output dengan prefix custom (contoh: `vulkanik_1.jpg`, `vulkanik_2.jpg`)
-   📏 **Flexible Size**: Atur ukuran target dari 64x64 hingga 2048x2048 pixel
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
├── uploads/           # Temporary upload folder
├── outputs/           # Processed images folder
└── utils/            # Utility functions
    └── image_processing.py
```

## 🎯 Cara Penggunaan

1. **Upload ZIP File**

    - Gunakan widget file uploader Streamlit
    - Drag & drop atau klik untuk memilih file ZIP
    - File ZIP harus berisi gambar format JPEG/PNG
    - Maksimal ukuran file: 200MB

2. **Atur Pengaturan (Sidebar)**

    - **Ukuran Target**: Atur lebar dan tinggi (64px - 2048px)
    - **Prefix Output**: Masukkan nama prefix untuk file output (contoh: "vulkanik")
    - Jika prefix kosong, akan menggunakan "resized" sebagai default

3. **Proses Resize**

    - Klik tombol "🚀 Start Resize Process"
    - Progress bar akan menampilkan kemajuan real-time
    - Sistem akan otomatis resize semua gambar sesuai ukuran yang dipilih

4. **Preview & Download**
    - Setelah proses selesai, preview gambar akan ditampilkan
    - Klik tombol "📦 Download ZIP Hasil Resize" untuk mengunduh
    - File hasil akan berformat: `<prefix>_images_TIMESTAMP.zip`
    - Nama file gambar: `<prefix>_1.jpg`, `<prefix>_2.jpg`, dll.

## 🔧 Konfigurasi

### Pengaturan Ukuran Target

Atur ukuran target melalui sidebar:

-   **Lebar**: 64px - 2048px (default: 224px)
-   **Tinggi**: 64px - 2048px (default: 224px)
-   Increment: 32px untuk setiap step

### Pengaturan Prefix Output

Atur nama prefix melalui sidebar:

-   **Default**: "resized" (jika input kosong)
-   **Custom**: Masukkan nama sesuai keinginan (contoh: "vulkanik", "dataset")
-   **Output**: File akan dinamai `<prefix>_1.jpg`, `<prefix>_2.jpg`, dst.

### Pengaturan Upload

Konfigurasi file upload (dapat diubah di `app.py`):

```python
# Streamlit file uploader config
MAX_FILE_SIZE = 200  # MB
ALLOWED_EXTENSIONS = ['zip']
SUPPORTED_IMAGE_FORMATS = ['.jpg', '.jpeg', '.png']
```

## 📊 Format File yang Didukung

### Input

-   **ZIP File**: Berisi gambar-gambar
-   **Format Gambar**: JPEG (.jpg, .jpeg), PNG (.png)

### Output

-   **Format**: Sama dengan input (JPEG/PNG)
-   **Ukuran**: Dapat disesuaikan (default 224x224 pixel)
-   **Penamaan**: `<prefix>_<nomor>.<ekstensi>` (contoh: `vulkanik_1.jpg`)
-   **Kompresi**: Otomatis optimized (JPEG: 95% quality)

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

-   [x] **Custom prefix untuk nama file output** ✅
-   [x] **Flexible sizing (64px - 2048px)** ✅
-   [x] **Sequential file naming** ✅
-   [ ] Support format gambar tambahan (GIF, BMP, TIFF)
-   [ ] Preset size options (128x128, 512x512, 1024x1024)
-   [ ] Custom watermark option
-   [ ] Batch processing dengan multiple ZIP files
-   [ ] Export ke Google Drive/OneDrive
-   [ ] Image quality settings
-   [ ] Bulk rename dengan pattern custom

## 📝 Changelog

### v1.1.0 (Current)

-   ✅ **Custom prefix untuk nama file output**
-   ✅ **Sequential file naming**: `<prefix>_1.jpg`, `<prefix>_2.jpg`, dst.
-   ✅ **Flexible target size**: 64px - 2048px dengan step 32px
-   ✅ **Improved sidebar**: Pengaturan ukuran dan prefix yang terpisah
-   ✅ **Better file naming**: Konsisten dengan format `<prefix>_images_timestamp.zip`

### v1.0.0

-   ✅ Streamlit file uploader untuk ZIP files
-   ✅ Real-time progress bar dengan st.progress
-   ✅ Image preview dengan st.image
-   ✅ Download button untuk hasil resize
-   ✅ Clean dan intuitive Streamlit interface

## 📷 Contoh Output

Berdasarkan file yang ada di workspace, berikut contoh hasil dari aplikasi:

### Input

-   File ZIP berisi gambar tanah podsol

### Output dengan prefix "podsol"

```
outputs/podsol_images_8f7cba9c.zip
├── podsol_1.jpg
├── podsol_2.jpg
├── podsol_3.jpg
├── ...
└── podsol_21.jpg
```

### Output default (tanpa prefix)

```
outputs/resized_images_f17e36fd.zip
├── resized_1.jpg
├── resized_2.jpg
├── resized_3.jpg
├── ...
└── resized_21.jpg
```

---

**🌟 Jika project ini membantu, jangan lupa kasih star di GitHub!**
