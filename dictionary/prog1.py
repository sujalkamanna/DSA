#generate multiple files 
import os


for i in range(0,100):
    with open(f"file{i}.py","w") as f:
        f.write("print('hello world')")
