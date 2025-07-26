'''Given a list of integers and a target value, write a function to 
find two numbers in the list that add up to the target. Return their indices. 
If no such pair exists, return None. nums = [7, 3, 2, 4, 6] target = 9'''

def find_two_number_indecis(nums, target):
    hm = {}

    for i, num in enumerate(nums): #2, 2
        if num in hm:
            return hm[num], i
        diff = target - num  # 2
        hm[diff] = i  #{2: 0, 6: 1}
    return None
    
    
print(find_two_number_indecis([7, 3, 2, 4, 6], 9))  #0, 2   
print(find_two_number_indecis([7, 3, 2, 4, 6], 4))  #0, 2   