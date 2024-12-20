def countChars(words):
  words = words.lower()
  alphabet = { }

  for i in range(len(words)):
    if words[i] in alphabet:
      alphabet[words[i]] += 1
    elif words[i].isalpha():
      # set key only if it is alphabetical letter
      alphabet.setdefault(words[i], 1)

  for key,value in alphabet.items():
    print(f"The {key} character was found {value} times")

def countWords(words):
  words = words.split()
  count = 0

  for word in words:
    count += 1

  print(f"{count} words were found in the document")

def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)
    countWords(file_contents)
    countChars(file_contents)

  print("-- End Report --")
  
main()

