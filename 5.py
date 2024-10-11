'''
The continue statement in Python is used within loops to skip the current iteration and proceed to the next iteration of the loop. When the continue statement is encountered, the remaining code inside the loop for the current iteration is skipped, and the loop continues with the next iteration.

Purpose of the continue Statement
Skip Specific Iterations: It allows you to skip certain iterations based on a condition without breaking out of the entire loop.
Control Flow: It helps in controlling the flow of the loop more precisely, making the code cleaner and easier to read.

'''
# Example 

for i in range(10):
    if i % 2 == 0: 
        continue    
    print(i)       
