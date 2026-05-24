import sys
import argparse
import math
from collections import Counter

# Custom cipher mapping (original mapping from Amit's code)
CIPHER_MAP = {
    'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9',
    'j': '!', 'k': '@', 'l': '#', 'm': '$', 'n': '%', 'o': '^', 'p': '&', 'q': '*', 'r': '(', 's': ')',
    't': '_', 'u': '-', 'v': '+', 'w': '=', 'x': '~', 'y': '{', 'z': '}'
}
# Reverse map for decryption
REVERSE_MAP = {v: k for k, v in CIPHER_MAP.items()}

# ANSI Colors for terminal UI styling
GREEN = "\033[1;32m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

def calculate_entropy(text):
    """Calculates Shannon Entropy of a string to measure randomness/cryptographic strength."""
    if not text:
        return 0.0
    counter = Counter(text)
    length = len(text)
    entropy = -sum((count / length) * math.log2(count / length) for count in counter.values())
    return round(entropy, 3)

def get_entropy_rating(entropy):
    """Returns a security strength rating based on entropy bits/char."""
    if entropy < 3.0:
        return RED + "WEAK (Highly Predictable)" + RESET
    elif entropy < 4.5:
        return YELLOW + "MODERATE (Basic Obfuscation)" + RESET
    else:
        return GREEN + "STRONG (High Randomness/Good Diffusion)" + RESET

def show_entropy_analysis(plain, cipher):
    """Prints a beautiful Shannon Entropy analysis comparison."""
    entropy_plain = calculate_entropy(plain)
    entropy_cipher = calculate_entropy(cipher)
    percentage_change = 0.0
    if entropy_plain > 0:
        percentage_change = round(((entropy_cipher - entropy_plain) / entropy_plain) * 100, 1)
    
    print(CYAN + "\n  [>] Shannon Entropy & Cryptographic Analysis:" + RESET)
    print(f"      - Plaintext Entropy  : {entropy_plain} bits/char")
    print(f"      - Ciphertext Entropy : {entropy_cipher} bits/char")
    sign = "+" if percentage_change >= 0 else ""
    print(f"      - Complexity Change  : {sign}{percentage_change}%")
    print(f"      - Security Rating    : {get_entropy_rating(entropy_cipher)}")

def encrypt_custom(text):
    """Encrypts text using Amit's Custom Substitution Cipher with case-preservation."""
    result = []
    for char in text:
        lower_char = char.lower()
        if lower_char in CIPHER_MAP:
            symbol = CIPHER_MAP[lower_char]
            if char.isupper():
                result.append("^" + symbol)
            else:
                result.append(symbol)
        else:
            result.append(char)
    return "".join(result)

def decrypt_custom(text):
    """Decrypts text back to original form with case restoration."""
    result = []
    i = 0
    while i < len(text):
        if text[i] == "^" and i + 1 < len(text):
            symbol = text[i+1]
            if symbol in REVERSE_MAP:
                result.append(REVERSE_MAP[symbol].upper())
                i += 2
                continue
            else:
                result.append("^")
                i += 1
        else:
            symbol = text[i]
            if symbol in REVERSE_MAP:
                result.append(REVERSE_MAP[symbol])
            else:
                result.append(symbol)
            i += 1
    return "".join(result)

def encrypt_vigenere(text, key):
    """Encrypts text using Vigenere cipher (case-preserving)."""
    result = []
    key = key.lower()
    key_idx = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
            key_idx += 1
        else:
            result.append(char)
    return "".join(result)

def decrypt_vigenere(text, key):
    """Decrypts text using Vigenere cipher (case-preserving)."""
    result = []
    key = key.lower()
    key_idx = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_idx % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(new_char)
            key_idx += 1
        else:
            result.append(char)
    return "".join(result)

def show_interactive():
    print(CYAN + """
  ======================================================
   _________  _______  ___   ___  _________  
  |  _   _  ||  ____ \|   \ /   ||____   ____| 
  |_| | | |_|| |____  |    v    |     | |      
      | |    |  ____| |  |\_/|  |     | |      
      | |    | |____  |  |   |  |     | |      
      |_|    |_______||__|   |__|     |_|      
                                               
               [ textEncrypt Shell Interface ]
  ======================================================
  """ + RESET)
    while True:
        print("  1. Encrypt Text")
        print("  2. Decrypt Text")
        print("  3. Calculate String Entropy")
        print("  4. Exit")
        try:
            choice = input(YELLOW + "\n  Select Option (1-4): " + RESET).strip()
            if choice == "4":
                print(CYAN + "  Goodbye!" + RESET)
                break
            
            if choice == "3":
                text = input(YELLOW + "  Enter string to analyze: " + RESET)
                ent = calculate_entropy(text)
                print(GREEN + f"\n  [+] Shannon Entropy: " + RESET + f"{ent} bits/character")
                print(f"  [+] Rating: {get_entropy_rating(ent)}\n")
                continue

            if choice in ("1", "2"):
                action = "encrypt" if choice == "1" else "decrypt"
                mode = input(YELLOW + "  Select Mode (custom/vigenere) [default: custom]: " + RESET).strip().lower() or "custom"
                if mode not in ("custom", "vigenere"):
                    print(RED + "  [!] Invalid mode. Defaulting to custom." + RESET)
                    mode = "custom"
                
                key = ""
                if mode == "vigenere":
                    key = input(YELLOW + "  Enter Vigenere Key [default: securekey]: " + RESET).strip() or "securekey"
                
                text = input(YELLOW + f"  Enter text to {action}: " + RESET)
                
                if action == "encrypt":
                    res = encrypt_custom(text) if mode == "custom" else encrypt_vigenere(text, key)
                    print(GREEN + f"\n  [+] Result ({mode}): " + RESET + res)
                    show_entropy_analysis(text, res)
                    print()
                else:
                    res = decrypt_custom(text) if mode == "custom" else decrypt_vigenere(text, key)
                    print(GREEN + f"\n  [+] Result ({mode}): " + RESET + res)
                    show_entropy_analysis(res, text)
                    print()
                    
        except (KeyboardInterrupt, EOFError):
            print(RED + "\n\n  [!] Exiting." + RESET)
            break

def main():
    if len(sys.argv) < 2:
        show_interactive()
        return

    parser = argparse.ArgumentParser(description="textEncrypt: A lightweight text encryption utility.")
    parser.add_argument("action", choices=["encrypt", "decrypt", "analyze"], help="Action to perform.")
    parser.add_argument("text", help="Text to encrypt, decrypt, or analyze.")
    parser.add_argument("-m", "--mode", choices=["custom", "vigenere"], default="custom", help="Encryption cipher mode.")
    parser.add_argument("-k", "--key", default="securekey", help="Key for Vigenere cipher.")
    parser.add_argument("-a", "--analyze", action="store_true", help="Include Shannon Entropy analysis in output.")

    args = parser.parse_args()

    if args.action == "analyze":
        ent = calculate_entropy(args.text)
        print(f"Shannon Entropy: {ent} bits/char")
        print(f"Strength Rating: {get_entropy_rating(ent)}")
        return

    if args.action == "encrypt":
        res = encrypt_custom(args.text) if args.mode == "custom" else encrypt_vigenere(args.text, args.key)
        print(res)
        if args.analyze:
            show_entropy_analysis(args.text, res)
            
    elif args.action == "decrypt":
        res = decrypt_custom(args.text) if args.mode == "custom" else decrypt_vigenere(args.text, args.key)
        print(res)
        if args.analyze:
            show_entropy_analysis(res, args.text)

if __name__ == "__main__":
    main()
