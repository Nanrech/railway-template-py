from os import getenv
from dotenv import load_dotenv


load_dotenv()

__SUPER_SECRET_STUFF = getenv("VENV_NAME")

print(__SUPER_SECRET_STUFF)
