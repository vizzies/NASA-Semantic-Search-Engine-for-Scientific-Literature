from reusetracker import create_app
from dotenv import load_dotenv

load_dotenv('.env')

print("HELLO WORLD", flush=True)

app = create_app()