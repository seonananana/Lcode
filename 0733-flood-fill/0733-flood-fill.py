class Solution:
    def floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int
    ) -> List[List[int]]:

        # 시작 위치의 원래 색 저장
        original = image[sr][sc]

        # 이미 같은 색이면 바꿀 필요 없음
        if original == color:
            return image

        # DFS 함수
        def dfs(r, c):

            # 범위를 벗어나면 종료
            if (
                r < 0 or
                r >= len(image) or
                c < 0 or
                c >= len(image[0])
            ):
                return

            # 원래 색이 아니면 종료
            if image[r][c] != original:
                return

            # 현재 칸의 색 변경
            image[r][c] = color

            # 위
            dfs(r - 1, c)

            # 아래
            dfs(r + 1, c)

            # 왼쪽
            dfs(r, c - 1)

            # 오른쪽
            dfs(r, c + 1)

        # 시작 위치부터 DFS 수행
        dfs(sr, sc)

        # 색이 변경된 이미지 반환
        return image