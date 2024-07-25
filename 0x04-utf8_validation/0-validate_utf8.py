#!/usr/bin/python3

"""0. UTF-8 Validation"""


def validUTF8(data):
    """ utf 8 validation"""
    counter = 0
    for byte in data:
        byte_bin = format(byte, '08b')  # Convert byte to binary string
        if counter == 0:
            if byte_bin[0] == '0':
                if counter != 0:
                    return False
                continue
            elif byte_bin[:3] == '110':
                counter = 1
            elif byte_bin[:4] == '1110':
                counter = 2
            elif byte_bin[:5] == '11110':
                counter = 3
            else:
                return False
        else:
            if byte_bin[:2] != '10':
                return False
            counter -= 1

            if counter < 0:
                return False

    return counter == 0
