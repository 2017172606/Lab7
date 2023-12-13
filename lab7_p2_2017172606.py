with open('input_7_2.txt', 'r') as f:
    content = f.read()

element = {}

for char in content:
    if char.isalpha(): # 파일에 !, -- 같은 특수문자도 있음.
        char = char.upper() # 대소문자 구분 X
        if char not in element:
            element[char] = 0
        element[char] += 1

char_list = list(element.items())


char_list.sort(key=lambda x: (-x[1], x[0]))
# descending order, (알파벳,등장횟수) tuple 에서 등장횟수를 우선으로,
# 그다음에 알파벳은 사전순으로 정렬. 기본적으로 ascending order 인것을 감안할 때
# 횟수값에 -를 붙여서 정렬하면 곧 가장 많이 나온 것이 맨 뒤로 가게 되므로 자동으로 내림차순 정렬
# 그 다음의 기준은 사전식 정렬이므로 x[0]

# 튜플에서 알파벳만 가져오기
char_list = [item[0] for item in char_list]

print(char_list)
