What is a Variable?
===================
A variable is a value assigned to a key. 
Example: name = "Rishi"
A value gets assigned from rigth to left. Here '=' doesn't means equals. It means assigning. A value in the right side gets assigned to key in the left side. A variable can store any type of data like string, float, boolean, integer, etc..
We can use variables instead of hardcoding the values multiple times in a code.

What is dynamic typing?
======================
A dynamic typing in python is where a same named
It will give NameError as the variable we created has lower case 'c' but the argument in the print function() if calling Upper case 'C'. Python reads both of them as two different variables. Python is Case Sensitive. variable can store any type of data without us mentioning what type of data it is.
Example: x = 5
         x = "10"
while running the code, python will run x = 5 in the first line, and it will take x= "10" in the second line. We donot have to mention the type od data. Python will understand itself and run the code.

what is SyntaxError and NameError?
==================================
A SyntaxError is a type of error in python which arises when the syntax is wrong. Python will not run any line of code when you get this error as it will read the whole lines of code to look for grammatical errors before running the code.
Example: node-count = 5
Python thinks '-' as substraction symbol and gives an SyntaxError. It will not run any line od code in the file.

A NameError is a type of error in python which arises when the you call a variable with a wrong name. It is a runtime error, which means all the lines of code above this error will be run by the python.
Example: cluster_name = "dna"
         print (Cluster_name)
It will give NameError as the variable we created has lower case 'c' but the argument in the print function() if calling Upper case 'C'. Python reads both of them as two different variables. Python is Case Sensitive.
