"""
Question: { Big Q***. Refer PDF for it }
"""

""" 
{ Don't write this Part this is only for references }

- Before Going to write this program, name is file as "copfile.py"
- Create an Text name named as "input.txt", and write something you wish
"""

with open("input.txt", "r") as input:
    with open("output.txt", "w") as output:
        for line in input:
            output.write(line)
        output.write("JOB DONE!!")


"""
OUTPUT:
----

- There is no ouput is displayed in Ouput Terminal
- In File Directory you will see a new file named as "output.txt"
- In content in "output.txt" is copied from "input.txt" ( Where you write something )

"""