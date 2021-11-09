import textwrap

def wrap(string,value):
    return textwrap.fill(string,value)

result=wrap("abcdefghijklmnopqrstuvwxyz",6)
print(result)