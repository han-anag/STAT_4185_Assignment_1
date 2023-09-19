encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
message = list(encrypted_message)

a = 0
b = len(message)-1

while a < b:
    c = message[b]
    message[b] = message[a]
    message[a] = c
    a += 2
    b -= 2

message.reverse()

message_str = ''.join(message)
print(message_str)

