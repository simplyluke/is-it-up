# is-it-up

#### A simple python script to alert you via email if a website goes offline.

Is it up will run in the background and check to see if your websites are online every 30 minutes.

### [Dependencies](http://xkcd.com/754/)

* Requests

### Running up.py

1. Fill in the email and password variables with your gmail credentials. (Note: If you use two-factor auth for google you will need an application specific password)

2. Add the sites you would like to monitor to the sites list.

3. Copy the script into init.d and set it to run on launch.

`sudo mv up.py /etc/init.d/`

`sudo +x /etc/init.d/up.py` 

`sudo update-rc.d up.py defaults`
