def a_method(): #parameters goes inside ()
    a_text = "Hello world"
    a_number = 12345
    #variable names on the left, values on the right
    print(a_text)
    return a_number

def main():
    print(a_method()) #prints 12345
main() #method(s) listed here will be executed directly 
