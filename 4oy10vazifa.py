from io import BufferedReader
from multiprocessing import Process,Queue
# ----------------------------------------------
def open_file(file_name:str,mode:str,encoding:str ='utf-8') -> BufferedReader:
    file = open(file_name,mode,encoding=encoding)
    try:
        yield file

    finally:
        file.close()

# ---------------------------------------------------------
class MyOpenFile:
    def __init__(self,file_name,mode='r',encoding='utf-8'):
        self.file_name = file_name
        self.mode = mode
        self.encoding = encoding
        self.file = None


    def __enter__(self):
        self.file = open(self.file_name,self.mode,encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()





# ---------------------------------------------------
# def yigindi(nums:list):
#     i = 0
#     x = 0
#     while len(nums)>i:
#         x+=nums[i]
#         i+=1
#
#     print(x)
#
# s = [1,2,3,4,5,6,7,8,9]
#
#
# if __name__ == "__main__":
#     xx = Process(target=yigindi,args=(s,))
#     xx2 = Process(target=yigindi,args=(s,))
#     xx3= Process(target=yigindi,args=(s,))
#
#     xx.start()
#     xx2.start()
#     xx3.start()
#
#     xx.join()
#     xx2.join()
#     xx3.join()
#
# -----------------------------------------------------------------------------------
# 2-misol

# import random
# def royxat(l:list):
#     random.shuffle(l)
#     print(l)
#
#
# l = [1,2,3,4,5,6,7,8,9]
#
#
# if __name__ == "__main__":
#     pp = Process(target=royxat,args=(l,))
#     pp2 = Process(target=royxat,args=(l,))
#     pp3= Process(target=royxat,args=(l,))
#     pp4= Process(target=royxat,args=(l,))
#
#     pp.start()
#     pp2.start()
#     pp3.start()
#     pp4.start()
#
#     pp.join()
#     pp2.join()
#     pp3.join()
#     pp4.join()

# ----------------------------------------------------------------------------------------
# 3-misol

# def royxat(l:list):
#     print(f"Eng katta {max(l)} | Eng kichigi {min(l)}")
#
#
# l = [3,4,5,3,2,34,5,6]
#
#
# if __name__ == "__main__":
#     pp = Process(target=royxat,args=(l,))
#     pp2 = Process(target=royxat,args=(l,))
#     pp3= Process(target=royxat,args=(l,))
#     pp4= Process(target=royxat,args=(l,))
#
#     pp.start()
#     pp2.start()
#     pp3.start()
#     pp4.start()
#
#     pp.join()
#     pp2.join()
#     pp3.join()
#     pp4.join()


# ----------------------------------------------------------------------------------------
# 4-misol
# def search(item,l:list):
#     if l.count(item)>0:
#         print(f"{item} ro'yxatda mavjud")
#
# l = ["Ali","Vali","Laziz","Jalil"]
# x=input("Ro'yxatdan kimni qidiramiz: ")
#
#
# if __name__ == "__main__":
#     pp = Process(target=search,args=(x,l))
#     pp2 = Process(target=search,args=(x,l))
#     pp3= Process(target=search,args=(x,l))
#     pp4= Process(target=search,args=(x,l))
#
#     pp.start()
#     pp2.start()
#     pp3.start()
#     pp4.start()
#
#     pp.join()
#     pp2.join()
#     pp3.join()
#     pp4.join()
# ----------------------------------------------------------------------------------------
# 5-misol

# def ochirish(l:list):
#      print(list(set(l)))
#
# x = ["Ali","Vali","Laziz","Jalil","Ali"]
#
#
#
# if __name__ == "__main__":
#     pp = Process(target=ochirish,args=(x,))
#     pp2 = Process(target=ochirish,args=(x,))
#     pp3= Process(target=ochirish,args=(x,))
#     pp4= Process(target=ochirish,args=(x,))
#
#     pp.start()
#     pp2.start()
#     pp3.start()
#     pp4.start()
#
#     pp.join()
#     pp2.join()
#     pp3.join()
#     pp4.join()


# ----------------------------------------------------------------------------------------
# 6-misol

# def teskari(l:list,q:Queue):
#     x = []
#     for i in l:
#         x.append(i[::-1])
#     q.put(x)
#
# l = ["Ali","Vali","Laziz","Jalil"]
#
# if __name__ == "__main__":
#     q = Queue()
#     q2 = Queue()
#     q3= Queue()
#     q4= Queue()
#     pp = Process(target=teskari,args=(l,q))
#     pp2 = Process(target=teskari,args=(l,q2))
#     pp3= Process(target=teskari,args=(l,q3))
#     pp4= Process(target=teskari,args=(l,q4))
#
#     pp.start()
#     pp2.start()
#     pp3.start()
#     pp4.start()
#     print(q.get())
#     print(q2.get())
#     print(q3.get())
#     print(q4.get())
#     pp.join()
#     pp2.join()
#     pp3.join()
#     pp4.join()


# ----------------------------------------------------------------------------------------
# 7-misol

# def ddd(l:list):
#     x = 0
#     for i in l:
#         if len(i)>x:
#             x =len(i)
#     print(i)
# l = ["Ali","Vali","Laziz","Jalil","Jalilii"]
#
# if __name__ == "__main__":
#     pp = Process(target=ddd,args=(l,))
#     pp2 = Process(target=ddd,args=(l,))
#     pp3= Process(target=ddd,args=(l,))
#     pp4= Process(target=ddd,args=(l,))
#
#     pp.start()
#     pp2.start()
#     pp3.start()
#     pp4.start()
#
#     pp.join()
#     pp2.join()
#     pp3.join()
#     pp4.join()








# ----------------------------------------------------------------------------------------
# 8-misol
def raqam(d: dict,q:Queue):
    ii = []











# ----------------------------------------------------------------------------------------

# # 9-misol
# def raqam(d: dict,q:Queue):
#     ii = []
#     for i in d.values():
#         if isinstance(i, int):
#             ii.append(i)
#     q.put(ii)
#
#
#
# a = {'name':'Ali','age':19,'phone_number':9999}
#
#
# if __name__ == "__main__":
#     q = Queue()
#     q2 = Queue()
#     q3= Queue()
#     q4= Queue()
#     pp = Process(target=raqam,args=(a,q))
#     pp2 = Process(target=raqam,args=(a,q2))
#     pp3= Process(target=raqam,args=(a,q3))
#     pp4= Process(target=raqam,args=(a,q4))
#
#     pp.start()
#     pp2.start()
#     pp3.start()
#     pp4.start()
#     print(q.get())
#     print(q2.get())
#     print(q3.get())
#     print(q4.get())
#     pp.join()
#     pp2.join()
#     pp3.join()
#     pp4.join()

# -------------------------------------------------------------------------------
# 10-misol

# def raqam(d: dict,q:Queue):
#     ii = []
#     for i in d.values():
#         if isinstance(i, int):
#             ii.append(i**2)
#     q.put(ii)
#
#
#
# a = {'name':'Ali','age':19,'phone_number':9999}
#
#
# if __name__ == "__main__":
#     q = Queue()
#     q2 = Queue()
#     q3= Queue()
#     q4= Queue()
#     pp = Process(target=raqam,args=(a,q))
#     pp2 = Process(target=raqam,args=(a,q2))
#     pp3= Process(target=raqam,args=(a,q3))
#     pp4= Process(target=raqam,args=(a,q4))
#
#     pp.start()
#     pp2.start()
#     pp3.start()
#     pp4.start()
#     print(q.get())
#     print(q2.get())
#     print(q3.get())
#     print(q4.get())
#     pp.join()
#     pp2.join()
#     pp3.join()
#     pp4.join()

# -----------------------------------------------------------------------------------------
# 11-misol

# def eng_katta(d: dict):
#     kalit = None
#     x = 0.0
#     for key,value in d.items():
#         if isinstance(value, int) and value > x:
#             x = value
#             kalit = key
#
#     print(kalit)
#
# d = {'ali':12,'Vali':15,'Jalil':32}
#
# if __name__ == "__main__":
#
#     p1 = Process(target=eng_katta,args=(d,))
#     p2 = Process(target=eng_katta,args=(d,))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
# ------------------------------------------------------------------------------------------
# 12-misol
# def raqam(d: dict,q:Queue):
#     ii = []
#     for i in d.values():
#         if isinstance(i, int):
#             ii.append(i)
#     q.put(sum(ii)/len(ii))
#
#
#
# a = {'name':'Ali','age':19,'phone_number':9999}
#
#
# if __name__ == "__main__":
#     q = Queue()
#     q2 = Queue()
#     q3= Queue()
#     q4= Queue()
#     pp = Process(target=raqam,args=(a,q))
#     pp2 = Process(target=raqam,args=(a,q2))
#     pp3= Process(target=raqam,args=(a,q3))
#     pp4= Process(target=raqam,args=(a,q4))
#
#     pp.start()
#     pp2.start()
#     pp3.start()
#     pp4.start()
#     print(q.get())
#     print(q2.get())
#     print(q3.get())
#     print(q4.get())
#     pp.join()
#     pp2.join()
#     pp3.join()
#     pp4.join()

# ------------------------------------------------------------------------------------------
# 13-misol





# ------------------------------------------------------------------------------------------
# 14-misol

# def eng_katta(d: dict):
#     x = 0.0
#     for key,value in d.items():
#         if len(key)>x:
#             x=len(key)
#     ii = key
#     xx = 30
#     for key2,value2 in d.items():
#         if len(key2)<xx:
#             xx=len(key2)
#     j = key2
#     print(ii,j)
#
# a = {'name':'Ali','age':19,'phone_number':9999}
#
#
# eng_katta(a)

# ----------------------------------------------------------------
# 15-misol
# def raqam(d: dict,q:Queue):
#     ii = []
#     for i in d.values():
#         if isinstance(i, int):
#             ii.append(i)
#     q.put(ii)
#
#
#
# a = {'name':'Ali','age':19,'phone_number':9999}
#
#
# if __name__ == "__main__":
#     q = Queue()
#     q2 = Queue()
#     q3= Queue()
#     q4= Queue()
#     pp = Process(target=raqam,args=(a,q))
#     pp2 = Process(target=raqam,args=(a,q2))
#     pp3= Process(target=raqam,args=(a,q3))
#     pp4= Process(target=raqam,args=(a,q4))
#
#     pp.start()
#     pp2.start()
#     pp3.start()
#     pp4.start()
#     print(q.get())
#     print(q2.get())
#     print(q3.get())
#     print(q4.get())
#     pp.join()
#     pp2.join()
#     pp3.join()
#     pp4.join()

# ----------------------------------------------------------------------
# 16-misol
# def new_dict(d:dict):
#     a = {}
#     for keys,value in d.items():
#         a[f"{keys}"]=value*2
#
#     print(a)
#
# x = {'name':'Ali','age':19,'phone_number':9999}
#
# if __name__ == "__main__":
#     pr = Process(target=new_dict,args=(x,))
#     pr2 = Process(target=new_dict,args=(x,))
#
#     pr.start()
#     pr2.start()
#
#     pr.join()
#     pr2.join()


# ----------------------------------------------------------------------
# 17-misol
#
# def teskari_str(d: dict, q: Queue):
#     ii = []
#     for key, value in d.items():
#         if isinstance(value, str):
#             ii.append(value[::-1])
#     q.put(ii)
#
# x = {'name': 'Ali', 'age': 19, 'phone_number': 9999, 'name2': "Jalil"}
#
# if __name__ == "__main__":
#     q = Queue()
#     q2 = Queue()
#     pr = Process(target=teskari_str, args=(x, q))
#     pr2 = Process(target=teskari_str, args=(x, q2))
#
#
#     pr.start()
#     pr2.start()
#     print(q.get())
#     print(q2.get())
#     pr.join()
#     pr2.join()
#




















