# -*- coding: utf-8 -*-
"""
Created on Tue May 24 11:42:18 2022

@author: Admin
"""

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]  #list1 of 3 entities
row2 = ["⬜️","⬜️","⬜️"]  #list2 of 3 entities
row3 = ["⬜️","⬜️","⬜️"]  #list3 of 3 entities
map = [row1, row2, row3]  # Nested list
print(f"{row1}\n{row2}\n{row3}") 
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0]) #extract unit place from input
verticle = int(position[1])   #extract decimal place from input

selected_row = map[verticle - 1] # hold at any sublist
#print(selected_row)
selected_row[horizontal-1]= "X" # replace any element of hold list.

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")