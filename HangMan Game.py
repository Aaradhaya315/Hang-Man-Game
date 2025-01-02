import random

#words = ["UMBRELLA","COMPUTER","TELESCOPE","SMARTPHONE"]
f= open("words.txt","r")
data= f.readline()
words= data.split()
word = random.choice(words)
word=word.upper()
total_chances= 7
guessed_word = "-"*len(word)

while total_chances != 0:
              print(guessed_word)
letter = input("Guess a leter : ").upper()
if letter in word :
      for index in range(len(word)):
                      if word[index]==letter:
                        guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
                        #print(guessed_word)
                      if guessed_word == word:
                                            print("Congralutions You Won !!!")
                                            break
                      else:
                              total_chances-1
                              print("incorrect guess")
                              print("The remaining chances are:",total_chances)
      else:
              print("Game Over")
              print("You lose")
              print("All Chances are echauted")
              print("the correct word is",word)

            