import os
import time

def sure(string):
    while 1:
        yesOrNo = input(string+" ").lower()
        if yesOrNo in ["yes","y","yea"]: break

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def counter(n):
    for i in range(n):
        print(n-i)
        time.sleep(1)

def getShape(name):
    if name == "Blob":
        shape = r"""
   /\\||//\  
  / (> <)  \ 
 /    w     \
 \          /
  '--------' 
"""
    elif name == "Ghosterk":
        shape = r"""
  ,----.    
  ( @ @ (   
   \ O   \  
    \     \ 
     \/\/\/\
"""

    elif name == "Slither" :
        shape = r"""
 /\___/\      .- ~ ~ -.
(|)  (|)     /   _ _   `.          _ _ _
 \_VV _/    /  /     \   \     .~  _ _ _  ~ .
   | |~~~~~/  /       \   ( __/  /       ~-. `.
    \ _ _ _ _/          '._ _ _ /                   
"""
    return shape

