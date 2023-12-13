import re


with open("input_7_1.txt", 'r') as file:
    lines = file.readlines()

pattern = re.compile(r'\bdef\b') # def가 문자열의 일부로 사용된 것들 제외

func_dict = {}

for i, line in enumerate(lines, 1):
    if pattern.search(line):
        func_name = line.strip().split()[1].split('(')[0] # def a(n) 일 경우, 개행문자 제거후 split() 하면 ['def', 'a(n)'], 여기서
        # [1] 을 선택한 다음 '(' 로 split 하면 첫번쨰 element는 함수명.
        func_dict[func_name] = {'def': i, 'calls': []}

for i, line in enumerate(lines, 1):
    for func in func_dict.keys():
        if func + '(' in line and i != func_dict[func]['def']: # 정의된 함수가 호출 되었을 경우, 그러나, i가 def 라인이 아닌 것들
            func_dict[func]['calls'].append(i)

for func, info in func_dict.items():
    print(f"{func}: def in {info['def']}, calls in {info['calls']}")
