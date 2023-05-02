# 입력유효 확인 함수 1
def val(i):
	while True:
		try:
			i = float(i)
			break
		except ValueError:
			i = input("입력이 유효하지 않습니다. 다시 입력해주세요: ")
	return i
	
# 입력유효 확인 함수 2 (선택지 입력)
def val2(i):
	while True:
		if str(i) in ['1', '2']:
			break
		else:
			i = input("입력이 유효하지 않습니다. 다시 입력해주세요: ")
	return i
	
# 변수 초기화
v1 = float(0)	# 물체1 처음속도
v2 = float(0)	# 물체2 처음속도
m1 = float(0)	# 물체1 질량
m2 = float(0)	# 물체2 질량
p1 = float(0)	# 물체1 처음운동량
p2 = float(0)	# 물체2 처음운동량
total_p = float(0)	# 운동량의 합
v1f = float(0)	# 물체1 나중속도
v2f = float(0)	# 물체2 나중속도
p1f = float(0)	# 물체1 나중운동량
p2f = float(0)	# 물체2 나중운동량
impulse1 = float(0)	# 물체1 충격량
impulse2 = float(0)	# 물체2 충격량
choice = str(1)	# 충격량 / 나중속도 입력 선택
impulse_choice = str(1)	# 충격량 입력 물체 선택
object_choice = str(1)	# 나중속도 입력 물체 선택
e = float(0)	# 반발계수
c = str(1)		# 충돌 종류

# 시작
print("반갑습니다. 운동량과 충격량 계산 프로그램입니다.")
print("물체1은 왼쪽에 있고, 물체2는 오른쪽에 있으며, 오른쪽이 +입니다.")
print("물체1과 물체2의 질량과 처음속도를 입력한 후, 둘 중 한 물체의 충격량 또는 나중속도를 입력하여 계산합니다.")
print("질량의 단위는 kg, 속도의 단위는 m/s입니다.")
print("모든 입력은 공백이나 따옴표 없이 숫자만 입력하세요.")

while True:
	
	# 질량과 처음속도 입력
	print("\n========================================")
	m1 = float(val(input("물체1의 질량: ")))
	v1 = float(val(input("물체1의 처음속도: ")))
	m2 = float(val(input("물체2의 질량: ")))
	v2 = float(val(input("물체2의 처음속도: ")))
	print("----------------------------------------")

	# 처음운동량 계산
	p1 = m1 * v1
	p2 = m2 * v2
	total_p = p1 + p2
	print("물체1의 처음운동량:", p1)
	print("물체2의 처음운동량:", p2)
	print("운동량의 합:", total_p)
	print("========================================")

	if v2 >= v1:
		print("\n두 물체가 충돌하지 않습니다.")
		continue

	# 충격량 또는 나중속도 선택
	choice = str(val2(input("\n충격량을 입력하려면 '1'를, 나중속도를 입력하려면 '2'를 입력하세요: ")))

	# 충격량 입력 선택지
	if choice == '1':
		impulse_choice = str(val2(input("\n물체1이 받은 충격량을 입력하려면 '1', 물체2가 받은 충격량을 입력하려면 '2'를 입력하세요: ")))
		
		# 물체1 충격량 입력
		if impulse_choice == '1':
			impulse1 = float(val(input("\n물체1이 받은 충격량: ")))
		
			# 각 물체 나중속도 계산
			v1f = v1 + impulse1 / m1
			v2f = v2 - impulse1 / m2
			impulse2 = -impulse1
			
		# 물체2 충격량 입력
		elif impulse_choice == '2':
			impulse2 = float(val(input("\n물체2가 받은 충격량: ")))

			# 각 물체 나중속도 계산
			v1f = v1 - impulse2 / m1
			v2f = v2 + impulse2 / m2
			impulse1 = -impulse2

	# 나중속도 입력 선택지
	elif choice == '2':
		
		# 나중속도 입력할 물체 선택
		object_choice = str(val2(input("\n물체1의 나중속도를 입력하려면 '1', 물체2의 나중속도를 입력하려면 '2'를 입력하세요: ")))

		if object_choice == '1':
			
			# 물체1 나중속도 입력
			v1f = float(val(input("\n물체1의 나중속도: ")))

			# 물체2 나중속도 계산
			v2f = (total_p - m1 * v1f) / m2

			# 물체1 충격량 계산
			impulse1 = m1 * (v1f - v1)
			
		elif object_choice == '2':
			
			# 물체2 나중속도 입력
			v2f = float(val(input("\n물체2의 나중속도: ")))

			# 물체1 나중속도 계산
			v1f = (total_p - m2 * v2f) / m1

			# 충격량 계산
			impulse1 = m1 * (v1f - v1)
			
		# 물체2 충격량
		impulse2 = -impulse1

	if v2f < v1f:
		print("\n========================================")
		print("\n!! <<충돌양상이 통상적이지 않습니다>> !!")
	
	# 각각 나중운동량
	p1f = m1 * v1f
	p2f = m2 * v2f

	# 반발계수
	e = (v2f - v1f) / (v1 - v2)
	if e == float(1):
		c = '(완전) 탄성 충돌'
	elif e == float(0):
		c = '완전 비탄성 충돌'
	else:
		c = '비탄성 충돌'

	# 출력
	print("\n========================================")
	print("물체1의 처음운동량:", p1)
	print("물체1의 처음속도:", v1)
	print("물체2의 처음운동량:", p2)
	print("물체2의 처음속도:", v2)
	print("----------------------------------------")
	print("운동량의 합:", total_p)
	print("물체1이 받은 충격량(운동량의 변화량):", impulse1)
	print("물체2가 받은 충격량(운동량의 변화량):", impulse2)
	print("충돌의 종류:", c)
	print("----------------------------------------")
	print("물체1의 나중운동량:", p1f)
	print("물체1의 나중속도:", v1f)
	print("물체1의 속도변화량:", v1f-v1)
	print("물체2의 나중운동량:", p2f)
	print("물체2의 나중속도:", v2f)
	print("물체2의 속도변화량:", v2f-v2)
	print("========================================\n")
    
	# 종료여부 확인
	cont = str(val2(input("반복하려면 '1', 종료하려면 '2'을 입력하세요: ")))
	if cont == '2':
		break