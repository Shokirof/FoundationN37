def function_Shokiroff(age):
    if age <5:
        print("Siz uchun alohida bilet sotilmaydi")
    elif age > 5 and age <10:
        print("Siz uchun alohida bolalar bileti sotiladi")
    else:
        print("Ota-onayiz endi sizni olib yurmaydi chhunki bilet pullik")


def MedianOfTwoLists_function_Asrorov_1(nums1, nums2):
    nums1.extend(nums2)
    if len(nums1) % 2 == 0:
        return (sorted(nums1)[len(nums1) // 2] + sorted(nums1)[len(nums1) // 2 - 1]) / 2 
    return sorted(nums1)[len(nums1)//2]


def MukammalSon_function_Asrorov_2(num):
    lst = []
    for i in range(1, num//2 + 1):
        if num % i == 0:
            lst.append(i)

    if sum(lst) == num:
        return True
    else:
        return False



def Polindrom_function_Asrorov_3(num):
    if num == num[::-1]:
        return True
    return False


def LastWordLength_function_Asrorov_4(text):
        return len(text.split()[-1])


def Factorial_function_Asrorov_5(nums):
    lst = []
    for i in range(len(nums)):
        cnt = 1
        x = 1
        while x != nums[i]+1:
            cnt *= x
            x += 1
        lst.append(cnt)
    return lst

# 1-masala
def list_sum_Toxtamuratov(num_List):
    if len(num_List) == 1:
     return num_List[0]
    else:
     return num_List[0] + list_sum_Toxtamuratov(num_List[1:])
print(list_sum_Toxtamuratov([6,8,9,12,15,16]))

# Faktorial Rekursiya
# 2-masala
def Toxtamuratov_Faktorial(n):
 if n <= 1:
  return 1
 else:
   return n * (Toxtamuratov_Faktorial(n - 1))

#print(Toxtamuratov_Faktorial(5))

# rejursiya orqali sonning raqamlar yogindisini hisoblaydigan dastur tu
# 3-masala
def Toxtamuratovdef_sumDigits(n):
  if n == 0:
   return 0
  else:
   return n % 10 + Toxtamuratovdef_sumDigits(int(n / 10))
#print(Toxtamuratovdef_sumDigits(148))


# a ning b ning darajasini hisoblaydigan dastur
# 4-masala
def powerToxtamuratov(a,b):
    if b==0:
     return 1
    elif a==0:
     return 0
    elif b==1:
     return a
    else:
     return a*powerToxtamuratov(a,b-1)
#print(poterToxtamuratov(2,7))



# 5-masala
def ekub_Toxtamuratov(a,b):
    low = min(a, b)
    high = max(a, b)
    if low == 0:
     return high
    elif low == 1:
     return 1
    else:
     return ekub_Toxtamuratov(low, high%low)
print(ekub_Toxtamuratov(24,36))

###########################################



"""

def Qosimov_1_countKDifference(self, nums: List[int], k: int) -> int:
        cnt=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i]-nums[j]==k:
                        cnt+=1
        return cnt



def Qosimov_2_arrayStringsAreEqual(self, word1: List[str], word2:
List[str]) ->
bool:
        if ''.join(word1)==''.join(word2):
            return True
        else:
            return False


def Qosimov_3_countMatches(self, items: List[List[str]], ruleKey: str,
ruleValue: str) -> int:
        count=0
        if ruleKey=="type":
            for i in items:
                if i[0]==ruleValue:
                    count+=1
        if ruleKey=="color":
            for i in items:
                if i[1]==ruleValue:
                    count+=1
        if ruleKey=="name":
            for i in items:
                if i[2]==ruleValue:
                    count+=1
        return count


def Qosimov_4_mostWordsFound(self, sentences: List[str]) -> int:
        count=0
        for i in range(len(sentences)):
            if sentences[i].count(' ') > count:
                count=sentences[i].count(' ')
        return count+1


def Qosimov_5_kidsWithCandies(self, candies: List[int], extraCandies: int)
->
List[bool]:
        M=max(candies)
        arr = []
        for i in range(len(candies)):
            if candies[i]+extraCandies >= M:
                arr.append(True)
            else:
                arr.append(False)
        return arr




"""
#====================================================
def Behruz_function(name):
    print(f"Salom ishyoqmas kamina {name}")
    print(f"Open budjetdan soqqa qalay {name}") 

# ================================================

def Behruz_function1(a,b):
    return a ** b
a,b = map(int,input("A va B ni kiriting: ").split())
print(Behruz_function1(a,b))# a ni b inchi darajasini chiqaradi
#================================================
def Behruz_function2(a,b,c,d):
    return a*b*c*d

a,b,c,d=map(int,input("a,b,c,d ni kiriting: "))
print(Behruz_function2(a,b,c,d))
#=================================================

def Behruz_function3(a,b,s,d):
    M=a*12220.00
    print(f"Dollar kursi: {M}")
    K=b*13300.00
    print(f"Euro kursi: {K}")
    L=s*140.00
    print(f"Rubl kursi: {L}")
    G=d*15800.00
    print(f"Funt steling: {G}")
a,b,s,d=map(float,input("so'mni kiriting: ").split())
Behruz_function3(a,b,s,d)

print("Ming somdan Akajonlar\n Iltimos silardan akajonlar")
#===========================================================
def ramzem_singh(o):
    son = 1
    while son != 0:
       m = 20
       if o == m:
          print("Aka yorilibkediz")
          break
       if o > m:
          print("Yuqoriga")
       if o < m:
          print("Pastga")
       son -= 1
Son = int(input("sonni kiriting brat:"))
print(ramzem_singh(Son))

def takrorlanuvchi_ramzem(ls):
    ls = []
    for i in Num:
       x = Num.count(i)
       if x <= 1:
         ls.append(i)
    print(ls)
Num = list(map(str,input("Satrni kiriting ==> ").split())) 
takrorlanuvchi_ramzem(Num,)       
def topuvchi(Num):
   for x in range(len(ls)):
      son = ls[0]
      if son == ls[x]:
         sch += 1
      return sch
N = int(input())
ls = []
sch = 0
ls.append(N)
print(topuvchi(N))

''' 
#Sobirjonov_Ilyosbek Eng uzun ketma-ketlik o'sib borishi 
def find_lis(arr):    n = len(arr) 
    lis = [1] * n 
    for i in range(1, n):        for j in range(i): 
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:                lis[i] = lis[j] + 1 
        length = max(lis) 
    return length 
 
#Sobirjonov_Ilyosbek  Shifrlash va shifrdan chiqarish 
 
import random 
def gcd(a, b):    while b != 0: 
        a, b = b, a % b    return a 
def generate_rsa_keypair(): 
    p = random_prime()    q = random_prime() 
    n = p * q 
    phi = (p - 1) * (q - 1) 
    e = random.randint(2, phi - 1)    while gcd(e, phi) > 1: 
        e = random.randint(2, phi - 1) 
    d = inverse_mod(e, phi) 
    return ((e, n), (d, n)) 
def encrypt_rsa(message, public_key): 
    e, n = public_key    return pow(message, e, n) 
def decrypt_rsa(ciphertext, private_key): 
    d, n = private_key    return pow(ciphertext, d, n) 
 
 
#Sobirjonov_Ilyosbek Farengeyt Celsiyga va teskarisi
def celsius_to_fahrenheit(celsius):    fahrenheit = (celsius * 9/5) + 32 
    return fahrenheit 
def fahrenheit_to_celsius(fahrenheit):    celsius = (fahrenheit - 32) * 5/9 
    return celsius

#Sobirjonov_ILyosbek unli harf sanovchi dastur
def count_vowels(string):    vowels = "aeiouAEIOU"
    count = 0    
    for char in string:        if char in vowels:
            count += 1    
    return count

#Sobirjonov_Ilyosbek daraja aniqlovchi
def power(x, n): 
    result = 1 
     
    for _ in range(n): 
        result *= x 
     
    return result
'''





# hello 37
'''
 ..-"""-..             
.'          '.
|   o      o   |
|      ^       |
 \    ' _ '    /
  '._.'"'._.'

  
    ..-"""-..
.'          '.
|   o      o   |
|      ^       |
 \    ' _ '    /
  '._.'"'._.'

    ..-"""-..
.'          '.
|   o      o   |
|      ^       |
 \    ' _ '    /
  '._.'"'._.'
'''

 ###########################################################################3
                                                                            #
def Abduxoliq_1(i):                                                         #
    if i>10:                                                                #
        return                                                              #
    print(i)                                                                #
    Abduxoliq_1(i+1)                                                        #
                                                                            #
                                                                            #
def Abduxoliq_2(s):                                                         #
    print("Hello",s)                                                        #
                                                                            #
def Abduxoliq_2_5(a,b):                                                     #
    print(f"{a}+{b}={a+b}")                                                 #
                                                                            #
def Abduxoliq_3(ls):                                                        #
    for i in ls:                                                            #
        print(i**2)                                                         #
                                                                            #
def Abduxoliq_4(tp):                                                        #
    ls=list(tp)                                                             #
    for i in range(len(ls)):                                                #
        ls[i]=ls[i]**2                                                      #             
    tp=tuple(ls)                                                            #
    return tp                                                               #
                                                                            #
def Abduxoliq_5(ls,ls1):                                                    #
    dc={}                                                                   #
    for i,j in zip(ls,ls1):                                                 #
        dc.setdefault(i,j)                                                  #
    return dc                                                               #
                                                                            #
                                                                            #
                                                                            #
                                                                            #
def Abduxoliq_6(ls):                                                        #
    for i in ls:                                                            #
      print(i)                                                              #
                                                                            #
    print("hello")                                                          #
                                                                            #
def Abduxoliq_7():                                                          #
   print ("Example")                                                        #
                                                                            #
                                                                            #
                                                                            #
def Tugadi(name):                                                           #
   if len(name)<5:                                                          #
      print("Qales",name)                                                   #
   else:                                                                    #
      print("Nma gap",name[0:5])                                            #
                                                                            #
                                                                            #
#############################################################################



def toq(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 1:
            if lst[i] % 2 == 0:
                sum+=lst[i]
    return sum

def ekub(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def valyuta(a):
    if a.endswith('$'):
        a=a.removesuffix('$')
        a=float(a)
        return a*12120
    elif a.endswith('R'):
        a=a.removesuffix('R')
        a=float(a)
        return a*121
    elif a.endswith('sum'):
        a=a.removesuffix('sum')
        a=float(a)
        return a*1
    else:
        return "Bizda bunday valyuta kursi yoq"









#man uygi vazifani qildm
print('hello')




#example 
































































































































































































































































































































































































































































































































































































# finish
