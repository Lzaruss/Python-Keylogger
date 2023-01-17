from cryptography.fernet import Fernet

class Decoder:
    def __init__(self, clave: bytes, mensaje: bytes):
        self.mensaje = mensaje
        self.object = Fernet(clave)
        self.mesageDecrypted = ''

    def decrypt(self) -> str:
        self.mesageDecrypted = self.object.decrypt(self.mensaje).decode('utf-8')
        return self.mesageDecrypted

    def showMesage(self):
        print(self.mesageDecrypted)

if __name__ == '__main__':
    d = Decoder(b'AfLD45zfo0rrfoMJV4Zp54kIED26SbwlOjvZQR1V2yo=', b'gAAAAABjxnq-94HQjWLAvt9Y8C6V0d48fD2K9CrE5kO3VqqO9GsVJ4yHWEO0oKWyOXfpbXSyhZKk1nHNXRYF6zde2n_AQOw9a6hyxAJmfj1C4r26LC9BgkU=').decrypt()
    print(d)