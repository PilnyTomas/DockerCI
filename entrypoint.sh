#!/bin/sh -l

echo "Hello From docker entryopint.sh"
python script.py
echo "Python script finished and returned ${?}"
