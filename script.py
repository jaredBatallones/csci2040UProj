import subprocess
import sys
import os
import shutil

def ensure_pyinstaller():
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("PyInstaller installed successfully!")

def build():
    # Ensure PyInstaller is installed
    ensure_pyinstaller()
    
    # Now we can safely import PyInstaller
    import PyInstaller.__main__
    
    # Clean and create dist directory
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    os.makedirs('dist')
    
    # Build the executable
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--windowed',
        '--clean',
        '--name','Furniture Inventory & Management System.exe',
    ])
    os.makedirs(os.path.join('dist', 'data'), exist_ok=True)
    shutil.copy2(
        os.path.join('data', 'placeholderData.db'),
        os.path.join('dist', 'data', 'placeholderData.db')
    )
    if os.path.exists('build'):
        shutil.rmtree('build')

if __name__ == '__main__':
    build()

#Documention on how to build the application
#step one: run the script.py file. This will create a dist folder with the executable file and the database file.