import sys, subprocess, os, socketserver, json

class MyTCPHandler(socketserver.BaseRequestHandler):
    root_path = os.environ.get('ROOT_PATH') if os.environ.get('ROOT_PATH') else b''

    def handle(self):
        data, out = self.request.recv(1024).split(b'\n'), {}
        r_path = self.root_path if type(self.root_path) == bytes else self.root_path.encode()

        if data:
            method, path, protocol = data.pop(0).split(b' ')
            if method == b'GET':
                if os.path.exists(r_path + path):
                    process_output = subprocess.run([
                        'find', r_path + path, '-type', 'f', '-exec', 'du', '-a', '{}', '+'
                    ], capture_output=True)
                    disk_usage = process_output.stdout.splitlines()

                    for file in disk_usage:
                        f_bytes, f_name = file.split('\t'.encode())
                        out[f_name.decode('utf-8')] = int(f_bytes)
        
        self.request.sendall(b'{ "files": ' + json.dumps(out).encode() + b'}')

if __name__ == '__main__':

    HOST = os.environ.get('HOST')
    if not HOST: 
        HOST = '0.0.0.0'

    PORT = os.environ.get('PORT')
    if not PORT: 
        PORT = 9999

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

