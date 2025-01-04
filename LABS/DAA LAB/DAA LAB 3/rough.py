sudo apt update
sudo apt install wget gpg
wget https://go.microsoft.com/fwlink/?LinkID=760868 -O vscode.deb
sudo dpkg -i vscode.deb
sudo apt-get install -f
code
