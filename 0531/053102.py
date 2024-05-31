import modules.m053101 as mmm

result = mmm.sum(2, 3, 1.5, "동양", 6, 3.3, "미래")

print("result type은", type(result))
print("result의 데이터 항목의 개수는", len(result))
print(f'정수의 합계는 {result[0]}, 실수의 합계는 {result[1]}, 문자열의 합은 {result[2]}')