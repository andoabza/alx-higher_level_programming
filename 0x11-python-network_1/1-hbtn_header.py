#!/usr/bin/python3
""" a script that takes url then display value of X-Request_Id """
if __name__ == "__main__":
    import sys
    import urllib.request
    var = sys.argv[1]
    with urllib.request.urlopen(var) as response:
        html = response.getheader("X-Request-Id")
        print(html)
