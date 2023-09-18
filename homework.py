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