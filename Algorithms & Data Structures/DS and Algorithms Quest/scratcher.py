def reverse_two_pointer(word):
    chars = list(word)

    left = 0
    right = len(chars) - 1
    
    while left < right:
        temp = chars[left]
        chars[left] = chars[right]
        chars[right] = temp
        
        left += 1
        right -= 1
        
    return "".join(chars)


print(reverse_two_pointer("rrrrssss"))

def is_palindrome(word):
    left = 0
    right = len(word) - 1
    
    while left < right:
        if word[left] != word[right]:
            return False
        
        #move pointers towards the center
        left += 1
        right -= 1
    
    return True

print(is_palindrome("racecar"))
print(is_palindrome("python"))

        