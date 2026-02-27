def occupied(t,y,z):
    x = 0
    for i in range(t):
        if y[i] == "c" and z[i] == "c":
            x = x+1
    print(x)
    
        
occupied(5,"c..c..",".c.cc")