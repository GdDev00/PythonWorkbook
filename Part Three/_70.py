

text = input("Inserisci il testo da criptare: ")
crypt_text = ''

for char in text:
    #controllo se il carattere è una lettera
    if(char.isalpha()):
        if(char.isupper()):
            #converto il carattere in numero ascii
            ascii_code = ord(char)
            #aumento di tre posizioni
            ascii_code + 3
            #converto il codice ascii in carattere
            crypt_text += chr(ascii_code)

