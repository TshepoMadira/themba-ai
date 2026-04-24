import os
import webbrowser
import subprocess

APPS = {
    "chrome": "google-chrome",
    "firefox": "firefox",
    "calculator": "gnome-calculator",
    "files": "nautilus",
    "terminal": "gnome-terminal",
    "notepad": "gedit",
    "vscode": "code",
}

WEBSITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://www.github.com",
    "gmail": "https://mail.google.com",
    "whatsapp": "https://web.whatsapp.com",
    "twitter": "https://www.twitter.com",
    "facebook": "https://www.facebook.com",
    "netflix": "https://www.netflix.com",
}

def open_website(url: str):
    """Open a website in browser"""
    webbrowser.open(url)
    return f"Opening {url}, sir."

def open_app(app_name: str):
    """Open a desktop application"""
    try:
        subprocess.Popen([app_name])
        return f"Opening {app_name}, sir."
    except Exception as e:
        return f"Could not open {app_name}: {str(e)}"

def handle_launch(user_input: str) -> str:
    """Detect and handle open/launch commands"""
    text = user_input.lower()

    # Check for websites
    for name, url in WEBSITES.items():
        if name in text:
            # Check if search is requested
            if "search" in text and "google" in text:
                query = text.split("search")[-1].strip().replace("for", "").strip()
                search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
                return open_website(search_url)
            return open_website(url)

    # Check for apps
    for name, cmd in APPS.items():
        if name in text:
            return open_app(cmd)

    return None