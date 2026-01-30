import math
import os

def calculate_entropy(file_path):
    print("Checking file:", file_path)

    if not os.path.exists(file_path):
        print("❌ File not found")
        return 0

    try:
        with open(file_path, "rb") as f:
            data = f.read()

        print("File size:", len(data))

        if not data:
            print("❌ File is empty")
            return 0

        byte_frequency = {}
        for byte in data:
            byte_frequency[byte] = byte_frequency.get(byte, 0) + 1

        entropy = 0
        data_length = len(data)

        for freq in byte_frequency.values():
            probability = freq / data_length
            entropy -= probability * math.log2(probability)

        return entropy

    except Exception as e:
        print("❌ Error:", e)
        return 0
