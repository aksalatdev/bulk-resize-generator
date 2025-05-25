"""
Image Processing Module for Bulk Image Resizer
Handles image extraction, resizing, and ZIP creation
"""

import os
import zipfile
import shutil
import uuid
from PIL import Image
from typing import List, Tuple
import tempfile


class ImageProcessor:
    def __init__(self, target_size: Tuple[int, int] = (224, 224)):
        """
        Initialize ImageProcessor with target size

        Args:
            target_size: Target size for resized images (width, height)
        """
        self.target_size = target_size
        self.supported_formats = ['.jpg', '.jpeg',
                                  '.png', '.JPG', '.JPEG', '.PNG']

    def extract_zip(self, zip_file_path: str, extract_to: str) -> List[str]:
        """
        Extract ZIP file and return list of image file paths

        Args:
            zip_file_path: Path to the ZIP file
            extract_to: Directory to extract files to

        Returns:
            List of extracted image file paths
        """
        image_files = []

        try:
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                # Extract all files
                zip_ref.extractall(extract_to)

                # Get list of extracted files
                for root, dirs, files in os.walk(extract_to):
                    for file in files:
                        file_path = os.path.join(root, file)
                        # Check if file is a supported image format
                        if any(file.lower().endswith(ext.lower()) for ext in self.supported_formats):
                            image_files.append(file_path)

            return image_files

        except Exception as e:
            raise Exception(f"Error extracting ZIP file: {str(e)}")

    def resize_image(self, input_path: str, output_path: str) -> bool:
        """
        Resize a single image to target size

        Args:
            input_path: Path to input image
            output_path: Path to save resized image

        Returns:
            True if successful, False otherwise
        """
        try:
            # Open and resize image
            with Image.open(input_path) as img:
                # Convert to RGB if necessary (for PNG with transparency)
                if img.mode in ('RGBA', 'LA', 'P'):
                    rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGB')
                    else:
                        rgb_img.paste(img, mask=img.split()
                                      [-1] if img.mode == 'RGBA' else None)
                        img = rgb_img

                # Resize with high quality
                resized_img = img.resize(
                    self.target_size, Image.Resampling.LANCZOS)                # Determine output format and quality
                output_format = 'JPEG' if input_path.lower().endswith(('.jpg', '.jpeg')) else 'PNG'

                if output_format == 'JPEG':
                    resized_img.save(
                        output_path, format=output_format, quality=95, optimize=True)
                else:
                    resized_img.save(
                        output_path, format=output_format, optimize=True)

                return True

        except Exception as e:
            print(f"Error resizing image {input_path}: {str(e)}")
            return False

    def resize_images_batch(self, image_files: List[str], output_dir: str, prefix: str = "resized", progress_callback=None) -> Tuple[List[str], int, int]:
        """
        Resize multiple images in batch

        Args:
            image_files: List of image file paths to resize
            output_dir: Directory to save resized images
            prefix: Prefix for output filenames
            progress_callback: Optional callback function for progress updates

        Returns:
            Tuple of (resized_file_paths, successful_count, failed_count)
        """
        resized_files = []
        successful = 0
        failed = 0

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        total_files = len(image_files)

        for i, image_path in enumerate(image_files):
            try:
                # Generate output filename with sequential numbering
                filename = os.path.basename(image_path)
                _, ext = os.path.splitext(filename)

                # Ensure JPEG extension for JPG files
                if ext.lower() in ['.jpg', '.jpeg']:
                    ext = '.jpg'
                elif ext.lower() == '.png':
                    ext = '.png'

                output_filename = f"{prefix}_{i + 1}{ext}"
                output_path = os.path.join(output_dir, output_filename)

                # Resize the image
                if self.resize_image(image_path, output_path):
                    resized_files.append(output_path)
                    successful += 1
                else:
                    failed += 1

                # Update progress
                if progress_callback:
                    progress_callback(i + 1, total_files)

            except Exception as e:
                print(f"Error processing {image_path}: {str(e)}")
                failed += 1

                if progress_callback:
                    progress_callback(i + 1, total_files)

        return resized_files, successful, failed

    def create_zip(self, files: List[str], zip_path: str) -> bool:
        """
        Create ZIP file from list of files

        Args:
            files: List of file paths to include in ZIP
            zip_path: Path for the output ZIP file

        Returns:
            True if successful, False otherwise
        """
        try:
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
                for file_path in files:
                    if os.path.exists(file_path):
                        # Use only filename (not full path) in ZIP
                        arcname = os.path.basename(file_path)
                        zip_ref.write(file_path, arcname)

            return True

        except Exception as e:
            print(f"Error creating ZIP file: {str(e)}")
            return False

    def cleanup_directory(self, directory: str) -> bool:
        """
        Clean up temporary directory

        Args:
            directory: Directory path to clean up

        Returns:
            True if successful, False otherwise
        """
        try:
            if os.path.exists(directory):
                shutil.rmtree(directory)
            return True
        except Exception as e:
            print(f"Error cleaning up directory {directory}: {str(e)}")
            return False

    def get_image_info(self, image_path: str) -> dict:
        """
        Get basic information about an image

        Args:
            image_path: Path to the image file

        Returns:
            Dictionary with image information
        """
        try:
            with Image.open(image_path) as img:
                return {
                    'filename': os.path.basename(image_path),
                    'size': img.size,
                    'mode': img.mode,
                    'format': img.format,
                    'file_size': os.path.getsize(image_path)
                }
        except Exception as e:
            return {
                'filename': os.path.basename(image_path),
                'error': str(e)
            }


def process_bulk_resize(uploaded_file, target_size=(224, 224), prefix="resized") -> dict:
    """
    Main function to process bulk image resize

    Args:
        uploaded_file: Streamlit uploaded file object
        target_size: Target size for resized images
        prefix: Prefix for output filenames

    Returns:
        Dictionary with results
    """
    # Generate unique session ID
    session_id = str(uuid.uuid4())[:8]

    # Create temporary directories
    temp_dir = os.path.join("uploads", f"temp_{session_id}")
    output_dir = os.path.join("outputs", f"resized_{session_id}")

    try:
        # Create directories
        os.makedirs(temp_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        # Save uploaded file temporarily
        zip_path = os.path.join(temp_dir, "uploaded.zip")
        with open(zip_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Initialize processor
        processor = ImageProcessor(target_size)

        # Extract ZIP file
        extract_dir = os.path.join(temp_dir, "extracted")
        image_files = processor.extract_zip(zip_path, extract_dir)

        if not image_files:
            return {
                'success': False,
                'error': 'No valid image files found in ZIP',
                'cleanup_dirs': [temp_dir, output_dir]
            }        # Resize images
        resized_files, successful, failed = processor.resize_images_batch(
            image_files, output_dir, prefix
        )        # Create output ZIP
        output_zip_name = f"{prefix}_images_{session_id}.zip"
        output_zip_path = os.path.join("outputs", output_zip_name)

        if processor.create_zip(resized_files, output_zip_path):
            return {
                'success': True,
                'output_zip_path': output_zip_path,
                'resized_files': resized_files[:6],  # First 6 for preview
                'total_processed': len(image_files),
                'successful': successful,
                'failed': failed,
                'cleanup_dirs': [temp_dir],
                'session_id': session_id
            }
        else:
            return {
                'success': False,
                'error': 'Failed to create output ZIP file',
                'cleanup_dirs': [temp_dir, output_dir]
            }

    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'cleanup_dirs': [temp_dir, output_dir]
        }
