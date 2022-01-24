import re

regular = re.compile(r'((?:\d+[.]){3}\d+).*\[(.+)\] "([A-Z]+).([^"]+)" (\d+) (\d+)')
reqest = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
print(regular.match(reqest).groups())
