""" 
start
get the numbers of sheets
 sheets / 5 
 round answer to next number
 output the result to the user
 end
 """

import math
# Input : sheet
def calculate (sheet):
  answer = (sheet / 5)
  rounded = math.ceil(answer)
  print ("sheet is : ", sheet)
  print ("The answer is :", answer)
  print ("rounded is:", rounded)
  print ("==================================")
  #output number of stamps needed for sheet 
  return rounded

output = calculate (21)

print ("The number of stamps needed is:", output)


