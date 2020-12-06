file= open("poem1.txt","r")
lines = file.readlines()
for line in lines:
    print(line)

file.close()
print("file closed")