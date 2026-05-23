# Copyright (c) REYUX
# See the file 'LICENSE' for copying permission

try:
    import sys
    import os

    # WINDOWS
    if sys.platform.startswith("win"):
        os.system("cls")
        print("Installing the python modules required for the REYUX Tool:\n")

        packages = [
            "auto-py-to-exe",
            "bcrypt",
            "beautifulsoup4",
            "browser-cookie3",
            "colorama",
            "cryptography",
            "customtkinter",
            "deep-translator",
            "discord",
            "dnspython",
            "exifread",
            "GPUtil",
            "instaloader",
            "keyboard",
            "opencv-python",
            "phonenumbers",
            "piexif",
            "pillow",
            "psutil",
            "pyautogui",
            "pycryptodome",
            "pyinstaller",
            "pyqt5",
            "pyqtwebengine",
            "pywin32",
            "pyzipper",
            "rarfile",
            "requests",
            "screeninfo",
            "selenium",
            "setuptools",
            "urllib3",
            "whois"
        ]

        # Upgrade pip first
        os.system(f'"{sys.executable}" -m pip install --upgrade pip')

        # Install all packages
        for package in packages:
            print(f"Installing {package}...")
            os.system(f'"{sys.executable}" -m pip install {package}')

        print("\nAll modules installed successfully!")

        # Run main tool
        os.system(f'"{sys.executable}" REYUX.py')

    else:
        print("Unsupported operating system.")

except Exception as e:
    input(f"Error: {e}")