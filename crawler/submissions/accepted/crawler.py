#!/usr/bin/env python3
import sys
from html.parser import HTMLParser

ok = set()
queue = ["/"]
tried = set("/")

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            for t, link in attrs:
                if t.lower() == "href":
                    if link not in tried:
                        tried.add(link)
                        queue.append(link)

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass

def parse_links(entity):
    parser = MyHTMLParser()
    parser.feed('\n'.join(entity))


OK = "HTTP/1.0 "

def read_response():
    statusmsg = sys.stdin.readline()
    headers = []
    msg = []
    inmsg = False
    while True:
        line = sys.stdin.readline()
        if line == F("\r\n"):
            if inmsg:
                break
            inmsg = True
        elif inmsg:
            msg.append(line)
        else:
            headers.append(line)
    return statusmsg, msg, headers

def F(p):
    # return p.replace("\r", "CRLF")
    return p

def handle_redirect(headers):
    for h in headers:
        if h[0:10] == "Location: ":
            p = h[10:].strip()
            if p not in tried:
                tried.add(p)
                queue.append(p)

while queue:
    p = queue[0]
    queue = queue[1:]
    request = F("GET " + p + " HTTP/1.0\r")
    print(F(request), flush=True)
    print(F("\r"), flush=True)
    sys.stdout.flush()

    status, entity, headers = read_response()
    if status[0:len(OK)] == OK:
        code = int(status[len(OK):len(OK)+3])
        if code == 503:
            queue.append(p)
        elif 300 <= code < 400:
            handle_redirect(headers)
        else:
            parse_links(entity)
            ok.add(p)

print(" ".join(sorted(list(ok))))
