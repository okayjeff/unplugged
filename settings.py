# Python has 3 libraries for making http requests. Others may wrap these libs,
# but the following patch targets are the core behavior that results in an
# outbound HTTP connection.
PATCH_TARGETS = (
    'urllib.request.OpenerDirector._open',                # urllib
    'urllib3.connectionpool.HTTPConnectionPool.urlopen',  # urllib3
    'http.client.HTTPConnection._send_request'            # http.client
)
