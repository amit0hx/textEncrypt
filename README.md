<div align="center">

# textEncrypt

**A command-line text encryption utility with custom cipher, Vigenère cipher, and Shannon entropy analysis — built in Python.**

[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

</div>

---

## Overview

textEncrypt is a lightweight CLI tool for encrypting, decrypting, and analyzing text using two cipher modes. It includes a built-in Shannon Entropy Analyzer that measures the cryptographic strength and randomness of both plaintext and ciphertext.

Designed for security enthusiasts, CTF players, and developers who need quick text obfuscation with measurable complexity metrics.

---

## Supported Ciphers

| Cipher | Type | Key Required | Case Preserving |
|--------|------|:------------:|:---------------:|
| **Custom** | Monoalphabetic substitution (A→1, J→!, Z→}) | No | Yes |
| **Vigenère** | Polyalphabetic shift cipher | Yes | Yes |

---

## Getting Started

### Prerequisites

- Python 3.6 or later (no external dependencies)

### Installation

```bash
git clone https://github.com/amit0hx/textEncrypt.git
cd textEncrypt
```

---

## Usage

### CLI Mode

#### Custom Cipher (Default)

```bash
# Encrypt
python text_encrypt.py encrypt "Hello World"

# Decrypt
python text_encrypt.py decrypt "^85##^o ^=^o(#!4"
```

#### Vigenère Cipher

```bash
# Encrypt with key
python text_encrypt.py encrypt "Attack at Dawn" --mode vigenere --key "mysecretkey"

# Decrypt with same key
python text_encrypt.py decrypt "Mttsgo sd Hsko" --mode vigenere --key "mysecretkey"
```

#### Shannon Entropy Analysis

Append `-a` to any encrypt/decrypt command to include entropy metrics:

```bash
python text_encrypt.py encrypt "Attack at Dawn" --mode vigenere --key "secret" --analyze
```

Output:

```
[>] Shannon Entropy & Cryptographic Analysis:
    - Plaintext Entropy  : 3.239 bits/char
    - Ciphertext Entropy : 3.239 bits/char
    - Complexity Change  : +0.0%
    - Security Rating    : MODERATE (Basic Obfuscation)
```

#### Standalone Entropy Analysis

Measure the entropy of any arbitrary string:

```bash
python text_encrypt.py analyze "InputYourTextHere"
```

### Interactive Mode

Launch without arguments for the terminal shell interface:

```bash
python text_encrypt.py
```

| Option | Action |
|--------|--------|
| `1` | Encrypt text (custom or Vigenère) |
| `2` | Decrypt text (custom or Vigenère) |
| `3` | Calculate Shannon entropy of a string |
| `4` | Exit |

---

## CLI Reference

| Flag | Description | Default |
|------|-------------|---------|
| `action` | `encrypt`, `decrypt`, or `analyze` | — (required) |
| `text` | Input string to process | — (required) |
| `-m`, `--mode` | Cipher mode: `custom` or `vigenere` | `custom` |
| `-k`, `--key` | Encryption key (Vigenère only) | `securekey` |
| `-a`, `--analyze` | Include Shannon entropy output | `false` |

---

## Entropy Rating Scale

| Entropy (bits/char) | Rating | Meaning |
|:--------------------:|--------|---------|
| < 3.0 | **Weak** | Highly predictable, trivial to break |
| 3.0 – 4.5 | **Moderate** | Basic obfuscation, not cryptographically secure |
| > 4.5 | **Strong** | High randomness, good diffusion properties |

---

## Project Structure

```
textEncrypt/
├── text_encrypt.py   # CLI parser, cipher engines, entropy calculator, interactive shell
├── LICENSE           # MIT License
├── .gitignore        # Python cache exclusions
└── README.md
```

---

## Disclaimer

These ciphers are **educational implementations** and are not suitable for protecting sensitive data. For production use, use established cryptographic libraries (e.g., `cryptography`, `PyCryptodome`) with proven algorithms (AES, ChaCha20).

---

## License

Distributed under the [MIT License](LICENSE).

---

<div align="center">
  <sub>Built by <a href="https://github.com/amit0hx">@amit0hx</a></sub>
</div>