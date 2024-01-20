set dotenv-load

serve:
  python3 App/App.py

fmt:
  yapf --in-place --recursive **/*.py

run *args:
  python3 placeholder {{args}}

install *pkg:
  pip3 install {{pkg}} 

lock:
  pipreqs .

env:
  python3 -m venv venv

deps:
  pip3 install -r requirements.txt
