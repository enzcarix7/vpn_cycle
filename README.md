### VPN/IP Rotation

This Python script automatically cycles through different VPN configurations stored in .ovpn files, connects to them for a specified time, and then disconnects. It also checks your public IP address after each connection to confirm that the VPN is working.

### Requirements
```
• Python 3.x
• The requests library (for getting public IP)
• OpenVPN installed on your machine
• A folder with .ovpn files for different VPN servers
• Sudo privileges for starting OpenVPN via sudo (Linux/MacOS)
```

### Installation
1. Clone this repository or download the script to your local machine.
2. Install required Python libraries:
You will need the requests library to interact with the public IP API.

Run:

```
pip install requests
```

3. Set up your VPN credentials:
```
• Modify the script to input your VPN credentials (USER, PASSWORD, and sudo_password).
• Replace folder_path = "PATH/FILE" with the actual path to your folder containing .ovpn files.
```

5. Make sure OpenVPN is installed:
The script uses OpenVPN to connect to VPN servers, so make sure OpenVPN is installed on your system. You can install it using:

• For Linux (Ubuntu/Debian):
```
sudo apt-get install openvpn
```
• For macOS:
```
brew install openvpn
```
• For Windows, download and install here:
```
https://openvpn.net/community-downloads/
```

### How It Works
1. Cycle Through VPN Configurations: The script looks for .ovpn files in the specified folder, picks one at random, and starts the VPN connection using OpenVPN.
2. Check Public IP: After connecting to the VPN, it retrieves your public IP address using the api.ipify.org service to confirm the VPN connection is active.
3. Disconnect: It disconnects the VPN after 15 seconds and waits 1 second before switching to the next VPN configuration.

### Usage
1. Open the script in any text editor and modify the following fields:
folder_path: Path to your folder with .ovpn files.
user, password, and sudo_password: Your VPN credentials and sudo password.
2. Run the script:
```
python ipxvpn_rotation.py
```
The script will cycle through your .ovpn files, connect to the VPN, check the public IP address, and disconnect every 15 seconds.

### Notes
```
• Sudo Permissions: The script uses sudo to execute OpenVPN commands. Make sure you have appropriate permissions or you may need to adjust the script to work without sudo depending on your environment.
• Security: Do not store sensitive credentials (e.g., passwords) in the script in plain text in production environments. Consider using environment variables or secure vaults to manage them.
• OpenVPN: Ensure OpenVPN is running on your system and properly configured.
```
