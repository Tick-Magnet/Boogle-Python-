# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 12:03:00 2021

@author: Jacob Bowers
"""


import random

def word(g,j,x,array,i,final):
    
    final += str(x[i])

    if x == final:
        return True
    
    i = i +  1


    if (g-1) >= 0:
        north = array [g-1][j]
        if x[i] == north:
            g = g - 1
            r = word(g,j,x,array,i,final)
            if r == False:
                g = g + 1
                
            else:
                return True
    else:
        north = ""
        
        
        
    if (g-1) >= 0 and (j+1) < 4:
        northeast = array [g-1][j+1]
        if x[i] == northeast:
            g = g - 1
            j = j + 1
            r = word(g,j,x,array,i,final)
            if r == False:
                g = g + 1
                j = j -1
            else:
                return True
    else: 
        northeast = ""

    
    
    
    if (j+1) < 4:
        east = array [g][j+1]
        if x[i] == east:
            j = j + 1
            r = word(g,j,x,array,i,final)
            if r == False:
                j = j - 1
            else:
                return True

    else:
        east = ""
        
        
        
    if (g+1) < 4 and (j+1) < 4:
        southeast = array [g+1][j+1]
        if x[i] == southeast:
            g = g + 1
            j = j + 1
            r = word(g,j,x,array,i,final)
            if r == False:
                g = g - 1
                j = j - 1
            else:
                return True
    else: 
        southeast = ""




    if (g+1) < 4:
        south = array [g+1][j]
        if x[i] == south:
            g = g + 1
            r = word(g,j,x,array,i,final)
            if r == False:
                g = g - 1
            else:
                return True
    else:
        south = ""
    
    
    
    
    if (g+1) < 4 and (j-1) >= 0:
        southwest = array [g+1][j-1]
        if x[i] == southwest:
            g = g + 1
            j = j - 1
            r = word(g,j,x,array,i,final)
            return r
            if r == False:
                g = g - 1
                j = j + 1
            else:
                return True
            
    else: 
        southwest = ""
        
    if (j-1) >= 0:
        west = array [g][j-1]
        if x[i] == west:
            j = j - 1
            r = word(g,j,x,array,i,final)
            if r == False:
                j = j + 1
            else:
                return True
    else:
        west = ""
    
    
    
    if (g-1) >= 0 and (j-1) >= 0:
        northwest = array [g-1][j-1]
        if x[i] == northwest:
            g = g - 1
            j = j -1
            r = word(g,j,x,array,i,final)
            if r == False:
                g = g + 1
                j = j +1
            else:
                return True
    else:
        northwest = ""

    return False
    
       
   

    
def boggle():
   
    die_1 = ["A","E","A","N","E","G"]
    random.shuffle(die_1)
    
    die_2 = ["A","H","S","P","C","O"]
    random.shuffle(die_2)
    
    die_3 = ["A","S","P","F","F","K"]
    random.shuffle(die_3)
    
    die_4 = ["O","B","J","O","A","K"]
    random.shuffle(die_4)
    
    die_5 = ["I","O","T","M","U","C"]
    random.shuffle(die_5)
    
    die_6 = ["R","Y","V","D","E","L"]
    random.shuffle(die_6)
    
    die_7 = ["L","R","E","I","X","D"]
    random.shuffle(die_7)
    
    die_8 = ["E","I","U","N","E","S"]
    random.shuffle(die_8)
    
    die_9 = ["W","N","G","E","E","H"]
    random.shuffle(die_9)
    
    die_10 = ["L","N","H","N","R","Z"]
    random.shuffle(die_10)
    
    die_11 = ["T","S","T","I","Y","D"]
    random.shuffle(die_11)
    
    die_12 = ["O","W","T","O","A","T"]
    random.shuffle(die_12)
    
    die_13 = ["E","R","T","T","Y","L"]
    random.shuffle(die_13)
    
    die_14 = ["T","O","E","S","S","I"]
    random.shuffle(die_14)
    
    die_15 = ["T","E","R","W","H","V"]
    random.shuffle(die_15)
    
    die_16 = ["N","U","I","H","M","Q"]
    random.shuffle(die_16)
    
    boggle_board = [die_1[0], die_2[0], die_3[0], die_4[0], die_5[0], die_6[0], die_7[0], die_8[0], 
                    die_9[0], die_10[0], die_11[0], die_12[0], die_13[0], die_14[0], die_15[0], die_16[0]]
    random.shuffle(boggle_board)
    
    
    array = [ [boggle_board[0] , boggle_board[1] ,boggle_board[2] , boggle_board[3]] , [boggle_board[4] , boggle_board[5] , boggle_board[6] , boggle_board[7]] , [boggle_board[8],boggle_board[9],boggle_board[10],boggle_board[11] ] , [ boggle_board[12] , boggle_board[13] , boggle_board[14] , boggle_board[15] ] ]
    print(array)
    
    print("[" + array[0][0] + "] " + "[" + array[0][1] + "] " + "[" + array[0][2] + "] " + "[" + array[0][3] + "] ")
    print("[" + array[1][0] + "] " + "[" + array[1][1] + "] " + "[" + array[1][2] + "] " + "[" + array[1][3] + "] ")
    print("[" + array[2][0] + "] " + "[" + array[2][1] + "] " + "[" + array[2][2] + "] " + "[" + array[2][3] + "] ")
    print("[" + array[3][0] + "] " + "[" + array[3][1] + "] " + "[" + array[3][2] + "] " + "[" + array[3][3] + "] ")
    
    
   
    print("Start typing your words! (press enter after each word and enter 'X' when done): ")    
    
    word_list = []
    scored_list = []
    total_points = 0
    loop = True
    
    
    while loop == True:
        enter = input(">")
        if enter == "":
            break
        if enter == "X" or enter == "x":
            break
        else:
            word_list.append(enter)
    
    for x in word_list:    
        x = x.upper()
        
        if x in scored_list:
            print("The word " + x + " has already been used.")
            continue
        if len(x) < 3:
            print("The word " + x + " is too short.")
            continue
        else:
            if len(x) == 3:
                points = 1
            elif len(x) == 4:
                points = 1
            elif len(x) == 5:
                points = 2
            elif len(x) == 6:
                points = 3
            elif len(x) == 7:
                points = 5
            elif len(x) > 8:
                points = 11

           
        if x[0] in boggle_board:   
            for g in range(len(array)):
                for j in range(len(array[g])):
                    if x[0] == array[g][j] and x not in scored_list:
                        i = 0;
                        final = ""
                        answer = word(g,j,x,array,i,final)
                        
                        if answer == True:
                            with open('words.txt') as myfile:
                                lower = x.lower()
                                if lower in myfile.read():
                                    print("The word " + x + " is worth " + str(points) + " point(s).")
                                    total_points += points
                                    scored_list.append(x)
                                    break
                                else:
                                    print("The word " + x + " is not a word.")
                        else:
                          print("The word " + x + " is not present in the grid.")
                          
    print("Your total score is " + str(total_points) + " points!" )                     
boggle()
