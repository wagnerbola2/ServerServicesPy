import os
from dotenv import load_dotenv

class envioment:
    server = ""
    def __init__(self):
        load_dotenv()
        self.server = os.getenv('SERVER')