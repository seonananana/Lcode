class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # target을 찾은 경우
            if nums[mid] == target:
                return mid

            # 왼쪽 구간이 정렬되어 있는 경우
            if nums[left] <= nums[mid]:

                # target이 왼쪽 정렬 구간 안에 있는 경우
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                # target이 오른쪽에 있는 경우
                else:
                    left = mid + 1

            # 오른쪽 구간이 정렬되어 있는 경우
            else:

                # target이 오른쪽 정렬 구간 안에 있는 경우
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                # target이 왼쪽에 있는 경우
                else:
                    right = mid - 1

        return -1