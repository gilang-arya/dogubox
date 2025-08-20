import os

# Root project
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")

# Daftar item menu
MENU_ITEMS = [
    "Install Japanese Locales",
    "Install Korean Locales",
    "Setup nvm for Fish",
    "Install yay (AUR Helper)"
]

# Perintah untuk tiap item
COMMANDS = {
    "Install Japanese Locales": ["bash", os.path.join(SCRIPTS_DIR, "install-japanese-locales.sh")],
    "Install Korean Locales": ["bash", os.path.join(SCRIPTS_DIR, "install-korean-locales.sh")],
    "Setup nvm for Fish": ["fish", os.path.join(SCRIPTS_DIR, "setup-nvm-fish.sh")],
    "Install yay (AUR Helper)": ["bash", os.path.join(SCRIPTS_DIR, "install-yay.sh")]
}
