import os
from http.server import HTTPServer, BaseHTTPRequestHandler

from urllib.parse import urlparse, parse_qsl

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # print("GET Request")
        # insert relevant code

        parsed = urlparse(self.path)

        # Check for content.html
        if parsed.path in ['/content.html']:
            # retrieve HTML file

            fp = open('.'+self.path)
            content = fp.read()

            # generate headers
            self.send_response(200) # OK
            self.send_header("Content-type", "text/html")
            self.send_header("Content-length", len(content))
            self.end_headers()

            # Send to browser
            self.wfile.write(bytes(content, "utf-8"))
            fp.close()

        elif parsed.path.__contains__('.png'):
            # retrieve image
            filename = parsed.path[1:]
            if os.path.exists(filename):
                with open(filename, 'rb') as fp:
                    content = fp.read()
                self.send_response(200) #OK
                self.send_header("Content-type", "image/png")
                self.send_header("Content-length", len(content))
                self.end_headers()

                # send to browser
                self.wfile.write(bytes(content))

        elif parsed.path.__contains__('.jpg') or parsed.path.__contains__('.jpeg'):
            # retrieve image
            filename = parsed.path[1:]
            if os.path.exists(filename):
                with open(filename, 'rb') as fp:
                    content = fp.read()
                self.send_response(200) # OK
                self.send_header("Content-type", "image/jpeg")
                self.send_header("Content-length", len(content))
                self.end_headers()

                # Send to browser
                self.wfile.write(bytes(content))

        elif parsed.path.__contains__('.mp4'):
            # retrieve video
            filename = parsed.path[1:]
            if os.path.exists(filename):
                with open(filename, 'rb') as fp:
                    content = fp.read()
                self.send_response(200) # OK
                self.send_header("Content-type", "video/mp4")
                self.send_header("Content-length", len(content))
                self.end_headers()

                # Send to browser
                self.wfile.write(bytes(content))

        else:
            # generate 404 for GET requests that aren't the 3 files above
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes("404: %s not found" % self.path, "utf-8"))


    def do_POST(self):
        print("POST Request")
        # insert relevant code

if __name__ == "__main__":
    httpd = HTTPServer(('localhost', 5000), MyHandler)
    print("Server listing in port: ", 5000)
    httpd.serve_forever()