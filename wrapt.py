
import textwrap
  
value = """This function wraps the input paragraph such that each line
in the paragraph is at most width characters long. The wrap method
returns a list of output lines. The returned list
is empty if the wrapped
output has no content."""

word_list = textwrap.wrap(text=value, width=50)

for element in word_list:
    print(element)