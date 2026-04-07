import os
from dotenv import load_dotenv

project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
dotenv_path = os.path.join(project_dir, '.env')
print(f"Buscando .env em: {os.path.abspath(dotenv_path)}")
print(f"Arquivo existe? {os.path.exists(dotenv_path)}")

load_dotenv(dotenv_path)
print(f"USUARIO: {os.getenv('BASIC_AUTH_USERNAME')}")
print(f"SENHA: {os.getenv('BASIC_AUTH_PASSWORD')}")
