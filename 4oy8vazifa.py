# def daraja(num):
#     return num ** 2
#
# nums = [1,2,3,4,5,6,7,8,9]
# res = map(daraja,nums)
# print(list(res))
# -------------------------------------------
# 2-misol
# xx = ["A", "a", "B", "b", "C", "c", "D", "d"]
#
# def checkletter(l:str):
#     return l.isupper()
#
#
# ss = filter(checkletter,xx)
# print(list(ss))
# --------------------------------------------------------------------
# 3-misol
# phone_numbers = ["+998991234567", "+79454874459", "+14385001031", "+9989454874459", "+9989454874459"]
#
# def checknumber(num:str):
#     if num.startswith("+998"):
#         print(num)
#
# aa = map(checknumber,phone_numbers)
# list(aa)

# --------------------------------------------------------------------
# 4-misol

# names = ['alfred', 'tabitha', 'william', 'arla']
# res = map(str.capitalize,names)
# print(list(res))

# --------------------------------------------------------------------
# 5-misol

# def test(num:int):
#     return num > 75
#
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = filter(test,scores)
# print(list(res))

# --------------------------------------------------------------------
# 6-misol
"""bu savolda lyambda ketirilgan ekan biz hali bu narsa bilan tanish emasmiz shuning ucun bu savolni tekshirmasangiz tushunmadim savolni"""

# --------------------------------------------------------------------
# 7-misol
# letters = ['apple', 'banana', 'cherry']
#
# def uzunlik(l:str):
#     return len(l)
#
# sa = map(uzunlik,letters)
# print(list(sa))

# --------------------------------------------------------------------
# 8-misol
# r1 = ['apple', 'banana', 'cherry']
# r2 =  ['orange', 'lemon', 'pineapple']
# def plus(l1:str,l2:str):
#     return l1+l2
#
# res = map(plus,r1,r2)
# print(list(res))
# --------------------------------------------------------------------
# 9-misol
# l1 =  ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# l2 = ["Sobir", "Bakir", "Jalil", "Toxir"]
#
# def iii(ll:list,ll2:list):
#     x = ""
#     b = x+ll
#     a= x+ll2
#     return f"{b} {a}"
#
# ss = map(iii,l1,l2)
#
# print(list(ss))
# --------------------------------------------------------------------
# 10-misol
# x = ['a','s','d','e','a','a','e']
# y = input("Harf: ")
# def counter(l,el:str):
#     return el.count(el)
#
# ss = map(counter,x,y)
# print(list(ss))

# --------------------------------------------------------------------
# # 11-misol
# l1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# ss = list(set(l1) & set(l2))
# print(ss)
# --------------------------------------------------------------------
# 12-misol
# programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
#
# def toq(ll:list):
#     return ll[1::2]
#
# print(toq(programming_languages))
# --------------------------------------------------------------------
# 13-misol
# programming_languages = ['Python', 'C', 'C++', 'C#', 'Java', 'Basic', 'Kotlin', 'Pascal', 'JavaScript', 'Go', 'Dart', 'Assambler', 'Ruby', 'Rust', 'Mojo', 'Swift', 'Php']
# print(programming_languages[5::])
# --------------------------------------------------------------------
# 14-misol







# --------------------------------------------------------------------
# 15-misol
# kv = (num**2 for num in range(21))
# print(list(kv))

# --------------------------------------------------------------------
# 16-misol

# def uzunlik():
#     def inner(matn:str):
#         return len(matn)
#     return inner
#
# a = "salom dunyo"
# ss = uzunlik()
# print(ss(a))
# --------------------------------------------------------------------
# 17-misol
# def salom():
#     def inner(ism:str):
#         return f"Salom {ism}"
#     return inner
#
# x = input("Ism: ")
# aa = salom()
# print(aa(x))





