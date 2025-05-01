from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowel = ('a' , 'e' , 'i' ,'o','u')
        vowels = defaultdict(int)
        consonants = 0


        i=0
        j=0
        res = 0
        n= len(word)
        while j < n:
            if word[j] in vowel:
                vowels[word[j]] +=1
            else:
                consonants +=1
                if consonants > k:
                    while consonants > k :
                        if word[i] in vowel:
                            vowels[word[i]] -=1
                            if not vowels[word[i]]:
                                del vowels[word[i]]
                        else:
                            consonants -=1
                        i +=1
            
            if consonants ==k and len(vowels) ==5:
                res +=1
                j+=1
                while j < n and word[j] in vowels:
                    res +=1
                    j +=1
                    if j ==n:
                        while i < n and word[i] in vowel:
                            vowels[word[i]] -=1
                            if not vowels[word[i]]:
                                del vowels[word[i]]
                                break
                            else:
                                res+=1
            else:
                j+=1  

        return res


word ="iqeaouqi"
k = 2


obj =  Solution()

res =obj.countOfSubstrings(word, k)

print(res)