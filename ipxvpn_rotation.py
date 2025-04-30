import os
import time
import subprocess
import random
import tempfile
from requests import get 


# Path to the folder with .ovpn files
folder_path = "PATH/FILE"

# VPN credentials
user = "USER"
password = "PASSWORD"
sudo_password = "SUDO_PASSWORD"  # Enter your sudo password here


# # Function to get the public IP address using an external service.
def get_public_ip():
    try:
        response = get("https://api.ipify.org?format=json", timeout=5)
        response.raise_for_status()  # Check if the request was successful
        ip = response.json().get("ip")
        print(f"🌍 New public IP: {ip}")
        return ip
    except Exception as e:
        print(f"❌ Error retrieving public IP: {e}")
    return None


# # Function to start the VPN connection using a .ovpn file.
def connect_vpn(config_file):
    try:
        # Create a temporary file for credentials
        with tempfile.NamedTemporaryFile(delete=False) as cred_file:
            cred_file.write(f"{user}\n{password}".encode())
            cred_file.close()  # Close the temporary file

            # Build the OpenVPN command with hidden output
            command = f"echo {sudo_password} | sudo -S openvpn --config {config_file} --auth-user-pass {cred_file.name} --auth-nocache > /dev/null 2>&1 &"
            subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            print(f"🔗 Connected with {config_file}")

            # Wait a few seconds to ensure the connection is established
            time.sleep(3)

            # Get and print the public IP address after connecting
            get_public_ip()

    except subprocess.CalledProcessError as e:
        print(f"❌ Error in VPN connection: {e}")
    finally:
        # Remove the temporary credentials file
        if os.path.exists(cred_file.name):
            os.remove(cred_file.name)
            print("🔒 Removed the temporary credentials file")


# # Function to disconnect the VPN.
def disconnect_vpn():
    try:
        subprocess.run(['sudo', 'pkill', 'openvpn'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("🔌 VPN disconnected.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error disconnecting the VPN: {e}")


# # Function to get a list of .ovpn files from the folder.
def get_ovpn_files(folder):
    return [f for f in os.listdir(folder) if f.endswith('.ovpn')]


# # Function to cycle through .ovpn files and switch connections every 15 seconds.
def vpn_cycle():
    while True:
        ovpn_files = get_ovpn_files(folder_path)
        if not ovpn_files:
            print("⚠️ No .ovpn files found in the folder.")
            break

        # Choose a random .ovpn file
        config_file = os.path.join(folder_path, random.choice(ovpn_files))

        # Connect to the VPN
        connect_vpn(config_file)

        # Wait 15 seconds
        time.sleep(15)

        # Disconnect from the VPN
        disconnect_vpn()

        # Wait a little before changing the file
        time.sleep(1)


# # Main program execution
if __name__ == "__main__":
    vpn_cycle()
