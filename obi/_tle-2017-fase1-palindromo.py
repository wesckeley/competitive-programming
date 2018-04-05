# https://techiedelight.quora.com/500-Data-Structures-and-Algorithms-practice-problems-and-their-solutions
# http://www.techiedelight.com/find-minimum-cuts-needed-palindromic-partition-string/

is_palindrome = []
n = 0

#
def find_palindromes(str):
    global is_palindrome, n

    for i in range(0,n):
        is_palindrome.append([])
        for j in range(0,n):
            is_palindrome[i].append(False)

    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if i == j:                
                is_palindrome[i][j] = True
            elif str[i] == str[j]:
                is_palindrome[i][j] = True if j - i == 1 else is_palindrome[i+1][j-1]
            else:
                is_palindrome[i][j] = False

#
def min_palindrome_cuts(str):
    global is_palindrome, n
    
    dp = [0x1FFFFFFF for i in range(0,n)]

    for i in range(n-1,-1,-1):

        dp[i] = 0x1FFFFFFF

        if is_palindrome[i][n-1] == True:
            dp[i] = 0
        else:
            for j in range(n-2,i-1,-1):
                if is_palindrome[i][j]:
                    dp[i] = min(dp[i],dp[j+1]+1)
                    
    return dp[0]

n = int(input())
str = input()

find_palindromes(str)
print(min_palindrome_cuts(str) + 1)