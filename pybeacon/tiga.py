import time
import requests  # Import the requests library for HTTP requests

from beacontools import BeaconScanner, IBeaconFilter, IBeaconAdvertisement, BluetoothAddressType


def callback(bt_addr, rssi, packet, additional_info):
    """
    Callback function invoked when a beacon is detected.

    - Formats and prints the beacon data to the console.
    - Optionally sends an HTTP request with the beacon data (commented out).

    Args:
        bt_addr (str): Bluetooth address of the beacon.
        rssi (int): Received Signal Strength Indicator (RSSI) value.
        packet (IBeaconAdvertisement): Parsed beacon advertisement data.
        additional_info (dict): Additional information about the beacon.
    """

    print(f"Beacon detected: <{bt_addr}, {rssi}> {packet} {additional_info}")

    # Uncomment to send an HTTP request with the beacon data
    url = "http://192.168.0.117:3000/beacon/insert"
  # Replace with your server URL
    data = {
       "bt_addr": bt_addr,
       "rssi": rssi,
       "packet": str(packet),  # Convert packet to string for JSON
       "additional_info": additional_info,
    }
    try:
       response = requests.post(url, json=data)
       response.raise_for_status()  # Raise an exception for non-2xx responses
       print("HTTP request successful:", response.text)
    except requests.exceptions.RequestException as e:
       print(f"HTTP request error: {e}")


def main():
    try:
        while True:
            scanner = BeaconScanner(callback, scan_parameters={"address_type": BluetoothAddressType.PUBLIC})
            scanner.start()
            time.sleep(1)
            scanner.stop()  # Stop scanning to conserve resources

    except KeyboardInterrupt:
        print("Exiting...")
        scanner.stop()  # Ensure scanner is stopped on keyboard interrupt


if __name__ == "__main__":
    main()
