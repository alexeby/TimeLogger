rmdir /s /q dist ^
 & venv\Scripts\activate.bat ^
 && pyinstaller main.py -n="generate" --onefile ^
 && venv\Scripts\deactivate.bat ^
 && copy conf.ini dist