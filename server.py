import http.server
import socketserver

PORT = 8000  # Puoi cambiare questa porta se è già in uso

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server avviato su http://localhost:{PORT}")
    print("Premi Ctrl+C per fermare il server.")
    httpd.serve_forever()