# Longest common subsequnce
class UserMainCode(object):
    @classmethod
    def lCS(cls, input1, input2):
      m = len(input1)
      n = len(input2)
      L = [[None] * (n+1) for i in range(m+1)]
      print(L)
      for i in range(m+1):
         for j in range(n+1):
            if i == 0 or j ==0:
               L[i][j] = 0
            elif input1[i-1] == input2[j-1]:
               L[i][j] = L[i-1][j-1]+1
            else:
               L[i][j] = max(L[i-1][j], L[i][j-1])
      cls = L[m][n]
      return cls

input1 = "FOGYA"
input2 = "GXTXAYB"
lcs = UserMainCode().lCS
print(lcs(input1, input2))