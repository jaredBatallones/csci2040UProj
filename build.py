import PyInstaller.__main__
import os
import shutil

def build():
    # Clean and create dist directory
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    os.makedirs('dist')
    
    # Build the executable
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--windowed',
        '--clean'
    ])
    
    # Create data directory and copy database
    os.makedirs(os.path.join('dist', 'data'), exist_ok=True)
    shutil.copy2(
        os.path.join('data', 'placeholderData.db'),
        os.path.join('dist', 'data', 'placeholderData.db')
    )

if __name__ == '__main__':
    build()