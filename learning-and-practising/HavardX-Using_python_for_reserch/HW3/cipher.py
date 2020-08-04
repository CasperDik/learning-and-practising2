import string

alphabet = " " + string.ascii_lowercase

positions = {}
for i in range(27):
    positions[alphabet[i]] = i

def encode(message, key = 0):
    encoded_message = ""
    for letter in message:
        position = positions[letter]
        encoded_position =(position + key) % 27
        encoded_message += alphabet[encoded_position]
    return encoded_message

def decode(encoded_message, key=0):
    decoded_message = encode(encoded_message, -key)
    return decoded_message

message = "hi my name is caesar"
x = encode(message, 3)
print(decode(x, 3))