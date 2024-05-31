# #총점을 기준으로 내림차순으로 데이터 정렬
# exLst = [('사람1', 90, 80, 70), ('사람2', 70, 70, 60), ('사람3', 90, 90, 90)]
# print(exLst)

# exLst2 = print(sorted(exLst))

# for i in exLst2 :
#     hap = sum(i[1:])
#     print(i, hap)


#시험문제

exLst = [('사람1', 90, 80, 70), ('사람2', 70, 70, 60), ('사람3', 90, 90, 90)]
print(exLst)

# 총점을 기준으로 내림차순으로 정렬
exLst2 = sorted(exLst, key=lambda x: sum(x[1:]), reverse=True)

# 정렬된 리스트 출력
print(exLst2)

# 각 항목의 총점을 출력
for i in exLst2:
    hap = sum(i[1:])
    print(i, hap)
