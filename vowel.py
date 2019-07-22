vowel = ['a','e','i','o','u']
constant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
letter = input()
if letter in vowel:
  print("Vowel")
elif letter in constant:
  print("Consonant")
