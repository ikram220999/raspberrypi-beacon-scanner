from bleak import BleakClient
from beacontools import BeaconParser

def is_beacon(data):
  """Checks for advertising data patterns of iBeacon or Eddystone beacons."""
  return BeaconParser.detect_format(data) is not None

async def scan_for_beacons():
  print("Scanning for Bluetooth beacons...")
  async def callback(client, data, rssi):
    # Filter for beacon data
    if is_beacon(data):
      # Parse beacon data using BeaconTools
      beacon = BeaconParser.parse_from(data)
      print(f"Beacon found (RSSI: {rssi}):")
      print(f"  Type: {beacon.beacontype}")
      print(f"  UUID: {beacon.uuid}")
      if beacon.beacontype == 'iBeacon':
          print(f"  Major: {beacon.major}")
          print(f"  Minor: {beacon.minor}")
      # Add logic for Eddystone beacon data parsing if needed

  async with BleakClient("public", disconnected_callback=callback) as client:
    print("Scanning...")
    await client.start_notify(characteristic)  # Replace with characteristic for beacon data

if __name__ == "__main__":
  # Replace with the actual address of the beacon if known (optional)
  characteristic = "0x0000"  # Placeholder, replace with characteristic for beacon data notification
  scan_for_beacons()
