sudo apt update
sudo apt install python3 python3-pip python3-venv git docker.io docker-compose -y

# Install Node.js and npm for the frontend
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt install -y nodejs

# Install IPFS
wget https://dist.ipfs.io/go-ipfs/v0.8.0/go-ipfs_v0.8.0_linux-amd64.tar.gz
tar xvfz go-ipfs_v0.8.0_linux-amd64.tar.gz
cd go-ipfs
sudo bash install.sh
ipfs init
ipfs daemon &

# Clone the repository or copy your project files
git clone https://github.com/sainawj/real-estate-management.git
cd real-estate-management