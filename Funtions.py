def hello_print():
    print "hello"
print hello_print()


#def hello_print():
#print hello_print()


#def hello_print():
#    print "hi"
#print hello_print()


#def hello_print():
#   print "gretting"
#print hello_print()


#def hello_return():
#   return "hello"
#print hello_return()


def hello_name():
    name = "Yenny"
    print "hello"
    return "Yenny"
print hello_name()


def hello_name():
    print "hello_name"
print hello_name()


def hello_name():
    name = "Maria"
    return "Maria"
print hello_name()


def hello_name():
    return "Maria"
print hello_name()


def partner_name():
    Maria = 77
    return "partner_name"
print partner_name()


#Funtions Part 2

def add(num1, num2):
    return num1 + num2
print add(4,5)


def subtract(num1, num2):
    return num2 - num1
print subtract(4,5)


def multiply(num1, num2):
    return num1 * num2
print multiply(4,5)


def divide(num1, num2):
    return num1 / num2
print divide(4,5)


def modulo(num1, num2):
    return num1 % num2
print modulo(4,5)


def power(base, exponent):
    return base ** exponent
print power(4,5)


def square(num):
    return power(num, 2)
print square(2)


def square(num):
    return power(num, 6)
print square(2)


def main():
    #(4+5) + (9-6)
    print add(add(4,5), subtract(9,6))

    # (12/2) - 60
    print subtract(divide(12, 2), 60)

     # 1 + 2 + 3
    print add(add(1, 2), 3)

    # (1 + 2)^2
    print square(add(1, 2))

    # (3%4) / (9*9)
    print divide(modulo(3, 4), multiply(9, 9))

    # 7 * (3+8)
    print multiply(7, add(3, 8))

    # (1+2) - 3 * (4+5)
    print subtract(add(1, 2), multiply(3, add(4, 5)))

    # 3^(2+3)
    print power(3, add(2, 3))

if __name__ == "__main__":
    print "Show the __name__ of this calculator_main.py module.", __name__
    main()
    
