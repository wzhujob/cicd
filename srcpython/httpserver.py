#https://dev.to/kihuni/building-a-simple-web-application-with-python-33cd

from http.server import BaseHTTPRequestHandler, HTTPServer

# Define the HTTP request handler class
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Read the HTML content from the file
        #with open('index.html', 'rb') as file:
        #    html_content = file.read()
        html_content = "<html><body><h1>Welcome to the Simple Python Web Server</h1></body></html>"
        html_bytes = bytes(html_content, "utf-8")
        # Set the response body with the HTML content
        self.wfile.write(html_bytes)

# Define the main function to start the server
def main():
    # Set the server address and port
    server_address = ('', 8080)

    # Create an instance of the HTTP server
    httpd = HTTPServer(server_address, MyRequestHandler)

    # Start the server
    print('Starting server...')
    httpd.serve_forever()

if __name__ == '__main__':
    main()
