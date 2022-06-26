from os import getenv
from dotenv import load_dotenv


load_dotenv() # Boilerplate


__SUPER_SECRET_STUFF = getenv("VENV_NAME") # Of course, you have to take into account the path between main.py and .env

print(__SUPER_SECRET_STUFF) # Tada 🎉
