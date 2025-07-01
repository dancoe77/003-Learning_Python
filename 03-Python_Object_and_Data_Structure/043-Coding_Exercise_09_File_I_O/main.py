with open("test.txt","w", encoding="UTF-8") as f:
    f.write("Hello Milky Way")
with open("test.txt","r") as f:
    print(f.read())