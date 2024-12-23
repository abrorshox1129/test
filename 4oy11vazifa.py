import asyncio
#
# async def parolni_tozalash():
#     a = 'scs213qwed23e'
#     i = 0
#     x = ""
#     while len(a) > i:
#         if a[i].isdigit():
#             i += 1
#             continue
#         else:
#             x += a[i]
#         i += 1
#     print(x)
#
# async def parolni_tozalash2():
#     a = 'scs213qwed23e'
#     i = 0
#     x = ""
#     while len(a) > i:
#         if a[i].isdigit():
#             i += 1
#             continue
#         else:
#             x += a[i]
#         i += 1
#     print(x)
#
#
# async def parolni_tozalash3():
#     a = 'scs213qwed23e'
#     i = 0
#     x = ""
#     while len(a) > i:
#         if a[i].isdigit():
#             i += 1
#             continue
#         else:
#             x += a[i]
#         i += 1
#     print(x)
#
#
#
# async def main():
#     await asyncio.gather(parolni_tozalash(),parolni_tozalash2(),parolni_tozalash3())
#
# asyncio.run(main())

# --------------------------------------------------------------
# 2-misol

#
# async def matnni_qirqish1():
#     a = 'Assalomu alaykum'
#     i = 0
#     x = ""
#     while  i < 11:
#         x += a[i]
#         i += 1
#     print(x)
#
# async def matnni_qirqish2():
#     a = 'Assalomu alaykum'
#     i = 0
#     x = ""
#     while  i < 11:
#         x += a[i]
#         i += 1
#     print(x)
#
# async def matnni_qirqish3():
#     a = 'Assalomu alaykum'
#     i = 0
#     x = ""
#     while  i < 11:
#         x += a[i]
#         i += 1
#     print(x)
#
# async def main():
#     await asyncio.gather(matnni_qirqish1(),matnni_qirqish2(),matnni_qirqish3())
#
# asyncio.run(main())

# --------------------------------------------------------------
# 3-misol
# async def ismni_tozalash():
#     a = 'abrorjon0415'
#     i = 0
#     x = ""
#     while len(a) > i:
#         if a[i].isdigit():
#             i += 1
#             continue
#         else:
#             x += a[i]
#         i += 1
#     print(x.title())
#
# async def ismni_tozalash2():
#     a = 'abrorjon0415'
#     i = 0
#     x = ""
#     while len(a) > i:
#         if a[i].isdigit():
#             i += 1
#             continue
#         else:
#             x += a[i]
#         i += 1
#     print(x.title())
#
#
# async def ismni_tozalash3():
#     a = 'abrorjon0415'
#     i = 0
#     x = ""
#     while len(a) > i:
#         if a[i].isdigit():
#             i += 1
#             continue
#         else:
#             x += a[i]
#         i += 1
#     print(x.title())
#
#
#
# async def main():
#     await asyncio.gather(ismni_tozalash(),ismni_tozalash2(),ismni_tozalash3())
#
# asyncio.run(main())

# --------------------------------------------------------------
# 4-misol
#
# async def matinni_tozalash1():
#     a = 'sJBj kBJB jbJBJKbj'
#     i = 0
#     x = ""
#     while len(a) > i:
#         if a[i].isupper():
#             x += a[i].lower()
#         elif not a[i].isspace():
#             x += a[i]
#         i += 1
#     print(x.strip())
#
# async def matinni_tozalash2():
#     a = 'sJBj kBJB jbJBJKbj'
#     i = 0
#     x = ""
#     while len(a) > i:
#         if a[i].isupper():
#             x += a[i].lower()
#         elif not a[i].isspace():
#             x += a[i]
#         i += 1
#     print(x.strip())
#
# async def matinni_tozalash3():
#     a = 'sJBj kBJB jbJBJKbj'
#     i = 0
#     x = ""
#     while len(a) > i:
#         if a[i].isupper():
#             x += a[i].lower()
#         elif not a[i].isspace():
#             x += a[i]
#         i += 1
#     print(x.strip())
#
#
#
# async def main():
#     await asyncio.gather(matinni_tozalash1(),matinni_tozalash2(),matinni_tozalash3())
#
#
# asyncio.run(main())

# --------------------------------------------------------------
# 5-misol
#
# async def unli_harf():
#     x = 'salom dunyo'
#     y = ""
#     i = 0
#     while len(x) > i:
#         if x[i].lower() in ['a','i','u','e','o']:
#             y += x[i]
#             i += 1
#
#         else:
#             i += 1
#             continue
#     print(y)
#
# async def unli_harf2():
#     x = 'salom dunyo'
#     y = ""
#     i = 0
#     while len(x) > i:
#         if x[i].lower() in ['a','i','u','e','o']:
#             y += x[i]
#             i += 1
#
#         else:
#             i += 1
#             continue
#     print(y)
#
# async def unli_harf3():
#     x = 'salom dunyo'
#     y = ""
#     i = 0
#     while len(x) > i:
#         if x[i].lower() in ['a','i','u','e','o']:
#             y += x[i]
#             i += 1
#
#         else:
#             i += 1
#             continue
#     print(y)
#
#
# async def main():
#     await asyncio.gather(unli_harf(),unli_harf2(),unli_harf3())
#
#
# asyncio.run(main())

# --------------------------------------------------------------
# 6-misol

# async def ab():
#     i = 0
#     x = ''
#     a = 'abrorjon'
#     while len(a) > i:
#         if a[i] in ["a","A"]:
#             i +=1
#         elif a[i] in ["b","B"]:
#             x += '#'
#             i += 1
#         else:
#             x += a[i]
#             i += 1
#
#     print(x)
#
# async def ab2():
#     i = 0
#     x = ''
#     a = 'abrorjon'
#     while len(a) > i:
#         if a[i] in ["a","A"]:
#             i +=1
#         elif a[i] in ["b","B"]:
#             x += '#'
#             i += 1
#         else:
#             x += a[i]
#             i += 1
#
#     print(x)
#
# async def ab3():
#     i = 0
#     x = ''
#     a = 'abrorjon'
#     while len(a) > i:
#         if a[i] in ["a","A"]:
#             i +=1
#         elif a[i] in ["b","B"]:
#             x += '#'
#             i += 1
#         else:
#             x += a[i]
#             i += 1
#
#     print(x)
#
#
# async def main():
#     await asyncio.gather(ab(),ab2(),ab3())
#
# asyncio.run(main())


# --------------------------------------------------------------























# --------------------------------------------------------------

# 8-misol
# def filter():
#     word = "abrorjon"
#     x = len(word)//2
#     l = ''
#     i = 0
#     while len(word) > i:
#         if i == x:
#             i += 1
#             continue
#         else:
#             l += word[i]
#             i += 1
#     print(l)
#
# def filter2():
#     word = "abrorjon"
#     x = len(word)//2
#     l = ''
#     i = 0
#     while len(word) > i:
#         if i == x:
#             i += 1
#             continue
#         else:
#             l += word[i]
#             i += 1
#     print(l)
#
#
# def filter3():
#     word = "abrorjon"
#     x = len(word)//2
#     l = ''
#     i = 0
#     while len(word) > i:
#         if i == x:
#             i += 1
#             continue
#         else:
#             l += word[i]
#             i += 1
#     print(l)
#
# async def main():
#     await asyncio.gather(filter(),filter2(),filter3())
#
#
# asyncio.run(main())
# --------------------------------------------------------------
# 9-misol

# def right_to_left():
#     name = "AbrorjonA"
#     x = ''
#     i = 0
#     while len(name)>i:
#         x += name[i]
#         i += 1
#
#     if x[-1] in ["a","A"]:
#         print(x[::-1])
#
#     else:
#         print(x)
#
# def right_to_left2():
#     name = "AbrorjonA"
#     x = ''
#     i = 0
#     while len(name)>i:
#         x += name[i]
#         i += 1
#
#     if x[-1] in ["a","A"]:
#         print(x[::-1])
#
#     else:
#         print(x)
#
# def right_to_left3():
#     name = "AbrorjonA"
#     x = ''
#     i = 0
#     while len(name)>i:
#         x += name[i]
#         i += 1
#
#     if x[-1] in ["a","A"]:
#         print(x[::-1])
#
#     else:
#         print(x)
#
#
# async def main():
#     await asyncio.gather(right_to_left(),right_to_left2(),right_to_left3())
#
#
# asyncio.run(main())
#
# --------------------------------------------------------------
# 10-misol
# async def takror():
#     a = "abrorjon"
#     s = []
#     i = 0
#     while len(a)>i:
#         if a[i] in s:
#             i +=1
#             continue
#         else:
#             s.append(a[i])
#             i += 0
#     y = ""
#     for i in s:
#         y += i
#     print(y)
#
#
# async def takror2():
#     a = "abrorjon"
#     s = []
#     i = 0
#     while len(a) > i:
#         if a[i] in s:
#             i += 1
#             continue
#         else:
#             s.append(a[i])
#             i += 0
#     y = ""
#     for i in s:
#         y += i
#     print(y)
#
#
# async def takror3():
#     a = "abrorjon"
#     s = []
#     i = 0
#     while len(a) > i:
#         if a[i] in s:
#             i += 1
#             continue
#         else:
#             s.append(a[i])
#             i += 0
#     y = ""
#     for i in s:
#         y += i
#     print(y)
#
#
# async  def main():
#     await asyncio.gather(takror(),takror2(),takror3())
#
# asyncio.run(main())
#
# --------------------------------------------------------------
# 11-misol
# async def unli():
#     a = 'aiuoieae'
#     s = ''
#     i = 0
#     while len(a)>i:
#         if a[i] in ['a','i','e','o','u']:
#             s += a[i]
#             i += 1
#         else:
#             i += 1
#             continue
#
#
#     if a == s:
#         print(s.upper())
#     else:
#         pass
#
# async def main():
#     await asyncio.gather(unli(),unli(),unli())
#
# asyncio.run(main())

# --------------------------------------------------------------
# 12 - misol

from pprint import pprint
import aiohttp



async def current_weather(city_name:str):
    parametrs = {
        "q":city_name,
        "appid":'e9dce91ffe144886efd9e2b50ba648f2',
        "units":'metric'
    }
    url = "https://api.openweathermap.org/data/2.5/weather?"
    async with aiohttp.ClientSession() as session:
        async with session.get(url,params=parametrs) as response:
            data = await response.json()

            temp = data['main']['temp']
            description = data['weather'][0]["description"]
            wind = data['wind']['speed']
            info = f'Hozir {city_name}da havo harorati {round(temp)} C  gradus. Havo {description}. Shamol sekundiga {wind} tezlikda esmoqda.'
            print(info)


async def main():
    print("----------------------------------------------------------------------------------------------------")
    a = input("Shahar nomini kiriting: ").title()
    citys = ['Toshkent','Sirdaryo',"Farg'ona",'Namangan','Andijon','Navoiy','Samarqand','Qashqadaryo','Surxandaryo','Buxoro','Xorazm','Jizzax',]
    if a in citys:
        await asyncio.gather(current_weather(a))
    else:print("!!Shahar nomi noto'gri kiritildi!!")
    print("-----------------------------------------------------------------------------------------------------")

asyncio.run(main())




















