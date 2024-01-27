from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startin_color = image[sr][sc]
        colored = set()
        self.color_image(image, sr, sc, color, colored, startin_color)
        return image

    def color_image(self, image, sr, sc, color, colored, startin_color):
        image[sr][sc] = color
        colored.add((sr, sc))
        neighbors = [(sr+1, sc), (sr-1, sc), (sr, sc+1), (sr, sc-1)]
        neignors = [(2, 1), (0, 1), (1, 2), (1,0)]
        for row, col in neighbors:
            if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == startin_color and (row, col) not in colored:
                self.color_image(image, row, col, color, colored, startin_color)