# 부분 문자열

#####################
#      기본풀이      #
#####################
import sys
input = sys.stdin.readline

text = input().rstrip()
check = input().rstrip()

if check in text :
    print(1)
else :
    print(0)



#####################
#     KMP 사용      #
#####################
import sys
input = sys.stdin.readline
