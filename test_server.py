#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        print "Headers:"
        print self.headers
        print
        print "Body:"
        content_len = int(self.headers.getheader('content-length'))
        body = self.rfile.read(content_len)
        print body
        self.send_response(200)

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('port', type=int)
    args = ap.parse_args()
    server = SocketServer.TCPServer(("", args.port), Handler)
    server.serve_forever()
