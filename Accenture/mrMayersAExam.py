# Mr. Myers and the Exam
class UserMainCode(object):
    @classmethod
    def examMarks(cls, n, arr):
        arr1=[]
        for i in arr:
            if i not in arr1:
                arr1.append(i)
            else:
                arr1.append(i+1)
        return sum(arr1)


input1 = 5
input2 = [1,2,3,4,5]
a = UserMainCode().examMarks
print(a(input1, input2))
n=5
A=[1,4,5,4,5]
print(a(n, A))