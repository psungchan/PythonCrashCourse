alphabet = "abcdefghijklmnopqrstuvwxyz"
def main():
    alphabet_array = list(alphabet)# turn alphabet into a list of char
    letter = input("Give me an letter: ")
    position = alphabet.find(letter)
    # we need position + 1 here because lists start w/ index 0
    print("the letter",letter,"is no.",str(position + 1),"in the alphabet.")
    
main()
    