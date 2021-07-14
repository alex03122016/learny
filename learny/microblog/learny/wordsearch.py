#!python3
# -*- coding: utf-8 -*-
def wordsearch(words):
  import docx
  import os

 #Python Wordsearch Generator - www.101computing.net/python-wordsearch-generator/
  import random
  try:
      import docxprint
  except ImportError:
      from learny import docxprint
  doc = docx.Document()
  save_path = docxprint.docx_print(Doc= doc, save= 'wordsearch')
  Aufgabe = {
      "Kopfzeile": "Name: 				Klasse: 				Datum:  \n ",
      "Titel": "Thema: ",
      "1. Aufgabe": "Finde die Wörter!\n",
      "Hinweise": "Diese Wörter kommen hier vor: \n",
      "Rätselwörter": "Hier ein paar Rätselwörter aus dem Text: \n",
      "Lösung": "Lösung: \n"
  }
  print('words: 		',words)
  ROWS = 20
  COLS = 20
  #words = ["PYTHON","ALGORITHM","CODING","PROGRAM","VARIABLE","INTEGER","STRING"]

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
    table = docxprint.docx_print(
                                    Paragraph="no",
                                    Doc=doc,
                                    NewTable=True,
                                    TableROWS=ROWS,
                                    TableCOLS=COLS)
    #print(table)
    for row in range(0,ROWS):
      line="| "
      for col in range(0,COLS):
        line = line + wordsearch[row][col] + " "
        docxprint.docx_print(printText=wordsearch[row][col],
                            Paragraph="no",
                            Doc=doc,
                            Table=table,
                            TableRow=row,
                            TableCol=col,)
      line = line + "|"

      print(line)
    print("|" + ("_"*COLS*2) + "_|")

  #A subroutine to add a word to the wordsearch at a random position
  def addWord(word,wordsearch):
    placed=False
    attempts = 0
    while not placed and attempts<100: #Avoid infinite loops if the program can't find a place for a word.
      attempts +=1
      direction = random.randint(0,2) #bis 2 ist also nur links-rechts-oben-unten-diagonal; rückwärts wurde ausgespart bis 5
      #Decide Starting Row and Col Position for the first letter of the wor
      #Decide horizontal step (hs) and vertical step (vs)

      if len(word)>ROWS or len(word)>COLS:
        print("Some of your words are too long for this grid. Remove long words or resize your grid. Skipping wordsearch.")
        #exit()
        break

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
  #randomFill(wordsearch)

  docxprint.docx_print(printText=Aufgabe["Lösung"], Doc=doc)

  #Display the fully competed wordseach on screen
  displayWordsearch(wordsearch)

  print("\n--- LIST OF WORDS ---\n")
  for word in words:
    print("  - " + word)
#All unused spaces in the wordsearch will be replaced with a random letter

  #doc = docx.Document(save_path)
  doc.add_page_break()
  docxprint.docx_print(printText=Aufgabe["Kopfzeile"], Doc=doc)
  docxprint.docx_print(Doc=doc)
  docxprint.docx_print(printText=Aufgabe["1. Aufgabe"], Bold=True, Doc=doc)

  randomFill(wordsearch)

  #Display the fully competed wordseach on screen
  displayWordsearch(wordsearch)

  print("\n--- LIST OF WORDS ---\n")
  for word in words:
    print("  - " + word)

  docxprint.docx_print(Doc=doc)
  docxprint.docx_print(printText=Aufgabe["Hinweise"], Doc=doc)
  paragraph = docxprint.docx_print(Doc=doc)
  for word in words:
    print("  - " + word)
    docxprint.docx_print(printText=" - " + word, Paragraph=paragraph, Doc=doc)
  doc.save(save_path)

  return

#some_nouns = ['Abitur', 'King', 'Wunderkind']
#wordsearch(some_nouns)
