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
word=input("Enter the word: ")

    
    
