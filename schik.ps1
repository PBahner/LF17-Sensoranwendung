python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -e python-app[dev]
pip install -r mkdocs\requirements.txt
Start-Process "C:\Program Files\JetBrains\PyCharm Community Edition 2024.1.3\bin\pycharm64.exe" "."
pause
