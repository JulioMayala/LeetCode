class Solution(object):
    def isValid(self, s):
       my_pile=list()
       others={")":"(", "]":"[", "}":"{"}
       for char in s:
           if char in others:
               top= my_pile.pop() if my_pile else '#'
               if others[char]!= top:
                   return False
           else:
               my_pile.append(char)
       return len(my_pile)==0