import livereload
import os

if __name__ == '__main__':
    host = os.getenv('LR_HOST', '127.0.0.1')
    port = os.getenv('LR_PORT', 5500)
    server = livereload.Server()
    server.watch('source/', livereload.shell('make html'))
    server.serve(root='build/html', host=host, port=port)
