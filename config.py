import json
import io
from typing import Dict, Any

settings : Dict[str, Any] = {}
# Load JSON settings file.
with open("settings.json", "r") as f:
    settings = json.load(f)
