text = input()
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in text.lower():
   index = alphabet.find(char)
   new_index = index + shift
   new_char = alphabet[new_index]