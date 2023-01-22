from cryptography.fernet import Fernet

class Decoder:
    def __init__(self, mensaje: bytes = None, key: bytes = None, file = None):
        if not (file):
            self.mensaje = mensaje
            try:
                self.object = Fernet(key)
            except:
                raise Exception("Please make sure that you have put the key in the arguments")
        else:
            with open(file, "r") as f:
                text = f.readlines()
            try:
                self.object = Fernet(text[1].encode('utf-8'))
                self.mensaje = text[2]
            except:
                raise Exception("Please make sure that you have put the right file in the arguments")

    def decrypt(self) -> str:
        try:
            return self.object.decrypt(self.mensaje).decode('utf-8')
        except:
            raise Exception("Please make sure that you have put the message in the arguments")

if __name__ == '__main__':
    print(Decoder(file="log.txt").decrypt())