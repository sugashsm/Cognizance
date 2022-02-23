A = [ [1, "Sujith", 75],
     [2, "Varun", 85],
     [3, "Srimitha", 95]]   
print ("{:<10} {:<10} {:<10}".format('Roll No','Name','Marks'))
for B in A:
    Roll, name, marks = B
    print ("{:<10} {:<10} {:<10}".format( Roll, name, marks))
print("")
print("")
print("THE Second row of the table:");

import pandas as pd
X = [ [1, "Sujith", 75],
     [2, "Varun", 85],
     [3, "Srimitha", 95]]
print("")
data = pd.DataFrame([2, "VARUN", 85])
print ("{:<6} {:<6} {:<6}".format('2','VARUN','85'))
