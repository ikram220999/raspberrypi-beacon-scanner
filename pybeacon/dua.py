import time

from beacontools import BeaconScanner, IBeaconFilter, IBeaconAdvertisement, BluetoothAddressType

def callback(bt_addr, rssi, packet, additional_info):
    print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))

# scan for all iBeacon advertisements from beacons with certain properties:
# - uuid
# - major
# - minor
# at least one must be specified.
while True:

	scanner = BeaconScanner(callback,
	    scan_parameters={"address_type": BluetoothAddressType.PUBLIC}
	)
	scanner.start()
	time.sleep(5)
	scanner.stop()
