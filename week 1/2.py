

ob1 = Solution()
print(ob1.reverseOnlyLetters("bcdfghjklmnpqrstvwxyz"))

myConsonant = input("consonant only:\n\n")
myConsonantSanEspace = myConsonant.swapcase()
print(myConsonantSanEspace)


class Solution:
   def reverseOnlyLetters(self, S):
      if not S:
         return S
      str_= ""
      index_1 = 0
      index_2 = len(S)-1
      while index_1<len(S):
         #print(index1,index2)
         if index_2>=0 and S[index_1].isalpha() and S[index_2].isalpha():
            str_+=S[index_2]
            index_2 -= 1
            index_1 += 1
         elif S[index_1].isalpha():
            index_2-=1
         elif not S[index_1].isalpha():
            str_+=S[index_1]
            index_1+=1
         else:
            index_2 -= 1
            index_1 += 1
      return str_
ob1 = Solution()
print(ob1.reverseOnlyLetters("abcdefghijklmnopqrstwxyz"))
