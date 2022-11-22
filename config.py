import os
from dotenv import load_dotenv
text = ''  # описание 
filename = 'a.jpg' # фотография которую хотите загрузить

load_dotenv()

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
