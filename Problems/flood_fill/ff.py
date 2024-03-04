'''
An image is represented by an m x n integer grid image where image[i][j] 
represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a 
flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels 
connected 4-directionally to the starting pixel of the same color as the 
starting pixel, plus any pixels connected 4-directionally to those pixels 
(also with the same color), and so on. Replace the color of all of the 
aforementioned pixels with color.

Return the modified image after performing the flood fill.
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        old = image[sr][sc]
        if old != color:
            self.helper(image, sr, sc, old, color)
        return image

    def helper(self, image, i, j, old, new):
        if i < 0 or i > len(image) - 1:
            return
        if j < 0. or j > len(image[0]) - 1:
            return
        if image[i][j] != old:
            return
        else: 
            image[i][j] = new

            self.helper(image, i, j - 1, old, new)
            self.helper(image, i, j + 1, old, new)
            self.helper(image, i - 1, j, old, new)
            self.helper(image, i + 1, j, old, new)

# Runtime: 61 ms -- beats 88.16% of users with Python3
# Memory: 16.67 mb -- beats 83.17% of users with Python3