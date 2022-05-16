# -*- coding: utf-8 -*-
"""level01(12_15).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17N_2-08uZGdQm3HHxjL_HZZneTVllcZD

# 12.정수 내림차순으로 배치하기
"""

def solution(n):
  n = list(str(n))
  n.sort(reverse=True)
  return int(''.join(n))

n = 118372

n = list(str(n))
n.sort(reverse=True)
int(''.join(n))

solution(118372)

"""- 다른 사람 풀이"""

def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))

solution(118372)

"""# 13.자연수 뒤집어 배열로 만들기"""

def solution(n):
  return list(map(int, reversed(str(n))))

n = 123554

n = list(str(n))
n.reverse()

n = str(n)
n = n.reverse()
n = list(map(int(n)))

solution(123554)

"""# 14.자릿수 더하기"""

# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수
def solution(n):
  return sum([int(i) for i in str(n)])

# 메모장
n = 123

n = str(n)

# len(n)

lst = []
for i in n:
  lst.append(int(i))

lst
sum(lst)

n=123
sum([int(i) for i in str(n)])

"""# 15.이상한 문자 만들기"""

# 문자열 s는 한 개 이상의 단어
# 각 단어는 하나 이상의 공백문자로 구분
# 각 단어의 짝수번째 알파벳은 대문자, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution

def solution(s):
  s = s.split(' ')
  lst = []

  for i in range(len(s)):
    result = ''
    for j in range(len(s[i])):
      if j % 2 == 0:
        result += s[i][j].upper()

      else:
        result += s[i][j].lower()

    lst.append(result)

  return ' '.join(lst)

s = "try hello world"

for i in range(len(s)):
  if i % 2 == 0:
    s[i].upper()
  
  # else:
  #   s[i].lower()

s

s = "try hello world"

s = s.split(' ')
lst = []

for i in range(len(s)):
  result = ''
  for j in range(len(s[i])):
    if j % 2 == 0:
      result += s[i][j].upper()

    else:
      result += s[i][j].lower()

  lst.append(result)

' '.join(lst)

