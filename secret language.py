 exercise 2 : a secret coding language?????
  a = input("Enter the sentence:")
  words = a.split()
  print(words)
  print("What do you want to do?")
  print("1. Encoding \t 2. Decoding")
  b = input("Enter your choice:")
def create_random():
    import random
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    random_number = ''.join(random.choice(alphabet) for _ in range(3))
    return random_number
if b == "1":
    new_word = []
    space = " "
    for word in words:
        r1 = create_random()
        r2 = create_random()
        if len(word) >= 3:
            new_word.append(r1 + word[1:] + word[0] + r2)
        else:
            new_word.append(word[::-1])
    x = space.join(new_word)
    print("The encoding of your sentence is:")
    print(x)

if b == "2":
    new_word = []
    space = " "
    for word in words:
        if len(word) >= 3:
            new_word.append(word[-4] + word[3:-4])
        else:
            new_word.append(word[::-1])
    x = space.join(new_word)
    print("The Decoding of your sentence is:")
    print(x)
