```text
====================================================================
  █████╗ ███╗   ███╗██╗████████╗ ██████╗ ██╗  ██╗██╗  ██╗
 ██╔══██╗████╗ ████║██║╚══██╔══╝██╔═══██╗██║  ██║╚██╗██╔╝
 ███████║██╔████╔██║██║   ██║   ██║   ██║███████║ ╚███╔╝ 
 ██╔══██║██║╚██╔╝██║██║   ██║   ██║   ██║██╔══██║ ██╔██╗ 
 ██║  ██║██║ ╚═╝ ██║██║   ██║   ╚██████╔╝██║  ██║██╔╝ ██╗
 ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
====================================================================
```

# textEncrypt

**textEncrypt** is a lightweight command-line utility for encrypting and decrypting text using reversible ciphers. It features a unique **Shannon Entropy Analyzer** to measure the randomness and cryptographic strength of both plaintext and ciphertext.

Designed for security enthusiasts, bug bounty hunters, and developers who want a quick text obfuscation, encryption, and cryptographic complexity analysis utility.

---

## 🛡️ Features

- **Bidirectional Custom Cipher:** Uses Amit's classic character mapping (A ➔ 1, J ➔ !, Z ➔ }) with added support for case-preservation and decryption.
- **Vigenère Cipher Support:** Adds standard Vigenère polyalphabetic cipher for key-based case-preserving encryption and decryption.
- **Shannon Entropy Analyzer:** 
  - Measures text complexity and diffusion in bits per character (0.0 to 8.0).
  - Dynamically calculates the complexity change percentage between plaintext and ciphertext.
  - Automatically assesses the strength of the cipher (Weak, Moderate, Strong).
- **argparse CLI Interface:** Clean integration with flags and positional arguments.
- **Interactive TUI Shell:** Initiates a styled terminal interface when executed without arguments.

---

## ⚙️ Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/amit0hx/textEncrypt.git
   ```
2. **Navigate to the Directory:**
   ```bash
   cd textEncrypt
   ```

---

## 💻 Usage

### 1. CLI Mode (Command Line Arguments)

#### Custom Cipher (Default)
```bash
# Encrypt text using Amit's custom substitution cipher
python text_encrypt.py encrypt "Hello World"

# Decrypt the output back to original text (preserving case)
python text_encrypt.py decrypt "^85##^o ^=^o(#!4"
```

#### Vigenère Cipher (Key-based)
```bash
# Encrypt using a custom key
python text_encrypt.py encrypt "Attack at Dawn" --mode vigenere --key "mysecretkey"

# Decrypt using the same key
python text_encrypt.py decrypt "Mttsgo sd Hsko" --mode vigenere --key "mysecretkey"
```

#### Shannon Entropy Analysis (Add `-a` or `--analyze` flag)
You can append `-a` to any encrypt/decrypt CLI command to output the Shannon Entropy profile:
```bash
python text_encrypt.py encrypt "Attack at Dawn" --mode vigenere --key "secret" --analyze
```
*Output:*
```text
[>] Shannon Entropy & Cryptographic Analysis:
    - Plaintext Entropy  : 3.239 bits/char
    - Ciphertext Entropy : 3.239 bits/char
    - Complexity Change  : +0.0%
    - Security Rating    : MODERATE (Basic Obfuscation)
```

#### Standalone Complexity Analysis
To measure the entropy of any raw string:
```bash
python text_encrypt.py analyze "InputYourPlaintextOrCiphertextHere"
```

---

## 📂 Project Structure

```text
textEncrypt/
├── text_encrypt.py       # Main entry point (CLI, Interactive TUI, & Entropy calculations)
├── LICENSE               # MIT Open Source License
├── .gitignore            # Python cache and IDE exclusions
└── README.md             # Project documentation & setup instructions
```

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
====================================================================