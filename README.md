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

Once it starts up, install it
```
sudo mv foxpass-radius-proxy.py /usr/local/bin
```

And then install the upstart script
```
sudo mv upstart/foxpass-radius-proxy.conf /etc/init
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
