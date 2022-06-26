# railway-template-py
A template for python railway projects

## REQUIREMENTS.TXT
The `requirements.txt` holds your project's requirements, unsurprisingly. For it to work, simply write the required package's pypi name (for example: `py-dotenv`). Additionally, you can specify the package version using `==`, `>=`, etc... (for example: `python-dotenv==1.0.4`).

## RUNTIME.TXT
This file holds your Python version. In this template, Python 3.10.5 (`python-3.10.5`) is used as it is the latest available version, but you can specify any desired version.

## MAIN.PY
Copy/take inspiration from the code found in `main.py` to load the environment variables into your code.

## HOW TO SET ENVIRONMENT VARIABLES
The `production` [environment](https://docs.railway.app/develop/environments) is already available by default. To set up an [environment variable](https://docs.railway.app/develop/variables) you have to click on your project, then go to "Variables" and then simply add the variable of your choice.

Add.: For this template to "work", you'd have to name your venv "VENV_NAME", as per `main.py`'s code.
