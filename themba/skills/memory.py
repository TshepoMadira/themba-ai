import json
import os

MEMORY_FILE = "themba_memory.json"

def load_memory() -> list:
    """Load conversation history from file"""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(history: list):
    """Save conversation history to file"""
    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def add_to_memory(history: list, role: str, content: str) -> list:
    """Add a message to history"""
    history.append({"role": role, "content": content})
    # Keep only last 20 messages to avoid token limits
    if len(history) > 20:
        history = history[-20:]
    save_memory(history)
    return history

def clear_memory():
    """Clear all memory"""
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)
    return []