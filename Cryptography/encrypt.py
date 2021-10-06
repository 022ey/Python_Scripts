'''Code to encrypt a file and then decrypt it using a key.'''

from cryptography.fernet import Fernet
import argparse, os



def write_key(key):
    with open("keyfile.key", "wb") as file:
        file.write(key)


def load_key():
    with open("keyfile.key", "rb") as file:
        return file.read()

def encrypt_file(filename, key):
    f = Fernet(key)
    encrypted = b''
    with open(filename, "rb") as file:
        data = file.read()
        encrypted = f.encrypt(data)

    with open(filename, "wb") as file:
        file.write(encrypted)
    
    print("[+] Succesfully encrypted the file!")

def decrypt_file(filename, key):
    f = Fernet(key)
    encrypted_data = b''

    with open(filename, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    
    print("[+] Succesfully decrypted data!")

if __name__ == "__main__":

    #parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=argparse.FileType('r'), help="path to a file")
    parser.add_argument('-e', '--encrypt', action='store_true', help="encrypt file")
    parser.add_argument('-d', '--decrypt', action='store_true', help="decrypt file")
    args = parser.parse_args()




    if os.path.exists("keyfile.key"):
        #loading key from the keyfilefile
        key = load_key()
    else:
        key = Fernet.generate_key()
        #writing key to a file
        write_key(key)



    if(args.encrypt):
        #encrypting data
        encrypt_file(args.file.name, key)
    elif(args.decrypt):
        #decrypting data
        decrypt_file(args.file.name, key)
