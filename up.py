#!/usr/bin/env python

import requests
import smtplib
from time import sleep

# Gmail login, users of two factor auth will need to generate an application specific password.

email = 'user@gmail.com'
password = 'password'

sites = ['http://google.com/', 'http://simplyluke.com/', 'http://rainforestpartnership.org/']
def send_mail(site):
    fromaddr = email
    toaddrs = email
    # \n is necessary to separate the message from the header
    msg = '\nYour script has reported that %s has gone offline. Good luck.' % site
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(email, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

# Infinite loop time.
while True:
    for site in sites:
        try:
            r = requests.get(site)
            if r.status_code == 200:
                pass
            else:
                raise Exception('spam')
        except:
            send_mail(site)

    # Wait 30 minutes
    sleep(1800)
