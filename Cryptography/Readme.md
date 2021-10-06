# Usage
### Get help
```sh
python3 crypt.py -h

usage: crypt.py [-h] [-f FILE] [-e] [-d]
optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  path to a file
  -e, --encrypt         encrypt file
  -d, --decrypt         decrypt file
```

### Encrypt a file
```sh
python3 crypt.py -e -f <filename.txt>
```

### Decrypt a file
```sh
python3 crypt.py -d -f <filename.txt>
```