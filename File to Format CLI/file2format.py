"""
Program to detect file format type based on their signatures.
"""

import os
import sys
from signatures import signatures

# ===================== CONSTANTS =====================

input_directory = "./samples/"
input_files = [
    "c-refcard.mp4",
    "earth.pdf",
    "headingwebsite",
    "list.jpg",
    "roman.png",
    "startoken.elf",
]


# ================= HELPER FUNCTIONS =================


def get_hexadecimal_file_header(input_file):

    with open(input_file, "rb") as file:
        file_header = file.read(34000)
        print(f"File Header: {file_header[:32]}")

    # Converting file header to decimal form, stored in a list
    file_header_dec = list(file_header)
    print(f"File Header (Dec): {file_header_dec[:32]}")

    # Converting each element of file header list to hexadecimal
    file_header_hex = [None] * len(file_header_dec)

    for i in range(len(file_header_dec)):
        val = hex(file_header_dec[i])[2:]

        if len(val) == 1:
            file_header_hex[i] = "0" + val.upper()
        else:
            file_header_hex[i] = val.upper()
    print(f"File Header (Hex): {file_header_hex[:32]}")

    return file_header_hex


# ============= SIGNATURE COMPARE FUNCTION =============


def compare_signature(input_file):
    file_extension = None
    description = None

    print("=" * 100)
    print(f"File Name: {input_file}", end="\n\n")

    if not os.path.exists(input_file):
        print(f"ERROR: {input_file} doesn't exists")
        return

    file_header_hex = get_hexadecimal_file_header(input_file)

    # Compare each element of the signatures list with the hexadecimal file header
    for element in signatures:
        hex_value = element["hex"].split(" ")
        length = len(hex_value)

        if element["offset"][:2] == "0x":
            offset = int(element["offset"][2:], 16)
        else:
            offset = int(element["offset"])

        if hex_value == file_header_hex[offset : length + offset]:
            file_extension = element["extension"]
            description = element["description"]
            break

    # Returns the final output
    print()

    if not file_extension:
        print(
            f"The signature of file '{input_file}' was not found in our index of 185 file signatures."
        )
    else:
        print(f"File Format: {file_extension}")
        print(f"Description: {description}")


# ==================== MAIN CODE ====================


if len(sys.argv) == 1:
    input_files = [input_directory + input_file for input_file in input_files]
elif len(sys.argv) > 1:
    input_files = sys.argv[1:]

for input_file in input_files:
    compare_signature(input_file)
