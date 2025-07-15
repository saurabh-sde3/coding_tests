"""
# Case 1:
inputs:
    "pikachu", "togepi"
output:
    ["p", "i"]
    
# Case 2:
inputs:
    "arbitrary", "lemon"
output:
    []

# Case 3:
inputs:
    "testimonial", "ants"
output:
    ["a","n","t","s"]

# Case 4:
inputs:
    "ants", "testimonial"
output:
    ["t","s","n","a"]

"""

def get_common_chars(str1, str2):
    d1 = {}

    for ch in str1:
        d1[ch] = True
    li = []
    for ch in str2:
        if d1.get(ch):
            d1.pop(ch)
            li.append(ch)
        
    print(li)
    

get_common_chars("pikachu", "togepi")
get_common_chars("arbitrary", "lemon")
get_common_chars("testimonial", "ants")
get_common_chars("ants", "testimonial")
 