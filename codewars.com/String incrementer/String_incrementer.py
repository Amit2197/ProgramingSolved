import re
def increment_string(strng):
    e_int = re.match(".*?([0-9]+)$", strng)
    return strng[:-len(e_int.group(1))] + str(int(e_int.group(1)) + 1).zfill(len(e_int.group(1))) if e_int is not None else strng + str(1)

print(increment_string("foo"))


# def increment_string1(s):
#     number = re.findall(r'\d+', s)
#     print(number)
#     if number:
#         s_number = number[-1]
#         print(s_number)
#         s = s.rsplit(s_number, 1)[0]
#         print(s)
#         number = str(int(s_number) + 1)
#         print(number)
#         return s + '0' * (len(s_number) - len(number)) + number
#     return s + '1'


# def increment_string1(strng):
#     str1 = ""
#     dig = ""
#     for i in strng:
#         if i.isnumeric():
#             dig += i
#         else:
#             str1 += i
#     if dig == "":
#         return str1 + str(1)
#     else:
#         digit = str(int(dig) + 1)
        # return str1 +'0' * (len(dig) - len(digit))+ str(digit)



# def increment_string2(input):
#     match = re.search("(\d*)$", input)
#     if match:
#         number = match.group(0)
#         if number is not "":
#             return input[:-len(number)] + str(int(number) + 1).zfill(len(number))
#     return input + "1"

# print(increment_string1("foobar001"))