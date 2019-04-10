"""
    You are given a string S and width W. 
    Your task is to wrap the string into a paragraph of width W.
"""
import textwrap
# This function wraps the input single paragraph in text, 
# and returns a single string containing the wrapped paragraph
def wrap(string, max_width): 
    wrapper = textwrap.TextWrapper(width = max_width)
    
    # returns the data joined into a single, newline-separated string
    s = wrapper.fill(string)
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
