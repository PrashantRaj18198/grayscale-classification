#!/bin/bash

echo "installing requirements"
pip install -r requirements.txt
echo "downloading photos"
python3 downloadImages.py
echo "classifying photos"
python3 classify.py