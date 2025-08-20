# Dogubox

**Dogubox** is a personal Arch Linux setup toolkit focused on automation.

## Installation

```bash
git clone https://github.com/gilang-arya/dogubox.git
cd dogubox
```

## Usage

```bash
./dogubox
```

## Structure

```bash
dogubox/
├── dogubox                 # Main wrapper script
├── arch-btrfs-install.sh   # Btrfs installer
├── scripts/                # Supporting scripts
└── src/                    # Custom tools
```

## Minimal Arch Linux Install

To perform a minimal Arch Linux installation using Btrfs, you can run:

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/gilang-arya/dogubox/main/arch-btrfs-install.sh)"
```
