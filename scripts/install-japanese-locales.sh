#!/bin/bash
set -e

FONT_DIR="$HOME/.fonts"

echo "Installing Japanese fonts..."
mkdir -p "$FONT_DIR"

# Download font
curl -L -o "$FONT_DIR/NotoSansJP-VariableFont_wght.ttf" \
  "https://github.com/gilang-arya/assets-repo/raw/main/fonts/NotoSansJP-VariableFont_wght.ttf"

# Refresh font cache
fc-cache -f "$FONT_DIR"

echo "Fonts downloaded and cache refreshed."

echo "Setting Japanese locales..."
# Tambahkan locale ke /etc/locale.gen jika belum ada
sudo sed -i 's/^#ja_JP.UTF-8 UTF-8/ja_JP.UTF-8 UTF-8/' /etc/locale.gen

echo "Generating locales..."
sudo locale-gen

echo "Installation complete!"
