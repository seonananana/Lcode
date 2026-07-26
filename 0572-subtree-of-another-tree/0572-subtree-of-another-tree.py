class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # 두 트리가 완전히 같은지 확인하는 함수
        def isSameTree(p, q):

            # 둘 다 None이면 같은 트리
            if p is None and q is None:
                return True

            # 하나만 None이면 다른 트리
            if p is None or q is None:
                return False

            # 값이 다르면 다른 트리
            if p.val != q.val:
                return False

            # 현재 노드가 같으면
            # 왼쪽과 오른쪽도 모두 같아야 함
            return (
                isSameTree(p.left, q.left)
                and
                isSameTree(p.right, q.right)
            )

        # root가 없으면 더 이상 비교할 트리가 없음
        if root is None:
            return False

        # 현재 root부터 시작하는 트리가
        # subRoot와 같으면 True
        if isSameTree(root, subRoot):
            return True

        # 아니라면
        # 왼쪽 서브트리에서 찾기
        # 또는
        # 오른쪽 서브트리에서 찾기
        return (
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right, subRoot)
        )