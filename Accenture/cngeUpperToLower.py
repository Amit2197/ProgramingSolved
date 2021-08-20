import re
def fun(cstr):
    cstr = [s for s in re.split("([A-Z][^A-Z]*)", cstr) if s]
    return ' '.join(c.lower() for c in cstr)

print(fun("TheCamel"))