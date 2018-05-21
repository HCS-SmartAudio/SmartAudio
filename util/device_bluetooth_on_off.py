"""
Class for BT handler
"""
import subprocess


class BTOnOFF:

    def check_bt_status(self):
        """
        Check BT status
        :return:
        """
        try:
            state = int(subprocess.check_output('adb shell settings get global bluetooth_on'))
            if state == 0:
                return False
            else:
                return True
        except:
            print("no devices/emulators found")

    def turn_bt_on(self):
        """
        Turns BT ON
        :return:
        """
        self.__turn_bt()

    def turn_bt_off(self):
        """
        Turns BT OFF
        :return:
        """
        self.__turn_bt()

    @staticmethod
    def __turn_bt():
        """
        Turns BT ON / OFF
        :return:
        """
        subprocess.call('adb shell am start -a android.settings.BLUETOOTH_SETTINGS')
        subprocess.call('adb shell input tap 960 350')
        subprocess.call('adb shell input keyevent 3')