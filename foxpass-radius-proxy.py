from __future__ import print_function

# Copyright (c) 2015-present, Foxpass, Inc.
# All rights reserved.
#
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import requests
import socket
import traceback

os.environ.setdefault('LISTEN_PORT', 1812)
os.environ.setdefault('SERVER', 'https://api.foxpass.com')

LISTEN_PORT = int(os.environ.get('LISTEN_PORT'))
SERVER = os.environ.get('SERVER')

def run_proxy_server(port):
    # create socket & establish verification url
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    url = '{}/radius/auth/'.format(SERVER)

    # start listening
    sock.bind(('0.0.0.0', port))

    print('Listening on port {}'.format(port))

    while True:
        # read data
        raw_data, address = sock.recvfrom(1024)
        print('received {} bytes from {}'.format(len(raw_data), address))

        try:
            # pass data over to server
            resp = requests.post(url, data=raw_data)

            if resp.status_code != 200:
                print('error {}: {}'.format(resp.status_code, resp.text))
                continue

            sock.sendto(resp.content, address)
            print('sent {} bytes to {}'.format(len(resp.content), address))
        except Exception:
            traceback.print_exc()


if __name__ == '__main__':
    run_proxy_server(LISTEN_PORT)
