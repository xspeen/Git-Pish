#!/bin/bash
# Git-Pish Installer - One-command setup for all platforms
# Author: xspeen

RED='\033[91m'
GREEN='\033[92m'
YELLOW='\033[93m'
CYAN='\033[96m'
RESET='\033[0m'

echo -e "${CYAN}╔══════════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${CYAN}║${GREEN}              Git-Pish Installer - One Command Setup              ${CYAN}║${RESET}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════════════╝${RESET}"

# Detect OS
if [[ -f /data/data/com.termux/files/usr/bin/termux-info ]]; then
    OS="termux"
    PKG_MANAGER="pkg"
    echo -e "${GREEN}[+] Termux detected${RESET}"
elif [[ -f /etc/debian_version ]]; then
    OS="debian"
    PKG_MANAGER="apt"
    echo -e "${GREEN}[+] Debian/Ubuntu/Parrot detected${RESET}"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
    PKG_MANAGER="brew"
    echo -e "${GREEN}[+] macOS detected${RESET}"
else
    OS="linux"
    PKG_MANAGER="apt"
    echo -e "${YELLOW}[!] Unknown OS, attempting with apt${RESET}"
fi

# Update and install Python
echo -e "${CYAN}[*] Installing Python and dependencies...${RESET}"

if [[ "$OS" == "termux" ]]; then
    $PKG_MANAGER update -y
    $PKG_MANAGER upgrade -y
    $PKG_MANAGER install git python python-pip openssh -y
elif [[ "$OS" == "macos" ]]; then
    brew update
    brew install python3 git
else
    sudo $PKG_MANAGER update -y
    sudo $PKG_MANAGER install git python3 python3-pip -y
fi

# Install Python packages
echo -e "${CYAN}[*] Installing Python packages...${RESET}"
pip3 install --upgrade pip 2>/dev/null || pip install --upgrade pip
pip3 install requests colorama termcolor 2>/dev/null || pip install requests colorama termcolor

# Create directories
mkdir -p logs assets modules

# Check if cloudflared is installed
if ! command -v cloudflared &> /dev/null; then
    echo -e "${YELLOW}[!] cloudflared not found. Installing...${RESET}"
    if [[ "$OS" == "termux" ]]; then
        pkg install cloudflared -y
    elif [[ "$OS" == "macos" ]]; then
        brew install cloudflared
    else
        wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared
        chmod +x cloudflared
        sudo mv cloudflared /usr/local/bin/
    fi
fi

# Make Python files executable
chmod +x git-pish.py git-pish-cli.py 2>/dev/null

echo -e "${GREEN}╔══════════════════════════════════════════════════════════════════╗${RESET}"
echo -e "${GREEN}║                    INSTALLATION COMPLETE!                         ║${RESET}"
echo -e "${GREEN}╚══════════════════════════════════════════════════════════════════╝${RESET}"
echo -e ""
echo -e "${CYAN}[*] Usage:${RESET}"
echo -e "    ${GREEN}python3 git-pish.py${RESET}           # Start phishing server"
echo -e "    ${GREEN}python3 git-pish-cli.py${RESET}       # Interactive CLI mode"
echo -e "    ${GREEN}python3 git-pish.py --tunnel cloudflare${RESET}  # Public URL via Cloudflare"
echo -e ""
echo -e "${YELLOW}[!] For authorized penetration testing only!${RESET}"
