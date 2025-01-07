$username=Read-Host -Prompt "Enter Github Username"
$key=Read-Host -Prompt "Enter Github Key"
$githubCloneUrl=-join("https://", $username, ":", $key, "@github.com/PBahner/LF17-Sensoranwendung.git")
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
pause
