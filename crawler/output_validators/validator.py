#!/usr/bin/env python3

import sys

def A(s):
    return s.encode('UTF-8')

def M(s):
    w = b''
    for k in s:
        w += k
    return w

def P(s):
    parts = s.strip().split(" ")
    for p in parts:
        if p[0] == '"' and p[-1] == '"':
            return p[1:-1]

def PRINT(x):
    sys.stdout.buffer.write(x.encode('ASCII'))

def not_found():
    PRINT(P("HTTP/1.0 404 Not Found\r\n"))
    PRINT(P("\r\n"))
    PRINT(P("\r\n"))
    sys.stdout.flush()

def ok(content, status):
    PRINT(P("HTTP/1.0 " + status + " OK\r\n"))
    PRINT(P("\r\n"))
    sys.stdout.buffer.write(content)
    PRINT(P("\r\n"))
    sys.stdout.flush()

def tempfail(content):
    first = [True]
    def p(headers):
        if first[0]:
            ok(b"", "503")
            first[0] = False
        else:
            ok(content, "200")
    return p

def Status(s):
    parts = s.strip().split(" ")
    for p in parts:
        if p[0:7] == 'status:':
            return p[7:]
    return "200"

def redir(s):
    parts = s.strip().split(" ")
    for p in parts:
        if p[0:6] == 'redir:':
            return p[6:]
    return None

def doredir(how):
    status, path = how.split(":")
    PRINT(P("HTTP/1.0 " + status + " OK\r\n"))
    PRINT(P("Location: " + path + "\r\n"))
    PRINT(P("\r\n"))
    PRINT(P("\r\n"))
    sys.stdout.flush()

def parse_input(lines):
    handlers = {}
    for i in range(len(lines)):
        if lines[i].startswith(A(">BEGIN")):
            end = i
            while not lines[end].startswith(A(">END")):
                end += 1
            metadata = lines[i]
            metadata = metadata.decode('UTF-8')
            content = M(lines[i + 1:end])
            path = P(metadata)
            status = Status(metadata)
            red = redir(metadata)
            if red:
                handlers[path] = lambda x,red=red: doredir(red)
            elif status == "503":
                handlers[path] = tempfail(content)
            else:
                handlers[path] = lambda x,content=content: ok(content, status)
    return handlers

inp = sys.argv[1]
ans = sys.argv[2]
feedback = sys.argv[3]

with open(inp, 'rb') as f:
    handlers = parse_input(f.readlines())

def handle_request(request):
    global handlers
    initial = request[0]
    if not initial.startswith('GET ') or not initial.endswith(' HTTP/1.0\r\n'):
        die()
    path = initial[4:-11]
    if path in handlers:
        handlers[path](request[1:])
    else:
        not_found()

def F(s):
    # return s.replace('CRLF', '\r')
    return s

def P(s):
    # return s.replace('\r', 'CRLF')
    return s

def check_answer(s):
    l = ' '.join(list(sorted(s.strip().split(" "))))
    with open(ans) as f:
        expected = f.read().strip()
        if l == expected:
            sys.exit(42)
    sys.exit(43)

def die():
    sys.exit(43)

while True:
    try:
        first = F(sys.stdin.readline())
    except:
        die()
    if len(first) == 0:
        die()
    if len(first) >= 3 and first[0:3] == "GET":
        request = [first]
        while True:
            try:
                line = F(sys.stdin.readline())
            except:
                die()
            if line == "\r\n":
                handle_request(request)
                break
        continue
    # assume answer
    check_answer(first)
