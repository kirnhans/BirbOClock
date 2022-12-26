Remove-Item venv -Recurse -ErrorAction Ignore
python -m venv venv
./venv/Scripts/Activate.ps1
pip install -r requirements.txt

if (Get-Command "deactivate" -errorAction SilentlyContinue) {
    deactivate
}
