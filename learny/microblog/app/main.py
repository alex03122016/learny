#Python Wordsearch Generator - www.101computing.net/python-wordsearch-generator/
import random

ROWS = 12
COLS = 12
words = ["PYTHON","ALGORITHM","CODING","PROGRAM","VARIABLE","INTEGER","STRING"]

#A subroutine to replace all "-" (empty characters) with a random letter
def randomFill(wordsearch):
  LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for row in range(0,ROWS):
    for col in range(0,COLS):
      if wordsearch[row][col]=="-":
        randomLetter = random.choice(LETTERS)
        wordsearch[row][col]=randomLetter

#A subroutine to output the wordsearch on screen    
def displayWordsearch(wordsearch):
  print(" " + ("_"*COLS*2) + "_ ")
  print("|" + (" "*COLS*2) + " |")
  for row in range(0,ROWS):
    line="| "
    for col in range(0,COLS):
      line = line + wordsearch[row][col] + " "
    line = line + "|"
    print(line)
  print("|" + ("_"*COLS*2) + "_|")  
    
#A subroutine to add a word to the wordsearch at a random position
def addWord(word,wordsearch):
  placed=False
  attempts = 0
  while not placed and attempts<100: #Avoid infinite loops if the program can't find a place for a word.
    attempts +=1
    direction = random.randint(0,5)
    #Decide Starting Row and Col Position for the first letter of the wor
    #Decide horizontal step (hs) and vertical step (vs)
    
    if len(word)>ROWS or len(word)>COLS:
      print("Some of your words are too long for this grid. Remove long words or resize your grid.")
      exit()
    
    if direction==0: #Horizontal Left to Right
      row=random.randint(0,ROWS - 1)
      col=random.randint(0,COLS - len(word))
      hs=1
      vs=0
    elif direction==1: #Vertical Top - To Bottom
      row=random.randint(0,ROWS - len(word))
      col=random.randint(0,COLS - 1) 
      hs=0
      vs=1      
    elif direction==2: #Diagonal Top Left - To Bottom Right
      row=random.randint(0,ROWS - len(word))
      col=random.randint(0,COLS - len(word))  
      hs=1
      vs=1      
    if direction==3: #Horizontal Right to Left
      row=random.randint(0,ROWS - 1)
      col=random.randint(len(word)-1,COLS - 1)
      hs=-1
      vs=0
    elif direction==4: #Vertical Top - To Bottom
      row=random.randint(len(word)-1,ROWS - 1)
      col=random.randint(0,COLS - 1) 
      hs=0
      vs=-1      
    elif direction==5: #Diagonal Top Left - To Bottom Right
      row=random.randint(len(word)-1,ROWS - 1)
      col=random.randint(len(word)-1,COLS - 1)  
      hs=-1
      vs=-1      

    #Check if words fit without colliding with other letters
    collision=False
    for i in range(0,len(word)):
      if (wordsearch[row+vs*i][col+hs*i]!="-" and wordsearch[row+vs*i][col+hs*i]!=word[i]):
        collision=True
    #Collision means we can addthe word to the gird
    if not collision:
      for i in range(0,len(word)):
        wordsearch[row+vs*i][col+hs*i]=word[i]
        placed=True

  if not placed:
    print("Program aborted. Try again, remove words from your list or increase the size of the grid.")
    exit()


#Create an empty wordsearch (list of lists)
wordsearch = []
for row in range(0,ROWS):
  wordsearch.append([])
  for col in range(0,COLS):
    wordsearch[row].append("-")

#Adding words to our wordsearch
for word in words:
  if word != "":
    addWord(word,wordsearch)    


#All unused spaces in the wordsearch will be replaced with a random letter
randomFill(wordsearch)

#Display the fully competed wordseach on screen
displayWordsearch(wordsearch)
  
print("\n--- LIST OF WORDS ---\n")  
for word in words:
  print("  - " + word)
