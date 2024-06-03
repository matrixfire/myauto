import shelve
import os
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

# Determine the directory of the script
script_dir = os.path.dirname(__file__)
# Set the directory for the database and HTML files
data_dir = os.path.join(script_dir, 'mcb')
html_file = os.path.join(data_dir, 'index.html')

# Function to generate HTML file
def generate_html(shelve_filename):
    with shelve.open(shelve_filename) as my_shelf:
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Clipboard Manager</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                table { width: 100%; border-collapse: collapse; }
                th, td { border: 1px solid #ddd; padding: 8px; }
                th { background-color: #f2f2f2; }
                input[type="text"] { width: 90%; padding: 6px; }
                button { padding: 10px 15px; margin: 5px; }
            </style>
        </head>
        <body>
            <h1>Clipboard Manager</h1>
            <form method="POST" action="/update">
                <table>
                    <thead>
                        <tr>
                            <th>Key</th>
                            <th>Value</th>
                        </tr>
                    </thead>
                    <tbody>
        """

        for key in my_shelf:
            value = my_shelf[key]
            html_content += f"""
            <tr>
                <td><input type="text" name="key_{key}" value="{key}" readonly></td>
                <td><input type="text" name="value_{key}" value="{value}"></td>
            </tr>
            """

        html_content += """
                    </tbody>
                </table>
                <button type="submit">Submit Changes</button>
            </form>
        </body>
        </html>
        """

        with open(html_file, 'w') as file:
            file.write(html_content)

# Function to start the HTTP server
def start_server():
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                with open(html_file, 'r') as file:
                    self.wfile.write(file.read().encode('utf-8'))
            else:
                self.send_error(404, "File not found.")

        def do_POST(self):
            if self.path == '/update':
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                parsed_data = urllib.parse.parse_qs(post_data.decode('utf-8'))
                with shelve.open(shelve_filename) as my_shelf:
                    for key in parsed_data:
                        if key.startswith("value_"):
                            original_key = key[6:]
                            my_shelf[original_key] = parsed_data[key][0]

                self.send_response(302)
                self.send_header('Location', '/')
                self.end_headers()

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Serving on port 8000...")
    webbrowser.open('http://localhost:8000')
    httpd.serve_forever()

# Function to create and open the HTML page
def create_and_open_html(shelve_filename):
    generate_html(shelve_filename)
    start_server()

if __name__ == "__main__":
    create_and_open_html(os.path.join(data_dir, 'mcb'))
