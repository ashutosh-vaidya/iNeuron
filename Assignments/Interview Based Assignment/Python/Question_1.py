# Question 1: -
# Write a program that takes a string as input, and counts the frequency of each word in the string, there might
# be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
# highest-frequency word.

# Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
# an explanation for the same.

# Example input - string = “write write write all the number from from from 1 to 100”
# Example output - 5

# Explanation - From the given string we can note that the most frequent words are “write” and “from” and
# the maximum value of both the values is “write” and its corresponding length is 5

def getHighestFrequencyWordLen(s):
    #Split the string into the list
    words = s.split()

    #Create a dictionary to save word as a key and its frequency as a value 
    word_freq = dict()
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    #Get the highest frequency
    max_freq = max(word_freq.values())

    #Fetch the max length of highest frequency word
    max_length = 0
    for word, freq in word_freq.items():
        if freq == max_freq and len(word) > max_length:
            max_length = len(word)

    return max_length

# Test Case 1
input1 = "write write write all the number from from from 1 to 100"
print(f"Test Case 1: Length of highest frequncy word is {getHighestFrequencyWordLen(input1)}")

# Explanation - From the given string we can note that the most frequent words are “write” and “from” and
# the maximum value of both the values is “write” and its corresponding length is 5

# Test Case 2
input2 = "Python is easy to learn and practice"
print(f"Test Case 2: Length of highest frequncy word is {getHighestFrequencyWordLen(input2)}")

# Explanation - In this test case there are no word are repeating hence max freuency is 1
# from all the word "practice" has max length which is 8

# Test Case 3
input3 = "Delhi Delhi is is is a a a capital capital capital of the India India"
print(f"Test Case 3: Length of highest frequncy word is {getHighestFrequencyWordLen(input3)}")

# Explanation - In this test case most frequent words are "is", "a" and "capital" with frequency 3
# "capital" has max length with value 7