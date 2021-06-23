original_string = input(" type here")
characters_to_remove = ["!", "(",")", "@", "hello", "hi","what", "is", "when", "why", "am", "he", "where"]

new_string = original_string
for character in characters_to_remove:
  new_string = new_string.replace(character, "")
print(new_string)