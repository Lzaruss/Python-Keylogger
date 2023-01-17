from cryptography.fernet import Fernet

class Decoder:
    def __init__(self, mensaje: bytes = None, clave: bytes = None, file = None):
        if not (file):
            self.mensaje = mensaje
            self.object = Fernet(clave)
            self.mesageDecrypted = ''
        else:
            with open(file, "r") as f:
                text = f.readlines()
            
            self.object = Fernet(text[1].encode('utf-8'))
            self.mensaje = text[2]

    def decrypt(self) -> str:
        self.mesageDecrypted = self.object.decrypt(self.mensaje).decode('utf-8')
        return self.mesageDecrypted

    def showMesage(self):
        print(self.mesageDecrypted)

if __name__ == '__main__':
    #d = Decoder(b'gAAAAABjxnq-94HQjWLAvt9Y8C6V0d48fD2K9CrE5kO3VqqO9GsVJ4yHWEO0oKWyOXfpbXSyhZKk1nHNXRYF6zde2n_AQOw9a6hyxAJmfj1C4r26LC9BgkU=', b'AfLD45zfo0rrfoMJV4Zp54kIED26SbwlOjvZQR1V2yo=').decrypt()
    d = Decoder(file='log.txt').decrypt()
    print(d)
