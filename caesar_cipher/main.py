running = True

def encrypt(message, key):
    result = []
    for ch in message:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shifted = (ord(ch) - base + key) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(ch)   
    return ''.join(result)

def decrypt(message, key):
    return encrypt(message, 26 - (key % 26))


def main():
    while running:
        choice = input("Press (e) for encryption and (d) for decryption, (q) to quit: ").strip().lower()
        if choice == "e":
            key = int(input("Enter the key (0-25): "))
            message = input("Enter the text you want to encrypt: ")
            print(encrypt(message, key))
        elif choice == "d":
            key = int(input("Enter the key (0-25): "))
            message = input("Enter the text you want to decrypt: ")
            print(decrypt(message, key))
        elif choice == "q": 
            print("Thanks for using the program!")
            break
        else: 
            print("Invalid Input please enter (e) or (d)")
            

if __name__ == "__main__":
    main()