from http.server import SimpleHTTPRequestHandler, HTTPServer
import logging

class MiManejador(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

    def log_message(self, format, *args):
        logging.info("%s - - [%s] %s" %
                     (self.client_address[0],
                      self.log_date_time_string(),
                      format % args))

def run(server_class=HTTPServer, handler_class=MiManejador, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.basicConfig(level=logging.INFO)
    logging.info(f'Servidor corriendo en http://localhost:{port}/')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Servidor detenido.')

if __name__ == "__main__":
    run()
