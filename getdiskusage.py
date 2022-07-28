import sys, os, subprocess

def getdiskusage(path):
    root_path = os.environ.get('ROOT_PATH') if os.environ.get('ROOT_PATH') else '/'
    response = dict(files=[])

    if os.path.exists(root_path + path):
        process_output = subprocess.run([
            'find', root_path + path, '-type', 'f', '-exec', 'du', '-a', '{}', '+'
        ], capture_output=True)

        disk_usage = process_output.stdout.splitlines()

        for file in disk_usage:
            f_bytes, f_name = file.split('\t'.encode())
            file_object = { f_name.decode() : int(f_bytes) }
            response['files'].append(file_object)

    return response

if __name__ == '__main__':
    from pprint import pprint

    if len(sys.argv) != 2:
        raise ValueError('Please provide a single path argument')
    else:
        pprint(getdiskusage(sys.argv[1]))
