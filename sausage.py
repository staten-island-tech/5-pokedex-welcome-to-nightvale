""" def occupied(t,y,z):
    x = 0
    for i in range(t):
        if y[i] == "c" and z[i] == "c":
            x = x+1
    print(x)
    
        
occupied(5,"c..c..",".c.cc") """

def lang(a):
    s = 0
    t = 0
    for i in a:
        if i == "s" or i == "S":
            s = s + 1
        elif i == "t" or i == "T":
            t = t + 1
    if s >= t:
        print("French") 
    else:
        print("English")

lang("ttts")