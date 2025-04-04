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
    
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Clean and create dist directory
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    os.makedirs('dist')
    
    # List of PNG files to include
    png_files = ['chair.png', 'table.png', 'sofa.png', 'cabinet.png', 'bed.png', 'shelf.png']
    
    # Build the executable with PNG files included
    pyinstaller_args = [
        'main.py',
        '--onefile',
        '--windowed',
        '--clean',
        '--name', 'Furniture Inventory & Management System.exe',
    ]
    
    # Add each PNG file as a data file
    for png in png_files:
        pyinstaller_args.extend(['--add-data', f'{png};.'])
    
    PyInstaller.__main__.run(pyinstaller_args)
    
    # Create dist/data directory and copy database
    os.makedirs(os.path.join('dist', 'data'), exist_ok=True)
    
    # Copy database if it exists
    try:
        shutil.copy2(
            os.path.join('data', 'placeholderData.db'),
            os.path.join('dist', 'data', 'placeholderData.db')
        )
    except FileNotFoundError:
        print("Note: Database file not found. It will be created on first run.")
    
    # Copy PNG files to dist directory
    for png in png_files:
        try:
            shutil.copy2(png, os.path.join('dist', png))
        except FileNotFoundError:
            print(f"Warning: {png} not found, the program may not display all images correctly.")
    
    # Clean up build directory
    if os.path.exists('build'):
        shutil.rmtree('build')

if __name__ == '__main__':
    build()

#Documention on how to build the application
#step one: run the script.py file. This will create a dist folder with the executable file and the database file.