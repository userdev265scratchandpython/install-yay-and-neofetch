import os, time
bash_contents = r"""
sudo pacman -Syu --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
yay -Syu neofetch i3wm sway foot alacritty
clear
mkdir -p ~/.config/alacritty
echo [font] > ~/.config/alacritty/alacritty.toml
echo size = 5.0 >> ~/.config/alacritty/alacritty.toml
clear
echo "saying yes(pressing y) will cause installation of catppuccin-mocha to alacritty. Some things can ONLY be done by user."
read -n 1 -s -r -p "Do you want to proceed? (y/n)" catppuccin
echo

ask_catppuccin_palette() {
    echo 1 - Latté
    echo 2 - Frappé
    echo 3 - Macchiato
    echo 4 - Mocha
    read -n 1 -s -r -p "Which palette of catppuccin-mocha do you want?" palette
    if [[ $palette == "1" ]]; then
        cd alacritty
        cp ./catppuccin-latte.toml ~/.config/alacritty/catppuccin.toml
    elif [[ $palette == "2" ]]; then
        cd alacritty
        cp ./catppuccin-frappe.toml ~/.config/alacritty/catppuccin.toml
    elif [[ $palette == "3" ]]; then
        cd alacritty
        cp ./catppuccin-macchiato.toml ~/.config/alacritty/catppuccin.toml
    elif [[ $palette == "4" ]]; then
        cd alacritty
        cp ./catppuccin-mocha.toml ~/.config/alacritty/catppuccin.toml
    else
        ask_catppuccin_palette
    fi
    echo "[general]" >> ~/.config/alacritty/alacritty.toml
    echo "import = [\"$HOME/.config/alacritty/catppuccin.toml\"]" >> ~/.config/alacritty/alacritty.toml
    echo "[env]" >> ~/.config/alacritty/alacritty.toml
    echo "TERM = \"xterm-256color\"" >> ~/.config/alacritty/alacritty.toml
    return
}

ask_install_catppuccin() {
    if [[ $catppuccin == "y" || $catppuccin == "Y" ]]; then
        git clone https://github.com/catppuccin/alacritty.git
        ask_catppuccin_palette
        return
    elif [[ $catppuccin == "n" || $catppuccin == "N" ]]; then
        return
    else
        ask_install_catppuccin
    fi
}

ask_install_catppuccin
clear
"""
with open("/tmp/installer.sh", "w") as a:
    a.write(bash_contents)
os.chmod("/tmp/installer.sh", 0o755)
os.system("bash /tmp/installer.sh")
time.sleep(1)
os.system("sudo rm -rf /tmp")
