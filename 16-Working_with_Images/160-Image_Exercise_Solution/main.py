from PIL import Image
words = Image.open("word_matrix.png")
mask = Image.open("mask.png")
print(words.size)
mask = mask.resize((words.size[0], words.size[1]))
print(mask.size)
mask.putalpha(150)
words.paste(mask,(0,0),mask)
words.save("word_matrix_mask.png")