#파라미터 리스트로 받아서 길이는 상관없이 리스트 항목들의 평균과 합계 return값 2개를 반환하는 함수
def cal_avg_sum(num):
    if len(num) == 0:
        return 0, 0
    total = sum(num)
    avg = total / len(num)
    return avg, total

# 입력을 리스트로 변환
user_input = input("숫자들을 입력하세요: ")
user_input_list = user_input.split()

numbers = []
for item in user_input_list:
    numbers.append(int(item))

avg, total = cal_avg_sum(numbers)
print('평균 :', avg)
print('합계 :', total)
