import subprocess

from util.device_bluetooth_on_off import BTOnOFF

BT = BTOnOFF()
print(BT.check_bt_status())
BT.turn_bt_on()
print(BT.check_bt_status())

#subprocess.call('adb shell am start -a android.settings.BLUETOOTH_SETTINGS', stdout=subprocess.PIPE)

state = int(subprocess.check_output('adb shell settings get global bluetooth_on'))
print(type(state))
if state == 0:
    print("BT IS OFF")
else:
    print("BT IS ON")

output = subprocess.check_output('adb shell dumpsys bluetooth_manager')
print(output)