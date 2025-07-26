# li = [-3, -1, -5, -4, 0, 2, 3, 8, 5]

# # -3 + -1
# # -4

# def find_triplets(li):
#     hm = set()
#     new_li = []
#     for i in range(len(li)):
#         for j in range(i+1, len(li)):
#             req = li[i] + li[j]
#             req = req * -1
#             if req in hm:
#                 new_li.append((li[i], li[j], req))
#             hm.add(req)
#     print(new_li)
    
# find_triplets(li)

# #O(n2)


# Customer
# id, name, mob, json_doc
# 1, SAurabh, +91, {f1: 10, f2, 20}

# Feature
# customer_id(FK), feature1, 10
# customer_id(FK), feature2, 20
# customer_id(FK), feature3, 5
# customer_id(FK), feature4, 100


# cache: redis --> read through 
# "customer_id_f1": 9

# ECS

# def middleware


# Student
# id, name, score


# Department
# id, name, student_id

# top3 student by each department

# select s.name, s.score, d.id
# from student as s
# join Department as d
# on s.id = d.id
# group by d.id
# order by s.score
















































