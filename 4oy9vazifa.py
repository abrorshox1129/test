# timeimport time
# from threading import Thread
#
#
#
# def ll(num):
#     x = 0
#     for i in num:
#         x+=int(i)
#     print(x)
#
# start = time.time()
#
# th1 = Thread(target=ll,args=("108",))
# th2 = Thread(target=ll,args=("108",))
# th3 = Thread(target=ll,args=("108",))
#
# th1.start()
# th2.start()
# th3.start()
#
# th1.join()
# th2.join()
# th3.join()
#
# end = time.time()
#
# print(f"Jarayon {round(end - start,2)} vaqt davom etdi.")
# --------------------------------------------------------------------
# 2-misol
# import time
# from threading import Thread
#
# a = int(input("Sekundni kiritng: "))
#
# def ll(sekund:int):
#     kun = sekund // 86400
#     sekund %= 86400
#     soat = sekund // 3600
#     sekund %= 3600
#     minut =sekund // 60
#     sekund %= 60
#     soniya = sekund
#     print(f"{kun} kun {soat} soat {minut} minut {soniya} sekund")
#
#
#
#
#
#
# start = time.time()
#
# th1 = Thread(target=ll,args=(a,))
# th2 = Thread(target=ll,args=(a,))
# th3 = Thread(target=ll,args=(a,))
#
# th1.start()
# th2.start()
# th3.start()
#
# th1.join()
# th2.join()
# th3.join()
#
# end = time.time()
#
# print(f"Jarayon {round(end - start,2)} vaqt davom etdi.")

# --------------------------------------------------------------------
# 3-misol

# import time
# from threading import Thread
#
#
# a = ['alfred', 'tabitha', 'william', 'arla']
# def letter(l:list):
#     a = list(map(str.title,l))
#     print(a)
#
#
# start = time.time()
#
# th1 = Thread(target=letter,args=(a,))
# th2 = Thread(target=letter,args=(a,))
# th3 = Thread(target=letter,args=(a,))
#
# th1.start()
# th2.start()
# th3.start()
#
# th1.join()
# th2.join()
# th3.join()
#
# end = time.time()
#
# print(f"Jarayon {round(end - start,2)} vaqt davom etdi.")
# -------------------------------------------------------------
# 4-misol
# import time
# from threading import Thread
#
#
# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
#
# def letter(l):
#    xx = []
#    for i in l:
#        if i > 75:
#            xx.append(i)
#    print(xx)
#
#
# start = time.time()
#
# th1 = Thread(target=letter,args=(scores,))
# th2 = Thread(target=letter,args=(scores,))
# th3 = Thread(target=letter,args=(scores,))
#
# th1.start()
# th2.start()
# th3.start()
#
# th1.join()
# th2.join()
# th3.join()
#
# end = time.time()
#
# print(f"Jarayon {round(end - start,2)} vaqt davom etdi.")
# -------------------------------------------------------------------
# 5-misol
# import time
# from threading import Thread
#
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom','Non']
#
# def letters(l):
#     words = []
#     for i in l:
#         if i.lower() == i.lower()[::-1]:
#             words.append(i)
#     print(words)
#
#
#
# start = time.time()
#
# th1 = Thread(target=letters,args=(words,))
# th2 = Thread(target=letters,args=(words,))
# th3 = Thread(target=letters,args=(words,))
#
# th1.start()
# th2.start()
# th3.start()
#
# th1.join()
# th2.join()
# th3.join()
#
# end = time.time()
#
# print(f"Jarayon {round(end - start,2)} vaqt davom etdi.")
# -----------------------------------------------------------------------
# 6-misol
# import time
# from threading import Thread
#
# words = input()
#
# def letters(word):
#     i = 0
#     l = ""
#     while i<len(word):
#         harf = word[i]
#         if harf == 'e':
#             harf = 3
#             l += str(harf)
#
#         else:l += harf
#         i+=1
#     print(l,sep="")
#
#
#
#
# start = time.time()
#
# th1 = Thread(target=letters,args=(words,))
# th2 = Thread(target=letters,args=(words,))
# th3 = Thread(target=letters,args=(words,))
#
# th1.start()
# th2.start()
# th3.start()
#
# th1.join()
# th2.join()
# th3.join()
#
# end = time.time()
#
# print(f"Jarayon {round(end - start,2)} vaqt davom etdi.")
# -------------------------------------------------------------------------
# 7-misol
# import time
# from threading import Thread
# from threading import Thread
#
# words = input()
#
# def letters(word):
#     i = 0
#     x =""
#     while i<len(word):
#
#         harf = word[i]
#         if harf == ' ':
#             del harf
#
#         else:
#           x+=harf
#         i+=1
#     print(x, sep="")
#
#
#
# start = time.time()
#
# th1 = Thread(target=letters,args=(words,),)
# th2 = Thread(target=letters,args=(words,))
# th3 = Thread(target=letters,args=(words,))
#
# th1.start()
# th2.start()
# th3.start()
#
# th1.join()
# th2.join()
# th3.join()
#
# end = time.time()
#
# print(f"Jarayon {round(end - start,2)} vaqt davom etdi.")
# -------------------------------------------------------------------------------
# 8-misol
from concurrent.futures import ThreadPoolExecutor




def nums(num:list):
        return num ** 2




with ThreadPoolExecutor() as exsecuter:
    raqamlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
    res = exsecuter.map(nums,raqamlar)
    print(list(res))


# ------------------------------------------------------------------------------
# 9-misol
# import time
# from threading import Thread
# import random
#
# raqamlar = [1,2,3,4,5,6,7,8,9,9]
#
# def nums():
#     print(random.randint(0,9999))
#
#
#
# start = time.time()
#
# th1 = Thread(target=nums)
# th2 = Thread(target=nums)
# th3 = Thread(target=nums)
# th4 = Thread(target=nums)
# th5 = Thread(target=nums)
# th6 = Thread(target=nums)
# th7 = Thread(target=nums)
# th8 = Thread(target=nums)
# th9 = Thread(target=nums)
# th10 = Thread(target=nums)
#
# th1.start()
# th2.start()
# th3.start()
# th4.start()
# th5.start()
# th6.start()
# th7.start()
# th8.start()
# th9.start()
# th10.start()
#
# th1.join()
# th2.join()
# th3.join()
# th4.join()
# th5.join()
# th6.join()
# th7.join()
# th8.join()
# th9.join()
# th10.join()
#
#
# end = time.time()
#
# print(f"Jarayon {round(end - start,2)} vaqt davom etdi.")



























