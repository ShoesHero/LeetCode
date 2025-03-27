import math
from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def get_slope(x1,y1, x2, y2):
            if x1 == x2:
                return math.inf

            return (y2 - y1)/(x2 - x1)

        ans = 1
        for i, point1 in enumerate(points):
            slopes = defaultdict(int)
            for point2 in points[i+1:]:
                slope = get_slope(point1[0], point1[1], point2[0], point2[1])
                slopes[slope] += 1
                ans = max(ans, slopes[slope])

        return ans + 1