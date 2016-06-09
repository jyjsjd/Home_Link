# -*- coding: utf-8 -*-

import base64


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://proxy.com:port'
        proxy_user_pass = "username:password"
        encoded_user_pass = base64.encodestring(proxy_user_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
