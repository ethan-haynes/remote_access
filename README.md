# Summary
Remote Access is a runnable socket server inside a Docker container. It is a toolset used to expose limited information to developers who do not have ssh access to the VM/server it is running on. It consumes a mount point provided in a GET request uri and returns a json object containing file names and their disk usage in bytes. The module for getting disk usage can also be run as a standalone script, or as a part of an API. 

## HOW TO TEST PYTHON MODULE
```sh
  $ export ROOT_PATH="$(dirname `pwd`)/"
  $ python3 getdiskusage.py remote_access
    {'files': [{'/root/user/remote_access/requirements.txt': 8},
               {'/root/user/remote_access/Dockerfile': 8},
               {'/root/user/remote_access/getdiskusage.py': 8},
               {'/root/user/remote_access/README.md': 8},
               {'/root/user/remote_access/.gitignore': 8},
               {'/root/user/remote_access/app.py': 8}]
    }
```

## HOW TO TEST APP SERVER
```sh
  $ export ROOT_PATH="$(dirname `pwd`)/"
  $ flask run --host=0.0.0.0 
  $ curl http://localhost:5000/remote_access
    {'files': [{'/root/user/remote_access/requirements.txt': 8},
               {'/root/user/remote_access/Dockerfile': 8},
               {'/root/user/remote_access/getdiskusage.py': 8},
               {'/root/user/remote_access/README.md': 8},
               {'/root/user/remote_access/.gitignore': 8},
               {'/root/user/remote_access/app.py': 8}]
    }
```

## HOW TO RUN API IN DOCKER
```sh
  $ docker build . -t remote_access/getdisk 
  $ docker run --rm -d -p 5000:5000 --read-only=true --tmpfs /run --tmpfs /tmp -v "$(pwd)":/app:ro remote_access/getdisk:latest
```

## HOW TO TEST API IN DOCKER

### Request
```sh
  $ curl http://localhost:5000/diskusage/app
```
### Response
```sh
  {
    'files': [{'/app/Dockerfile': 4},
              {'/app/getdiskusage.py': 4},
              {/app/README.md': 4},
              ...
              ]
    }
  }
```

## Production Setup
```sh
  $ docker build . -t remote_access/getdisk
  $ docker run -d \
--name=remote_access \
-p 5000:5000 \
--read-only=true \
--tmpfs /run \
--tmpfs /tmp \
-e ROOT_PATH=/host \
-v /:/host:ro \
remote_access/getdisk:latest
```

## Requirements
### Supported architectures:
amd64, arm32v5, arm32v6, arm32v7, arm64v8, i386, ppc64le, s390x, windows-amd64

### Supported Docker versions:
the latest release (down to 1.6 on a best-effort basis)
