#!/usr/bin/python3

"""0. UTF-8 Validation"""

def validUTF8(data):
    """ utf 8 validation"""
    counter = 0
    for byte in data:
        byte_bin = format(byte, '08b')  # Convert byte to binary string
        if counter == 0:
            if byte_bin[0] == '0':
                continue  # Single-byte character
            elif byte_bin[:3] == '110':
                counter = 1  # Start of 2-byte character
            elif byte_bin[:4] == '1110':
                counter = 2  # Start of 3-byte character
            elif byte_bin[:5] == '11110':
                counter = 3  # Start of 4-byte character
            else:
                return False  # Invalid UTF-8 start byte
        else:
            if byte_bin[:2] != '10':
                return False  # Invalid continuation byte
            counter -= 1
            
            if counter < 0:
                return False  # More continuation bytes than expected

    return counter == 0  # Valid if counter is 0 at the end
