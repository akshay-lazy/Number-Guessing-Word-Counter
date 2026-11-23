
file = open("sample.txt", "r")

text = file.read()

file.close()


words = text.lower().split()


count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1


print("Total words:", len(words))

print("\nWord Frequency:")

for word in count:
    print(word, ":", count[word])
