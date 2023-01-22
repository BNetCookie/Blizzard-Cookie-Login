from winproxy import ProxySetting
from mitmproxy import http
import os

cookie = input("Enter Battle.net Cookie: ")

p = ProxySetting()

p.server = dict(http='127.0.0.1:8080', https='127.0.0.1:8080')
p.enable = True
p.registry_write()

print("Open Battle.net Client")

def response(flow: http.HTTPFlow):
    if 'account.battle.net/login/en/login.app?app=app' in flow.request.url and flow.request.method == 'GET':
        flow.response.headers["location"] = f'http://localhost:0/?ST={cookie}'
        flow.response.status_code = 302
    elif 'oauth.battle.net/oauth/authorize' in flow.request.url:
        p.enable = False
        p.registry_write()
        print("Logged into account.")
        os._exit(0)