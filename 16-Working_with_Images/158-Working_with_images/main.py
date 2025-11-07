from PIL import Image
mac = Image.open("example.jpg")
print(type(mac))
print(mac)
# mac.show()
print(mac.size)
print(mac.filename)
print(mac.format_description)
mac.crop((0,0,100,100))
pencils = Image.open("pencils.jpg")
# pencils.show()
print(pencils.size)
x = 0
y = 0

w = 1950 / 3
h = 1300 / 10
pencils.crop((x,y,w,h))

x = 0
y = 1100
w = 1950 / 3
h = 1300

print(mac.size)
halfway = 1993/2

x = halfway - 200
w = halfway + 200

y = 800
h = 1257
mac.crop((x,y,w,h))
computer = mac.crop((x,y,w,h))
mac.paste(im=computer,box=(0,0))
print(mac.size)
mac.resize((3000,500))
mac.rotate(90)

red = Image.open("red_color.jpg")
blue = Image.open("blue_color.png")
blue = Image.open('blue_color.png')
blue_new = blue.convert('RGB')
blue_new.save("blue_new.jpg")
blue = Image.open('blue_new.jpg')

blue.putalpha(128)
# blue.show()
red.putalpha(128)
blue.paste(im=red,box=(0,0))
# blue.show()

blue.save("purple.png","PNG")