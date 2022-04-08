"""Find palindromes (letter palingrams) in a dictionary file with recursion."""
import load_dictionary
word_list = load_dictionary.load('2of4brif.txt')
pali_list = []

flag = True

def findPalindrome(word):
# Recursive function to find palindrome word
    #have to use global keyword to change the global flag value
    global flag
    #this is here to make sure the word on line 18 don't go out of index
    if len(word) < 2:
        return flag
    if flag == False:
        return flag
    else:
        if word[0]==word[-1]:
            word = word[1:-1]
            return findPalindrome(word)
        else:
            flag = False
            return findPalindrome(word)

for word in word_list:
 if len(word) > 1 and findPalindrome(word) == True:
    pali_list.append(word)
 else:
    #reset the global flag back to True 
    flag = True
print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')