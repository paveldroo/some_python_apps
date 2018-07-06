import time
from datetime import datetime as dt
hosts_path = "~/Google\ Drive/Programming/learning/udemy/site_blocker/hosts"
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com', 'www.reddit.com']
now = dt.now()


while True:
    if 10 <= now.hour <= 19:
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    file.write('{} {}\n'.format(redirect, site))
                    print('Added blocking sites')

    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)


