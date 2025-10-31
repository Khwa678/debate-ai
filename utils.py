# utils.py
import os, json
from datetime import datetime
from difflib import SequenceMatcher
from dotenv import load_dotenv
load_dotenv()

def ensure_log_dir(path="logs"):
    os.makedirs(path, exist_ok=True)
    return path

def create_log_file(prefix="debate"):
    log_dir = ensure_log_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(log_dir, f"{prefix}_{ts}.log.jsonl")
    return path

def append_log(log_path, entry: dict):
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

def similar(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()
