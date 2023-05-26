# Question 2: -
# Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
# we can remove just one character at the index in the string, and the remaining characters will occur the same
# number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .

# Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
# an explanation for the same.

# Example input 1 - s = “abc”. This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }
# Example output 1- YES
# Example input 2 - s “abcc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves
# character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }
# Example output 2 - NO

def isValid(s):
    #Calculate the frequency on each char in the string. 
    #Here key will be char and value will be freq
    char_freq = dict()
    for char in s:
        if char in char_freq: #char already present increase the freq by 1
            char_freq[char] += 1
        else: #first instance of char, intialize the value with freq 1
            char_freq[char] = 1

    #Create a set from the char_freq.values so that we can remove the duplicate frequencies
    unique_freqs = set(char_freq.values())    
    
    #Check if all frequencies are the same then return YES
    if len(unique_freqs) == 1:
        return "YES"
    #Check for more than two unique frequencies, then return NO
    ##Since no matter which char we remove, the frequency can not be same.
    if len(unique_freqs) > 2:
        return "NO"
    #If there are two frequency and there is only 1 char with frequency 1 
    # then we can remove that char to make string valid
    if list(char_freq.values()).count(1) == 1:
        return "YES"
    else: 
        #IN all other cases string is invalid
        return "NO"

#test case 1:
s = "abc"
print(isValid(s))
#output: YES
#explanation: This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }

#test case 2:
s = "abcc"
print(isValid(s))
#output: NO
#explanation: This string is not valid as we can remove only 1 occurrence of “c”. 
# That leaves character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }

#test case 3:
s = "aabbcccd"
print(isValid(s))
#output: NO
#explanation: 
# Frequencies: {'a': 2, 'b': 2, 'c': 3, 'd': 1}
# This string is not valid as no of the frequncies are more than 2 
# so no matter any char is removed the frequencies can't be same

#test case 4:
s = "aabbcdd"
print(isValid(s))
#output: YES
#explanation: 
# Frequencies: {'a': 2, 'b': 2, 'c': 1, 'd': 2}
# This string is valid as just removing char 'c' all other freuencies became same

