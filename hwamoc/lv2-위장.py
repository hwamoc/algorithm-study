def solution(clothes):
  cloType = {}  # 딕셔너리 자료형(키:밸류)에 옷들을 종류별로 몇개인지 저장합니다.
  for i in clothes:
    if i[1] in cloType: # 이미 저장되어 있는 종류의 경우 +1을 해준다
      cloType[i[1]] += 1
    else:
      cloType[i[1]] = 1

  cnt = 1
  for i in cloType.values():  # 다른 종류의 옷도 선택하지 않은 경우까지 생각해서
    cnt *= (i + 1)        # (각 종류별 갯수+1)을 곱해서 경우의 수를 구한다
  return cnt - 1  # 아무것도 입지 않은 경우는 빼준다

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))

'''
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
'''