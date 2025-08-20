#!/usr/bin/env fish

# Pastikan Fish shell terbaru
echo "Installing Fisher plugin manager..."
# Install fisher jika belum ada
if not functions -q fisher
    curl -sL https://git.io/fisher | source && fisher install jorgebucaran/fisher
else
    echo "Fisher sudah terinstal, melewati instalasi."
end

echo "Installing nvm.fish..."
if not type -q node
    echo "Node.js belum terinstal, menginstal nvm.fish dan Node.js..."
    fisher install jorgebucaran/nvm.fish

    # Reload konfigurasi Fish agar nvm tersedia
    status --is-interactive; and source (fisher --config)

    # Install versi Node.js terbaru
    echo "Installing latest Node.js..."
    nvm install latest

    # Set default versi Node.js
    set --universal nvm_default_version latest

    echo "Installation complete!"
else
    echo "Node.js sudah tersedia, melewati instalasi nvm.fish dan Node.js."
end
