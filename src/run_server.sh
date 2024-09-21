import os
import subprocess

python_path = r"C:\Users\mathi\OneDrive\Documents\BUT2\pythonProject\venv\Scripts\python.exe"
manage_py_path = r"C:\Users\mathi\OneDrive\Documents\BUT2\pythonProject\src\manage.py"

subprocess.run([python_path, manage_py_path, "runserver"])