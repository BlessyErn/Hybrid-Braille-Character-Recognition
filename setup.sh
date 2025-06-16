#!/bin/bash
pyenv install 3.11.9 -s
pyenv global 3.11.9
python -m pip install --upgrade pip
pip install -r requirements.txt
