import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
BASE_URL = "https://api.etherscan.io/api"
