# CLI Image Encryption / Decryption Tool

## Overview

ImgVault - Image Encryption and Decryption Tool, is designed to securely encrypt and decrypt images using a method based on the XOR operation. The project employs Cipher Block Chaining (CBC) mode, where each pixel's color value is XORed with both a key and an initial value (IV) to enhance security. The IV is updated dynamically as the encryption progresses, adding an extra layer of complexity. Additionally, you have included the concept of rounds, allowing for repeated encryption/decryption passes over the image for stronger protection. The tool supports both encryption and decryption through command-line arguments.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/AmalRitessh/CLI-Image-Encryption-Decryption-Tool.git
```
2. Navigate to the project directory:
```bash
cd ImgVault
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Encrypting Images.
```bash
# The format to pass variables
python3 ImgVault.py -e <path-to-img> <key> <initial-value> <no-of-rounds>
```
```bash
# Example usage
python3 ImgVault.py -e cat.jpg 4630 5734 13
```
```bash
# Example usage
python3 ImgVault.py --encrypt cat.jpg 4630 5734 13
```
2. Decrypting Images.
```bash
# The format to pass variables
python3 ImgVault.py -d <path-to-img> <key> <initial-value> <no-of-rounds>
```
```bash
# Example usage
python3 ImgVault.py -d image_enc.png 4630 5734 13
```
```bash
# Example usage
python3 ImgVault.py --decrypt image_enc.png 4630 5734 13
```
3. Help
```bash
python3 ImgVault.py -h
```

```bash
python3 ImgVault.py --help
```

## Example Output
| Original Image | Encrypted Image | Decrypted Image |
| --- | --- | --- |
| <img alt="Original" width="280" src="https://github.com/AmalRitessh/ImgVault/blob/main/examples/cat.jpg"> | <img alt="Encrypted" width="280" src="https://github.com/AmalRitessh/ImgVault/blob/main/examples/image_enc.png"> | <img alt="Decrypted" width="280" src="https://github.com/AmalRitessh/ImgVault/blob/main/examples/image_dec.png"> |
