# ls = [1,6,8,4,64,8,0,75,4,26,4,6,75]

# # for i in ls:
# #     print(ls)

# def length(ls):
#     count = 0
#     for i in ls:
#         count+=1

#     return count 

# ls1 = [1,2,3,4,5,6,7,8]
# ls2 = [7,6,5,4,3,2,1]

# print(length(ls2))

# def maximum(sid):
#     max=0
#     for i in sid:
#         if i > max:
#             max = i

#     return max

# ls=[1,2,3,4,5,6,7,8,9,0]
# print(maximum(ls)) 
     
def minimum(sid):
    min=100
    for i in sid:
        if i < min:
            min = i

    return min

ls=[1,2,3,4,5,6,7,8,9,0]
print(minimum(ls)) 
     