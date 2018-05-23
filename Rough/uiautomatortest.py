import uiautomator2 as u2

d = u2.connect("52e6e977")
print(d.device_info)
print(d.window_size())
d(className="android.widget.Switch", text="OFF").click()



# from uiautomator import Device
#
# d = Device("52e6e977")
# d.press.back()
# bt_btn = d(className="android.widget.Switch")
# bt_btn.click()

#d.dump(filename='screen.xml')
#d(text='ON').exists()
#d.screen.on()
#d(className="android.widget.Switch", text="OFF").click()

