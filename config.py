import os
from dotenv import load_dotenv
text = 'Продам руль Ua primo v2\n не гнут\n price - 2k'
filename = 'a.jpg'

load_dotenv()

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
