#!/bin/sh
set -e

# === PARTITIONING ===
echo "==> Run cfdisk to create partitions (EFI + Linux)"
read -p "Insert disk (example: /dev/nvme0n1): " DISK
cfdisk $DISK

# Setelah keluar dari cfdisk, user inputkan path partisi
read -p "Input your EFI Filesystem Partition (example: /dev/nvme0n1p1): " PATH_BOOT
read -p "Input your Linux System Partition (example: /dev/nvme0n1p2): " PATH_LINUX
read -p "Input hostname: " HOSTNAME
read -p "Input timezone (example: Asia/Jakarta): " TIMEZONE
read -p "Enter new username: " USERNAME
read -s -p "Set root password: " ROOT_PASS; echo
read -s -p "Set password for $USERNAME: " USER_PASS; echo

# === FORMAT & MOUNT ===
mkfs.fat -F32 $PATH_BOOT
mkfs.btrfs -f $PATH_LINUX

mount $PATH_LINUX /mnt

# Buat subvolume
btrfs subvolume create /mnt/@
btrfs subvolume create /mnt/@home
btrfs subvolume create /mnt/@log
btrfs subvolume create /mnt/@cache
umount /mnt

# Mount subvolumes
mount -o noatime,compress=zstd,ssd,space_cache=v2,discard=async,subvol=@ $PATH_LINUX /mnt
mkdir -p /mnt/{boot/efi,home,var/log,var/cache}

mount -o noatime,compress=zstd,ssd,space_cache=v2,discard=async,subvol=@home $PATH_LINUX /mnt/home
mount -o noatime,compress=zstd,ssd,space_cache=v2,discard=async,subvol=@log $PATH_LINUX /mnt/var/log
mount -o noatime,compress=zstd,ssd,space_cache=v2,discard=async,subvol=@cache $PATH_LINUX /mnt/var/cache
mount $PATH_BOOT /mnt/boot/efi

# === BASE INSTALL ===
pacstrap -K /mnt base base-devel linux-zen linux-zen-headers linux-firmware btrfs-progs \
    micro sudo git networkmanager sof-firmware pipewire pipewire-pulse pipewire-jack \
    grub efibootmgr

genfstab -U /mnt > /mnt/etc/fstab

# === CONFIG SYSTEM ===
arch-chroot /mnt /bin/bash <<EOF
ln -sf /usr/share/zoneinfo/$TIMEZONE /etc/localtime
hwclock --systohc

sed -i 's/^#en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
locale-gen
echo "LANG=en_US.UTF-8" > /etc/locale.conf

echo "$HOSTNAME" > /etc/hostname

# === USERS & PASSWORDS ===
useradd -m -G wheel -s /bin/bash $USERNAME
echo "root:$ROOT_PASS" | chpasswd
echo "$USERNAME:$USER_PASS" | chpasswd

# === SUDO CONFIG (wheel group) ===
echo "%wheel ALL=(ALL:ALL) ALL" > /etc/sudoers.d/99_wheel
chmod 440 /etc/sudoers.d/99_wheel

# === ENABLE SERVICES ===
systemctl enable NetworkManager

# === INSTALL GRUB ===
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
EOF

# === CLEAR PASSWORD VARIABLE ===
unset ROOT_PASS USER_PASS

echo "==> Installation complete! 🎉 Reboot and login as $USERNAME"
