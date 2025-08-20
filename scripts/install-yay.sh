#!/bin/bash

# Mengecek apakah yay sudah terinstal
if ! command -v yay &> /dev/null
then
    echo "yay belum terinstal. Installing dependencies..."
    sudo pacman -S --needed git base-devel

    # Tentukan folder sementara untuk clone
    TEMP_DIR="$HOME/yay_temp"

    # Hapus folder sementara kalau sudah ada
    [ -d "$TEMP_DIR" ] && rm -rf "$TEMP_DIR"

    echo "Cloning yay from AUR..."
    git clone https://aur.archlinux.org/yay.git "$TEMP_DIR"

    cd "$TEMP_DIR" || exit

    echo "Building and installing yay..."
    makepkg -si

    echo "yay installation complete!"

    # Hapus folder sementara setelah instalasi
    rm -rf "$TEMP_DIR"

else
    echo "yay sudah terinstal, melewati instalasi."
fi
