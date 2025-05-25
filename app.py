"""
Bulk Image Resizer - Streamlit Web Application
Resize multiple images from ZIP file to 224x224 pixels
"""

import streamlit as st
import os
import time
from datetime import datetime
import shutil
from utils.image_processing import process_bulk_resize, ImageProcessor

# Page configuration
st.set_page_config(
    page_title="Resize Gambar 224x224 px Online",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    .stProgress > div > div > div > div {
        background-color: #00cc88;
    }
    .upload-area {
        border: 2px dashed #cccccc;
        border-radius: 10px;
        padding: 40px;
        text-align: center;
        background-color: #f8f9fa;
        margin: 20px 0;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        margin: 1rem 0;
    }
    .error-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        margin: 1rem 0;
    }
    .info-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


def initialize_directories():
    """Create necessary directories if they don't exist"""
    directories = ['uploads', 'outputs', 'assets']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def cleanup_old_files():
    """Clean up old temporary files"""
    try:
        # Clean uploads older than 1 hour
        current_time = time.time()
        for directory in ['uploads', 'outputs']:
            if os.path.exists(directory):
                for item in os.listdir(directory):
                    item_path = os.path.join(directory, item)
                    if os.path.isdir(item_path):
                        # Check if directory is older than 1 hour
                        if current_time - os.path.getctime(item_path) > 3600:
                            shutil.rmtree(item_path)
    except Exception as e:
        st.warning(f"Warning: Could not clean old files: {str(e)}")


def display_image_preview(image_paths, title="Preview Gambar"):
    """Display image preview in grid layout"""
    if not image_paths:
        return

    st.subheader(title)

    # Create columns for image grid
    cols = st.columns(min(len(image_paths), 4))

    for i, img_path in enumerate(image_paths[:4]):
        if os.path.exists(img_path):
            with cols[i % 4]:
                try:
                    st.image(img_path, caption=os.path.basename(
                        img_path), use_container_width=True)
                except Exception as e:
                    st.error(
                        f"Error displaying {os.path.basename(img_path)}: {str(e)}")

    if len(image_paths) > 4:
        st.info(f"Menampilkan 4 dari {len(image_paths)} gambar hasil resize")


def display_processing_stats(result):
    """Display processing statistics"""
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Gambar", result['total_processed'])

    with col2:
        st.metric("Berhasil", result['successful'], delta=None)

    with col3:
        st.metric("Gagal", result['failed'], delta=None if result['failed']
                  == 0 else f"-{result['failed']}")


def main():
    # Initialize
    initialize_directories()
    cleanup_old_files()

    # Header
    st.title("🖼️ Resize Gambar 224x224 px Online")
    st.markdown(
        "### Aplikasi untuk me-resize banyak gambar sekaligus menjadi ukuran 224x224 pixel")

    # Sidebar - Settings
    st.sidebar.title("⚙️ Pengaturan")

    # Target size settings
    st.sidebar.subheader("Ukuran Target")
    width = st.sidebar.number_input(
        "Lebar (px)", min_value=64, max_value=2048, value=224, step=32)
    height = st.sidebar.number_input(
        "Tinggi (px)", min_value=64, max_value=2048, value=224, step=32)
    target_size = (width, height)

    # Info section
    st.sidebar.subheader("ℹ️ Informasi")
    st.sidebar.info("""
    **Format yang didukung:**
    - ZIP file berisi gambar
    - Format gambar: JPG, JPEG, PNG
    
    **Fitur:**
    - Resize otomatis ke ukuran yang dipilih
    - Preview hasil resize
    - Download ZIP hasil
    - Progress tracking real-time
    """)

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        # File upload section
        st.subheader("📁 Upload File ZIP")

        # Upload area with custom styling
        st.markdown('<div class="upload-area">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Pilih file ZIP yang berisi gambar",
            type=['zip'],
            help="Upload file ZIP yang berisi gambar dalam format JPG, JPEG, atau PNG"
        )
        st.markdown('</div>', unsafe_allow_html=True)

        # Display file info if uploaded
        if uploaded_file is not None:
            file_size_mb = uploaded_file.size / (1024 * 1024)
            st.markdown(f"""
            <div class="info-box">
                <strong>File terpilih:</strong> {uploaded_file.name}<br>
                <strong>Ukuran:</strong> {file_size_mb:.2f} MB<br>
                <strong>Target resize:</strong> {width}x{height} pixels
            </div>
            """, unsafe_allow_html=True)

    with col2:
        # Instructions
        st.subheader("📋 Cara Penggunaan")
        st.markdown("""
        1. **Upload ZIP** - Pilih file ZIP berisi gambar
        2. **Set Ukuran** - Atur ukuran target di sidebar
        3. **Proses** - Klik tombol "Start Resize Process"
        4. **Preview** - Lihat hasil preview
        5. **Download** - Unduh ZIP hasil resize
        """)

    # Processing section
    if uploaded_file is not None:
        st.divider()

        # Processing button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            process_button = st.button(
                "🚀 Start Resize Process",
                type="primary",
                use_container_width=True
            )

        # Process images when button is clicked
        if process_button:
            # Validate file size (200MB limit)
            if uploaded_file.size > 200 * 1024 * 1024:
                st.error(
                    "❌ File terlalu besar! Maksimal ukuran file adalah 200MB.")
                return

            # Processing container
            with st.container():
                st.subheader("⚡ Memproses Gambar...")

                # Progress indicators
                progress_bar = st.progress(0)
                status_text = st.empty()

                # Start processing
                start_time = time.time()
                status_text.text("🔄 Mengekstrak file ZIP...")

                try:
                    # Process images
                    result = process_bulk_resize(uploaded_file, target_size)

                    # Update progress
                    progress_bar.progress(100)
                    processing_time = time.time() - start_time

                    if result['success']:
                        status_text.text(
                            f"✅ Selesai! Waktu pemrosesan: {processing_time:.2f} detik")

                        # Success message
                        st.markdown(f"""
                        <div class="success-box">
                            <strong>🎉 Proses resize berhasil!</strong><br>
                            {result['successful']} gambar berhasil diresize dari total {result['total_processed']} gambar.
                        </div>
                        """, unsafe_allow_html=True)

                        # Display statistics
                        display_processing_stats(result)

                        # Display preview
                        if result['resized_files']:
                            st.divider()
                            display_image_preview(
                                result['resized_files'], "🖼️ Preview Hasil Resize")

                        # Download section
                        st.divider()
                        st.subheader("📥 Download Hasil")

                        if os.path.exists(result['output_zip_path']):
                            with open(result['output_zip_path'], "rb") as file:
                                zip_data = file.read()

                            st.download_button(
                                label="📦 Download ZIP Hasil Resize",
                                data=zip_data,
                                file_name=f"resized_images_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip",
                                mime="application/zip",
                                type="primary",
                                use_container_width=True
                            )

                            zip_size_mb = len(zip_data) / (1024 * 1024)
                            st.info(
                                f"📊 Ukuran file ZIP hasil: {zip_size_mb:.2f} MB")

                        # Cleanup temporary files
                        for cleanup_dir in result.get('cleanup_dirs', []):
                            if os.path.exists(cleanup_dir):
                                shutil.rmtree(cleanup_dir)

                    else:
                        status_text.text("❌ Proses gagal!")
                        st.markdown(f"""
                        <div class="error-box">
                            <strong>❌ Terjadi kesalahan:</strong><br>
                            {result['error']}
                        </div>
                        """, unsafe_allow_html=True)

                        # Cleanup on error
                        for cleanup_dir in result.get('cleanup_dirs', []):
                            if os.path.exists(cleanup_dir):
                                shutil.rmtree(cleanup_dir)

                except Exception as e:
                    progress_bar.progress(0)
                    status_text.text("❌ Terjadi kesalahan!")
                    st.markdown(f"""
                    <div class="error-box">
                        <strong>❌ Error tidak terduga:</strong><br>
                        {str(e)}
                    </div>
                    """, unsafe_allow_html=True)

    # Footer
    st.divider()
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p>🖼️ <strong>Bulk Image Resizer</strong> | Dibuat dengan ❤️ menggunakan Streamlit</p>
        <p><small>Aplikasi untuk membantu resize gambar secara batch dengan mudah dan cepat.</small></p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
