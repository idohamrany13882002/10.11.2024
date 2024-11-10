counter: int = 10

def inc_counter():
    global counter
    counter+=1

def dec_counter():
    global counter
    counter-=1

def print_counter():
    print(counter)

def int_local_counter():
    counter: int = 20
    return counter

def __main__():
    for _ in range (3):
        inc_counter()
    for _ in range (2):
        dec_counter()
    print_counter()
    print(int_local_counter())

if __name__ == "__main__":
    __main__()