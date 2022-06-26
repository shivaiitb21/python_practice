import textwrap
string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4

def wrap(string, max_width):
    
    word_list = textwrap.wrap(text=string, width=max_width)
    print(word_list)
    for i in word_list:
        print(i)
    
wrap(string, max_width)
    