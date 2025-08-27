
#!/bin/bash
set -e

echo "=== Basic Installation and Setup ==="

# 1. Instal paket grafis dan driver media
sudo pacman -S --noconfirm mesa vulkan-intel intel-media-driver intel-ucode

# 2. Aktifkan multilib
if ! grep -q "^\[multilib\]" /etc/pacman.conf; then
    echo "Enable multilib..."
    sudo cp /etc/pacman.conf /etc/pacman.conf.bak
    sudo sed -i '/\[multilib\]/,/Include/s/^#//' /etc/pacman.conf
fi
sudo pacman -Sy

# 3. Instal paket 32-bit pendukung gaming
sudo pacman -S --noconfirm lib32-mesa lib32-vulkan-intel lib32-freetype2

# 4. Konfigurasi mkinitcpio
# Tambahkan i915 ke MODULES jika belum ada
if ! grep -q "i915" /etc/mkinitcpio.conf; then
    sudo sed -i '/^MODULES=/ s/)/ i915)/' /etc/mkinitcpio.conf
fi

# Pastikan kompresi pakai zstd
if grep -q "^COMPRESSION=" /etc/mkinitcpio.conf; then
    sudo sed -i 's/^COMPRESSION=.*/COMPRESSION="zstd"/' /etc/mkinitcpio.conf
else
    echo 'COMPRESSION="zstd"' | sudo tee -a /etc/mkinitcpio.conf
fi

sudo mkinitcpio -P

# 5. Optimasi GRUB
sudo sed -i 's/^GRUB_CMDLINE_LINUX_DEFAULT=.*/GRUB_CMDLINE_LINUX_DEFAULT="nowatchdog nvme_load=YES zswap.enabled=0 splash loglevel=3 quiet"/' /etc/default/grub
sudo grub-mkconfig -o /boot/grub/grub.cfg

echo "=== Configuration zram-generator ==="

# 1. Instalasi zram-generator
sudo pacman -S --noconfirm zram-generator

# 2. Buat konfigurasi zram-generator
sudo cp /etc/systemd/zram-generator.conf /etc/systemd/zram-generator.conf.bak 2>/dev/null || true
sudo tee /etc/systemd/zram-generator.conf > /dev/null <<EOF
[zram0]
zram-size = ram / 2
compression-algorithm = zstd
swap-priority = 100
fs-type = swap
EOF

# 3. Aktifkan zram-generator
sudo systemctl daemon-reexec
sudo systemctl restart systemd-zram-setup@zram0.service

echo "=== Setup complete. check zram with 'swapon --summary' ==="
