import win10toast
import time

toast = win10toast.ToastNotifier()
toast.show_toast(title="All Ok Bro",  msg="By ...", duration=3)

time.sleep(2)

toast.show_toast(title="Wait Please",  msg="By ...", duration=3)