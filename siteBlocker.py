import time
from datetime import datetime as dt

start_time = dt(dt.now().year, dt.now().month, dt.now().day,8)
end_time = dt(dt.now().year, dt.now().month, dt.now().day,16)

hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "xvideos.com"]

while True:
    if start_time < dt.now() < end_time:
        print ("Fun time")
        with open(hosts_path, 'r+') as file:
            content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")


    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
        print ("working hours")

    time.sleep(30)