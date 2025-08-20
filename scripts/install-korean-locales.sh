#!/bin/bash
set -e

FONT_DIR="$HOME/.fonts"

echo "Installing Korean fonts..."
mkdir -p "$FONT_DIR"

# Download font
curl -L -o "$FONT_DIR/NotoSansKR-VariableFont_wght.ttf" \
  "https://github.com/gilang-arya/assets-repo/raw/main/fonts/NotoSansKR-VariableFont_wght.ttf"

# Refresh font cache
fc-cache -f "$FONT_DIR"

echo "Fonts downloaded and cache refreshed."

echo "Setting Korean locales..."
# Tambahkan locale ke /etc/locale.gen jika belum ada
sudo sed -i 's/^#ko_KR.UTF-8 UTF-8/ko_KR.UTF-8 UTF-8/' /etc/locale.gen

echo "Generating locales..."
sudo locale-gen

echo "Installation complete!"

