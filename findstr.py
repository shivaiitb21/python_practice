def count_substring(s, sub):
    return [s[i:i+len(sub)] for i in range(len(s))].count(sub)