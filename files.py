myfile = open("a.txt","a+")

i = input("Enter your name:")
myfile.write(i+"\n")
print(myfile.tell())
myfile.seek(0)
c = myfile.read()
print(c)
myfile.close()