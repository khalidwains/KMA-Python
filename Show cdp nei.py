from netmiko import ConnectHandler

# List of switches with their IP addresses
switches = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.0.200",
        "username": "admin",
        "password": "cisco",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.2",
        "username": "admin",
        "password": "cisco",
    },
    # Add more switches as needed
]

# Function to get CDP neighbors
def get_cdp_neighbors(device):
    try:
        connection = ConnectHandler(**device)
        output = connection.send_command("show cdp neighbors detail")
        connection.disconnect()
        return output
    except Exception as e:
        return f"Error connecting to {device['ip']}: {str(e)}"

# Main function to iterate over switches
def main():
    for switch in switches:
        print(f"CDP neighbors on {switch['ip']}:")
        cdp_output = get_cdp_neighbors(switch)
        print(cdp_output)

if __name__ == "__main__":
    main()
