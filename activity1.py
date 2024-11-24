# write in file using with()function
with open('Codingal (1).text', 'w') as file:
    file.write("Hi ! I am penguin and I am 1 yr old.")
    file.close()

with open('Codingal (1).txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are...")
    for line in data:
        word = line.split()
        print (word)
    file.close