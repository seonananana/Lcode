class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # 두 트리가 서로 대칭인지 확인하는 함수
        def isMirror(left, right):

            # 둘 다 None이면 대칭
            if left is None and right is None:
                return True

            # 하나만 None이면 대칭이 아님
            if left is None or right is None:
                return False

            # 값이 다르면 대칭이 아님
            if left.val != right.val:
                return False

            # 왼쪽의 왼쪽 == 오른쪽의 오른쪽
            # 왼쪽의 오른쪽 == 오른쪽의 왼쪽
            return (
                isMirror(left.left, right.right)
                and
                isMirror(left.right, right.left)
            )

        # 루트의 왼쪽과 오른쪽부터 비교 시작
        return isMirror(root.left, root.right)