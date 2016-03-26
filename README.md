# foxpass-radius-proxy
Foxpass's RADIUS proxy. Allows standard RADIUS protocol to be used securely by proxying requests over HTTPS.

This proxy supports regular, plain, basic RADIUS only. No EAP.

Linux (Ubuntu)
=====

Run `python proxy.py`

You might need to run `sudo pip install requests` first.

If that command fails, you might need to do `sudo apt-get install python-pip` to get pip.

Point your RADIUS clients at this, instead of at our RADIUS servers. Use the shared secret that's already set up in Foxpass (on this page: https://www.foxpass.com/settings/radclients/) for your company's IP address.

Docker
=====

The proxy can be easily deployed as a container.

```shell
docker build -t foxpass-radius-proxy .
docker run --net host foxpass-radius-proxy
```
