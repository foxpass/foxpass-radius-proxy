# foxpass-radius-proxy
Foxpass's RADIUS proxy. Allows standard RADIUS protocol to be used securely by proxying requests over HTTPS.

This proxy supports regular, plain, basic RADIUS only. No EAP.

All
===
Create a Radius Client (on this page: https://www.foxpass.com/settings/radclients/) from the proxy's *public* ip address. Note the shared secret.

Configure your endpoint to point to this server's IP address (usually the internal address) on pot 1812, using the shared secret from above.

Linux (Ubuntu)
=====

See if it runs (ctrl-c to stop)
```
python foxpass-radius-proxy.py
```

You might need to run `sudo pip install requests` first.

If that command also fails, you might need to do `sudo apt-get install python-pip` to get pip.

Once it starts up, install set it up to start automatically.

Upstart (Ubuntu before 17.10)
=====
```
sudo cp foxpass-radius-proxy.py /usr/local/bin
```

And then install the upstart script
```
sudo cp upstart/foxpass-radius-proxy.conf /etc/init
```

And then start it
```
sudo service foxpass-radius-proxy start
```

If you get errors, look in `/var/log/syslog` and `/var/log/upstart/foxpass-radius-proxy.log`

Docker
=====

The proxy can be easily deployed as a container.

```shell
docker build -t foxpass-radius-proxy .
docker run --net host foxpass-radius-proxy
```

SysV
=====

Script installation
------------
Install the start script
```
sudo cp sysv/foxpass-radius-proxy /etc/init.d/foxpass-radius-proxy
```

Script usage
------------

### Start ###

Starts the app.

    /etc/init.d/foxpass-radius-proxy start

### Stop ###

Stops the app.

    /etc/init.d/foxpass-radius-proxy stop

### Restart ###

Restarts the app.

    /etc/init.d/foxpass-radius-proxy restart

### Status ###

Tells you whether the app is running. Exits with _0_ if it is and _1_
otherwise.

    /etc/init.d/foxpass-radius-proxy status

Systemd (Ubuntu 17.10 and onwards)
=====

Script installation
------------
Install the control script
```
sudo cp systemd/foxpass-radius-proxy.service /lib/systemd/system/
sudo systemctl enable foxpass-radius-proxy.service
```

Script usage
------------

### Start ###

Starts the app.

      sudo systemctl start foxpass-radius-proxy

### Stop ###

Stops the app.

      sudo systemctl stop foxpass-radius-proxy

### Restart ###

Restarts the app.

      sudo systemctl restart foxpass-radius-proxy

### Status ###

Tells you some statistics about the process and its current state.

      sudo systemctl status foxpass-radius-proxy

### Logs ###

Messaging handled by journald; access the output using journal

      journalctl -u foxpass-radius-proxy.service
