import time
start = time.time()

def count_substring(string, sub_string):
    count = 0
    i = string.find(sub_string)
    while i != -1:
        count += 1
        i = string.find(sub_string, i+1)
    return count

print(count_substring("ABCDCDC","CDC"))
end = time.time()
print(end-start)