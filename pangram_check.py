def pangrams(s):
    # Write your code here
    sl = s.lower()
    test_set = set(sl)
    
    
    alphabet = set(string.ascii_lowercase)
    
    if test_set >= alphabet:
        return "pangram"
    
    else:
        return "not pangram"