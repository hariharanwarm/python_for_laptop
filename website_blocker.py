import time
from datetime import datetime as dt

hosts_temp='/Users/hariharan/Desktop/pythons_apps/hosts'
redirect='127.0.0.1'
website=['https://www.linkedin.com','https://linkedin.com']

while True :
    if dt(dt.now().year,dt.now().month,dt.now().day,23,00)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,23,30):
        print("blocked hours")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for web in website:
                if web in content:
                    pass
                else:
                    file.write(redirect+" "+web+"\n")
    else:
        with open(hosts_temp,'r+')as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(web in line for web in website):
                    file.write(line)
            file.truncate()
        print("fun hrs")
    time.sleep(5)