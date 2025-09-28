import os, time, threading
logo1 = """loading...

###  ### ####  ##### #   #  222   6666 55555  ####   #   ####
##-  ###  #  # #     #   # 2   2 6     5     #      # #  #   #
##%  ###  #  # ###    # #    22  6666   555   ###   ###  ####
###  #%#  #  # #      # #  22    6   6     5     # #   # #
 ######  ####  #####   #   22222  666  5555  ####  #   # #   
userdev265scratchandpython"""

logo2 = """loading...

###  ###  #### ####  ##### #   #  ###   6666 55555  ####   #   ####
#@#  ### #      #  # #     #   # #   # 6     5     #      # #  #   #
###  #-#  ###   #  # ###    # #    ##  6666   555   ###   ###  ####
###  ###     #  #  # #      # #  ##    6   6     5     # #   # #
 ######  ####  ####  #####   #   #####  666  5555  ####  #   # #   
userdev265scratchandpython"""

logo3 = """loading...

###  ###  #### ##### ####  ##### #   #  ###   #### 55555  ####   #   ####
##-  ### #     #      #  # #     #   # #   # #     5     #      # #  #   #
###  ###  ###  ###    #  # ###    # #    ##  ####   555   ###   ###  ####
###  -##     # #      #  # #      # #  ##    #   #     5     # #   # #
 ######  ####  ##### ####  #####   #   #####  ###  5555  ####  #   # #   
userdev265scratchandpython"""

logo4 = """loading...

###  ###  #### ##### ####  ##### ####  #   #  ###   #### #####  ####   #   ####
##-  ### #     #      #  # #     #   # #   # #   # #     #     #      # #  #   #
###  ###  ###  ###    #  # ###   ####   # #    ##  ####   ###   ###   ###  ####
###  -##     # #      #  # #     # #    # #  ##    #   #     #     # #   # #
 ######  ####  ##### ####  ##### #  #    #   #####  ###  ####  ####  #   # #   
userdev265scratchandpython"""

def loading_animation():
    while run_check:
        print(logo1)
        time.sleep(1)
        os.system("clear")
        print(logo2)
        time.sleep(0.25)
        os.system("clear")
        print(logo3)
        time.sleep(0.25)
        os.system("clear")
        print(logo4)
        time.sleep(1)
        os.system("clear")
        print(logo3)
        time.sleep(0.25)
        os.system("clear")
        print(logo2)
        time.sleep(0.25)
        os.system("clear")
user = os.getlogin()
if os.path.exists(f"/home/{user}/.config/alacritty/alacritty.toml"):
    os.system(f"mv /home/{user}/.config/alacritty/alacritty.toml /home/{user}/.config/alacritty/alacritty.toml.old")
    os.system("""echo "[font]" > ~/.config/alacritty/alacritty.toml ; echo "size = 5.0" >> ~/.config/alacritty/alacritty.toml""")
os.system(f"mkdir /home/{user}/yay ; sudo chmod 777 /home/{user}/yay")
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
    echo "saying yes(pressing y) will cause installation of catppuccin to alacritty. Some things can ONLY be done by user."
    echo
    read -n 1 -r -p "Do you want to proceed? (y/n)" catppuccin
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

ask_install_catppuccin
sleep 1
clear
"""
def make_file():
    global run_check
    run_check = True
    os.system("touch installer.sh")
    for I in bash_contents:
        with open("installer.sh", "a") as a:
            a.write(I)
            time.sleep(60/len(bash_contents))
    run_check = False
loading_thread = threading.Thread(target=make_file)
loading_thread.daemon = True
loading_thread.start()
loading_animation()
os.system("clear")
os.system("sudo mv ./installer.sh /tmp/udev265sap/installer.sh ; sudo chmod +x /tmp/udev265sap/installer.sh ; bash /tmp/udev265sap/installer.sh")
time.sleep(1)
os.system("sudo rm -rf /tmp/udev265sap")
