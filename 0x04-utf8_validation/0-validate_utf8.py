#!/usr/bin/python3
"""
This script implements a method that determines
if a given data set represents a valid UTF-8
encoding
"""


def validUTF8(data):
    """Function that determines a valid UTF-8 encoding.
    """
    # Number of bytes in the current UTF-8 character
    remaining_bytes = 0

    # Masks to check the leading bits
    one_byte = 0b10000000
    two_byte = 0b11100000
    three_byte = 0b11110000
    four_byte = 0b11111000
    continuation_byte = 0b11000000

    for byte in data:
        # If no bytes are expected, identify the leading byte pattern
        if remaining_bytes == 0:
            if (byte & one_byte) == 0:
                # 1-byte character, nothing to do
                continue
            elif (byte & two_byte) == 0b11000000:
                remaining_bytes = 1
            elif (byte & three_byte) == 0b11100000:
                remaining_bytes = 2
            elif (byte & four_byte) == 0b11110000:
                remaining_bytes = 3
            else:
                # Invalid starting byte
                return False
        else:
            # Check that byte starts with `10`
            if (byte & continuation_byte) != 0b10000000:
                return False
            remaining_bytes -= 1

    # If remaining_bytes is not zero, then not all start bytes
    # had the correct following bytes
    return remaining_bytes == 0
