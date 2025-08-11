# Caesar Cipher - Menu Version

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result


def main():
    while True:
        print("\n=== Caesar Cipher Menu ===")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value: "))
            encrypted = caesar_cipher(message, shift)
            print(f"Encrypted Message: {encrypted}")
        
        elif choice == "2":
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value: "))
            decrypted = caesar_cipher(message, -shift)
            print(f"Decrypted Message: {decrypted}")
        
        elif choice == "3":
            print("Exiting program... Sayonara!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

#Written by AG

if __name__ == "__main__":
    main()