import os

filepath = input("Please choose the directory you want to save this file to: ")

if (os.path.isdir(filepath) == False):
  os.mkdir(filepath)

filename = input("Please specify a filename: ")
name = input("what is your name: ")
address = input("what is your address: ")
phone = input("what is your phone number: ")
words = name + '\n' + address +'\n' + phone

with open(os.path.join(filepath,filename), 'w') as filehandle:
  filehandle.write(words)

print(f"Great, we stored that text in [{os.path.join(filepath,filename)}]:")

with open(os.path.join(filepath,filename), 'r') as filehandle:
