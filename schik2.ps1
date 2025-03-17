$githubCloneUrl="https://github.com/PBahner/LF17-Sensoranwendung.git"
set HTTP_PROXY=kjs-04.lan.dd-schulen.de:3128
set HTTPS_PROXY=kjs-04.lan.dd-schulen.de:3128
git config --global http.sslbackend openssl
git config --global http.proxy http://kjs-04.lan.dd-schulen.de:3128
git clone $githubCloneUrl
Set-Location -Path .\LF17-Sensoranwendung
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -e python-app[dev]
pip install -r mkdocs\requirements.txt
Start-Process "C:\Program Files\JetBrains\PyCharm Community Edition 2024.1.3\bin\pycharm64.exe" "."
pause
