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
#print(powerToxtamuratov(2,7))



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

















 


























