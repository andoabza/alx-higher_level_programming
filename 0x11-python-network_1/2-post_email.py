#!/usr/bin/python3
""" make post request with email with specied url """
if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys

    post = {"email": sys.argv[2]}
    url = sys.argv[1]
    data = urllib.parse.urlencode(post)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as resp:
        the_page = resp.read()
        print("Your email is: {}".format(sys.argv[2]))
