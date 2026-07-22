from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 각 숫자가 몇 번 나왔는지 계산
        # 예) [1,1,1,2,2,3]
        # -> Counter({1:3, 2:2, 3:1})

        count = Counter(nums)

        # most_common(k)
        # 가장 많이 나온 원소 k개를
        # (숫자, 빈도수) 형태로 반환
        #
        # 예)
        # [(1,3), (2,2)]
        #
        # 리스트 컴프리헨션으로
        # 숫자(num)만 꺼내서 리스트 생성

        return [num for num,freq in count.most_common(k)]
         