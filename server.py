#!/usr/bin/python

from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer
import urlparse
import sqlite3test

#Server PORT
PORT = 8020
#DB ( + name)
db = sqlite3test.sqlitedb("test.db")

class Server(SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.set_response(200)
        self.set_header('Content-type', 'type/html')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):

        """Respond to a POST request."""

        # Extract and print the contents of the POST
        length = int(self.headers['Content-Length'])
        post_data = urlparse.parse_qs(self.rfile.read(length).decode('utf-8'))
        print "INCOMING POST"
        post = {}
        for key, value in post_data.iteritems():
            post[str(key)] = str(value[0])
            print "Key -> {0} = {1}".format(key, value[0])
        print str(post['extension']).split(",")
        extension = str(post['extension']).split(",")
        callerID = post['callerId']
        if len(extension) == 3:
            db.add_to_queue(callerID, str(extension[0]), str(extension[1]), str(extension[2]))
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        self.wfile.write("{\"recognized\":\"true\"}")

Handler = Server

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "Starting Server on port: ", PORT

httpd.serve_forever()
