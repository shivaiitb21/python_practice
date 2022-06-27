import time
start = time.time()

def count_substring(s, sub):

    return [s[i:i+len(sub)] for i in range(len(s))].count(sub)

print(count_substring("ABCDCDC","CDC"))
end = time.time()
print(end-start)