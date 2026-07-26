class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # 노드가 없으면 깊이는 0
        if root is None:
            return 0

        # 왼쪽 서브트리의 최소 깊이
        left = self.minDepth(root.left)

        # 오른쪽 서브트리의 최소 깊이
        right = self.minDepth(root.right)

        # 왼쪽 자식이 없는 경우
        # 오른쪽으로만 내려갈 수 있으므로
        # 오른쪽 깊이 + 현재 노드(1)
        if root.left is None:
            return right + 1

        # 오른쪽 자식이 없는 경우
        # 왼쪽으로만 내려갈 수 있으므로
        # 왼쪽 깊이 + 현재 노드(1)
        if root.right is None:
            return left + 1

        # 왼쪽과 오른쪽이 모두 존재하면
        # 더 짧은 경로를 선택
        return min(left, right) + 1