"""
ImgVault - Image Encryption and Decryption Tool

This module contains the main logic to Encryption and Decryption
of Images.
"""

import os
import argparse
from PIL import Image
from tqdm import tqdm

def xorEncryptDecrypt(number, key):
    """
    XOR operator.

    This function switches the color of the input and
    returns within the range 255.

    Keyword Arguments:
    number                 -- Integer which contains R/G/B value.
    key                    -- Integer which contains the key to encrypt/decrypt.
    
    Return Value:
    XORed new R/G/B value.
    """

    return (number ^ key) % 256

def imageEncryption(path, key, iv):
    """
    Encryption.

    This fuction manipulates each pixel of an image
    and encrypts it.

    Keyword Arguments:
    path                   -- String which contains the path of image.
    key                    -- Integer which contains the key to encrypt/decrypt.
    iv                     -- Integer which contains the initial value.

    Return Value:
    String image name.
    """

    image = Image.open(path)
    image = image.convert('RGB')
    width, height = image.size

    modifiedImage = Image.new('RGB', (width, height))
    
    for x in range(width):
        for y in range(height):
    
            (
                R,
                G,
                B,
            ) = image.getpixel((x, y))

            R = R ^ iv
            G = G ^ iv
            B = B ^ iv  
             
            newR,newG,newB = ( 
                xorEncryptDecrypt(R,key),
                xorEncryptDecrypt(G,key),
                xorEncryptDecrypt(B,key) 
            )
            modifiedImage.putpixel((x, y), (newR, newG, newB))

            iv = newR + newG + newB

    modifiedImage.save('image_enc.png')
    return 'image_enc.png'

def imageDecryption(path,key,iv):
    """
    Decryption.

    This fuction manipulates each pixel of an image
    and decrypts it.

    Keyword Arguments:
    path                   -- String which contains the path of image.
    key                    -- Integer which contains the key to encrypt/decrypt.
    iv                     -- Integer which contains the initial value.

    Return Value:
    String image name.
    """

    image = Image.open(path)
    image = image.convert('RGB')
    width, height = image.size

    modifiedImage = Image.new('RGB', (width, height))
       
    for x in range(width):
        for y in range(height):
    
            (
                R,
                G,
                B,
            ) = image.getpixel((x, y))
            
            newR,newG,newB = (
                xorEncryptDecrypt(R,key),
                xorEncryptDecrypt(G,key),
                xorEncryptDecrypt(B,key)
            ) 
            
            newR = (newR ^ iv ) %256
            newG = (newG ^ iv ) %256
            newB = (newB ^ iv ) %256

            modifiedImage.putpixel((x, y), (newR, newG, newB))
            
            iv = R + G + B

    modifiedImage.save('image_dec.png')
    return 'image_dec.png'

def main():

    desc = """
        Encryption or Decryption of Images.
        The input value taken are
            - Path of image (String)
            - Key (Integer)
            - Initial value (Integer)
            - Rounds (Integer)
    """

    parser = argparse.ArgumentParser(
        description = desc, formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        '-e', 
        '--encrypt', 
        help='Encrypt the image input data', 
        type=str, 
        nargs = 4,
        metavar=('<imagePath>', '<key>', '<initialValue>', '<rounds>')
    )
    parser.add_argument(
        '-d', 
        '--decrypt', 
        help='Decrypt the image input data', 
        type=str, 
        nargs = 4,
        metavar=('<imagePath>', '<key>', '<initialValue>', '<rounds>')
    )
    
    args = parser.parse_args()

    if args.encrypt:
        if os.path.exists(args.encrypt[0]):
            try:
                if int(args.encrypt[3]) <= 0:
                    print("Rounds should be greater than 0.")
                else:
                    path = args.encrypt[0]
                    for _ in tqdm(range(int(args.encrypt[3]))):
                        path = imageEncryption(path,int(args.encrypt[1]),int(args.encrypt[2]))
            except:
                print("Unidentified image formate.")
        else:
            print("File does not exist.")
    
    if args.decrypt:
        if os.path.exists(args.decrypt[0]):
            try:
                if int(args.decrypt[3]) <= 0:
                    print("Rounds should be greater than 0.")
                else:
                    path = args.decrypt[0]
                    for _ in tqdm(range(int(args.decrypt[3]))):
                        path = imageDecryption(path,int(args.decrypt[1]),int(args.decrypt[2]))
            except:
                print("Unidentified image formate.")
        else:
            print("File does not exist.")
    
if __name__ == '__main__':
    main()