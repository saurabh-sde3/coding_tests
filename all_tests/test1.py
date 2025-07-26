# str1 = "Thisisamangoessproject"
# str2 = "Theprojectmangoess"
str1 = "Thisisamangoproject"
str2 = "Theprojectmango"


def get_longest_substring(str1, str2):
    i = 0
    j = 0
    if len(str1) < len(str2):
        new_str = str1
        other_str = str2
    else:
        new_str = str2
        other_str = str1
    max_size = 0
    left = 0
    right = 0
    while i < len(new_str):  #n
        for j in range(i + 1, len(new_str)): #n
            if new_str[i: j+1] in other_str:  #m
                new_max_size = max(max_size, j - i)
                if new_max_size != max_size:
                    left = i
                    right = j
                    max_size = new_max_size
            else:
                break
        i += 1

    return new_str[left: right+1]

#O(n^2*m)
    
print(get_longest_substring(str1, str2))