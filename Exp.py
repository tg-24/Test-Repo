def drawtriangle():
    for i in range(5,0,-1):
        print("*"*i,end=" "*(6-i)+(i*"*"))
        print()
drawtriangle()

print()
print("* * * *     *")
print("      *     *")
print("* * * * * * * ")
print("*     *")
print("*     * * * *")
