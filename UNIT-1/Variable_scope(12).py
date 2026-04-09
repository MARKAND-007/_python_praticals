#Variable scope

x = 10
def outer():
    y = 20   
    def inner():
        global x
        nonlocal y
        z = 30   
        print("Local variable z =", z)
        x = x + 5
        y = y + 5
    inner()
    print("Nonlocal variable y =", y)
outer()
print("Global variable x =", x)
