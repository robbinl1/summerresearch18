#!/bin/bash

cd iotapp/appfolder
export FLASK_APP=~/iotapp/iotapp.py
flask run --host 0.0.0.0
