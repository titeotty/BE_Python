def bmi(height, weight):
    return (weight / (height/100)**2 )  
    
h, w = input('당신의 키(cm)와 몸무게(kg)는? >> ').split() 
#h, w = 169, 66
height = float(h)  
weight = float(w)
#bmi = weight / (height/100)**2  
bmi = bmi(height, weight)

print('키:%6.1f(cm), 몸무게:%5.1f(km)' % (height, weight))
if 40 <= bmi:
    print('BMI:{:5.1f} {}'.format(bmi, '고도비만'))
elif 35 <= bmi:
    print('BMI:{:5.1f} {}'.format(bmi, '중등도비만'))
elif 30 <= bmi:
    print('BMI:{:5.1f} {}'.format(bmi, '비만'))
elif 25 <= bmi:
    print('BMI:{:5.1f} {}'.format(bmi, '과체중'))
elif 18.5 <= bmi:
    print('BMI:{:5.1f} {}'.format(bmi, '정상'))
else:
    print('BMI:{:5.1f} {}'.format(bmi, '저체중'))

  