#!/usr/bin/python3
""" make post request with email with specied url """
if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys

    post = {"email": sys.argv[2]}
    url = sys.argv[1]
    data = urllib.parse.urlencode(post)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
