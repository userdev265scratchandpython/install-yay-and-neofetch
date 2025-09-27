import os, time
user = os.getlogin()
if os.path.exists(f"/home/{user}/.config/alacritty/alacritty.toml"):
    os.system(f"mv /home/{user}/.config/alacritty/alacritty.toml /home/{user}/.config/alacritty/alacritty.toml.old")
os.system("mkdir /home/user/yay ; sudo chmod 777 /home/user/yay")
os.system("mkdir -p /tmp/udev265sap/")
os.system("cd /tmp/udev265sap ; sudo chmod 777 /tmp/ ; sudo chmod 777 /tmp/* ; sudo touch /tmp/udev265sap/installer.sh ; sudo chmod 777 /tmp/udev265sap/installer.sh")
bash_contents = r"""
echo "installig needed components..."
sudo pacman -Syu --needed --noconfirm git base-devel > /dev/null 2>&1
git clone https://aur.archlinux.org/yay.git > /dev/null 2>&1
cd yay
makepkg -si
clear
yay -Syu --noconfirm --needed neofetch i3wm sway foot alacritty
clear
mkdir -p ~/.config/alacritty
clear
echo "installed needed components"
echo "saying yes(pressing y) will cause installation of catppuccin-mocha to alacritty. Some things can ONLY be done by user."
read -n 1 -r -p "Do you want to proceed? (y/n)" catppuccin
clear

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
    echo -n "making config... "
    echo [font] > ~/.config/alacritty/alacritty.toml
    echo size = 5.0 >> ~/.config/alacritty/alacritty.toml
    echo "[general]" >> ~/.config/alacritty/alacritty.toml
    echo "import = [\"$HOME/.config/alacritty/catppuccin.toml\"]" >> ~/.config/alacritty/alacritty.toml
    echo "[env]" >> ~/.config/alacritty/alacritty.toml
    echo "TERM = \"xterm-256color\"" >> ~/.config/alacritty/alacritty.toml
    echo "done"
    return
}

ask_install_catppuccin() {
    if [[ $catppuccin == "y" || $catppuccin == "Y" ]]; then
        git clone https://github.com/catppuccin/alacritty.git > /dev/null 2>&1
        ask_catppuccin_palette
        return
    elif [[ $catppuccin == "n" || $catppuccin == "N" ]]; then
        echo -n "making config... "
        echo [font] > ~/.config/alacritty/alacritty.toml
        echo size = 5.0 >> ~/.config/alacritty/alacritty.toml
        echo "[env]" >> ~/.config/alacritty/alacritty.toml
        echo "TERM = \"xterm-256color\"" >> ~/.config/alacritty/alacritty.toml
        echo "done"
        return
    else
        ask_install_catppuccin
    fi
}

ask_install_catppuccin
clear
"""
with open("installer.sh", "w") as a:
    a.write(bash_contents)
os.system("sudo mv ./installer.sh /tmp/udev265sap/installer.sh ; sudo chmod +x /tmp/udev265sap/installer.sh ; bash /tmp/udev265sap/installer.sh")
time.sleep(1)
os.system("sudo rm -rf /tmp/udev265sap")
