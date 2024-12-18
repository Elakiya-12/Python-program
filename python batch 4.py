#enter  a sentence differentiate capital and small letters in the sentence and print it 
def sentence_case(sentence):
    capital_letters = 0
    small_letters = 0

    for s in sentence:
        if s.isupper():
            capital_letters += 1
        elif s.islower():
            small_letters += 1
    print("Capital letters:", capital_letters)
    print("Small letters:", small_letters)

# Example usage
sentence = input("Enter the sentence: ")
sentence_case(sentence)

#palindrome 
def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        print(f"The string {string} is a palindrome.")
    else:
        print(f"The string {string} is not a palindrome.")
s = input("Enter a string: ")
is_palindrome(s)
    
    
