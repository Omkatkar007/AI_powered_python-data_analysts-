# Local Variables

def show_value():
    x = 10
    print(x)

show_value()


# Global Variables

x = 20

def show_value():
    print(x)

show_value()



# Local vs Global Example

x = 10

def test():
    x = 5
    print(x)

test()
print(x)


# The global Keyword

x = 10

def update():
    global x
    x = 20

update()
print(x)