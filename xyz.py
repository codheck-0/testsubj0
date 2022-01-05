import time
from dotenv import load_dotenv
load_dotenv()
import os

KEY=os.getenv('KEY')
print(time.time())
print(KEY)
