def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others= n-2)


s = likes(["ram", "shyam", "himanshu"])
s1 = likes(["ram", "shyam"])
s2 = likes(["himanshu"])
s3 = likes(["ram", "shyam", "himanshu", "arsh"])
s4 = likes(["ram", "shyam", "himanshu", "arsh", "abhi"])
s5 = likes(["ram", "shyam", "himanshu", "arsh", "abhi", "akshat"])

print(f'{s}\n{s1}\n{s2}\n{s3}\n{s4}\n{s5}')