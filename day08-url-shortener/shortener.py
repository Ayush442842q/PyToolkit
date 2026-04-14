import requests
import json
import os
from datetime import datetime

# PyToolkit - Day 08
# Tool: URL Shortener
# Author: Ayush442842q
# Description: Shorten URLs using TinyURL API and track history

TINYURL_API = "https://tinyurl.com/api-create.php"
HISTORY_FILE = "url_history.json"
