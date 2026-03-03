
""" def occupied(t,y,z):
    x = 0
    for i in range(t):
        if y[i] == "c" and z[i] == "c":
            x = x+1
    print(x)
    
        
occupied(5,"c..c..",".c.cc") """

""" def lang(a):
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

lang("ttts") """

""" def honi(x):
    x = x.lower()
    a = 0
    b = 0
    for t in x:
        if t == "h":
            a += 1
        elif t == "o":
            a += 1
        elif t == "n":
            a += 1
        elif t == "i":
            a += 1
    if (a % 4) == 0:
        b = a / 4
    print(b)
honi("HHOOONNNIII") """

""" def honi(x):
    x = x.lower()
    a = 0
    b = 0 
    z = 0
    search = ["h", "o", "n", "i"]
    for t in x:
        if t == search[z]:
            a += 1
            z += 1
    b = math.floor(a / 4) 
    print(b)

honi("HHHONNNIIi") """


