#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""

    def is_multi_byte(number):
        """Checks if the number is a multi-byte character"""
        return number.startswith('10')

    data_iter = iter(data)
    for number in data_iter:
        # get the binary representation of the number with 8 bits
        bin_rep = format(number, '#010b')[-8:]

        if bin_rep[0] == '0':
            continue
        n_bytes = len(bin_rep.split('0')[0])

        # check if the number of bytes is valid
        if n_bytes == 1 or n_bytes > 4:
            return False

        # check if the next n_bytes - 1 numbers are valid
        for _ in range(n_bytes - 1):
            number = next(data_iter, None)
            if not number or not is_multi_byte(format(number, '#010b')[-8:]):
                return False
    return True


# tests
# data = [65]
# print(validUTF8(data))

# data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
# print(validUTF8(data))

# data = [229, 65, 127, 256]
# print(validUTF8(data))

# data = [467, 133, 108]  # true
# print(validUTF8(data))

# data = [240, 188, 128, 167]  # true
# print(validUTF8(data))

# data = [235, 140]  # false
# print(validUTF8(data))

# data = [250, 145, 145, 145, 145]  # false
# print(validUTF8(data))

# data = [0, 0, 0, 0, 0, 0]  # true
# print(validUTF8(data))

# data = []  # true
# print(validUTF8(data))
