import re

ini_str = 'GeeksForGeeks'

res_list = [s for s in re.split("([A-Z][^A-Z]*)", ini_str) if s]

print(str(res_list))

