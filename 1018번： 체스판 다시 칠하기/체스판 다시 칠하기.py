#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1018                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: supporting130870 <boj.kr/u/supporting1308   +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1018                           #+#        #+#      #+#     #
#    Solved: 2024/11/13 21:00:30 by supporting1308###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

wb = ["WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW"]

bw = ["BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB"]

n,m = map(int, sys.stdin.readline().split())

board =[]
for i in range(n):
    board.append(sys.stdin.readline().strip())


#n <- 줄
#ㅡ <- 칸
minResult = float("inf")
for i in range(n-7):
    #m-8범위 문제 해결
    for j in range(m-7):
        bw_count = 0
        wb_count = 0
        
        
        for k in range(8):
            current = board[i + k][j:j + 8]
            bw_list = bw[k]
            wb_list = wb[k]
            
            for l in range(8):
                if bw_list[l] != current[l]:
                    bw_count = bw_count+1
                if wb_list[l] != current[l]:
                    wb_count = wb_count +1
        
        minResult = min(wb_count, bw_count, minResult)


print(minResult)


