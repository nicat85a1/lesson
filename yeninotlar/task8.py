"""
# Task 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("Enter a number: "))
result = factorial(n)
print(f"The factorial of {n} is {result}")

# Task 2

def reverse_function(word):
    return word[::-1]

word = input("Enter a word: ")
reversed_word = reverse_function(word)
print(f"The reversed word is: {reversed_word}")

# Task 3.1

def sentence_function(sentence):
    words = len(sentence.split())
    return words

sentence = input("Enter a sentence: ")
print("Number of words:", sentence_function(sentence))

# Task 3.2

def sentence_function(sentence):
    print (sentence)
    res = sentence.count(" ")+1
    return res
sentence = input("Enter a sentence: ")
print ("The number of words in input are : " + str(sentence_function(sentence)))

# Task 5

def exponent_function(nums_input):
    nums = [int(num) for num in nums_input.split(',')]
    exponent = [num**3 for num in nums]
    return exponent

nums_input = input("Enter a exponent number(Separate numbers with commas.)): ")
exponent = exponent_function(nums_input)
print("The exponent of the numbers are:", exponent)
"""
# Task 4

def sentence_upper(user_input):
    sentences = user_input.split('.')
    return sentences[0].upper() + '.', sentences[1].strip()

user_input = input("Enter two sentences (separated by periods): ")
result = sentence_upper(user_input)
print(result)
