class Solution:
    def largestRectangleArea(self, heights) -> int:
        maxArea = 0
        stack = []

        for index , height in enumerate(heights):
            start = index
            
            while start and stack[-1][1] > height:
                i , h = stack.pop()
                maxArea = max(maxArea , (index-i)*h)
                start = i
            stack.append((start , height))

        for index , height in stack:
            maxArea = max(maxArea , (len(heights)-index)*height)

        return maxArea

if __name__ == "__main__":
    s = Solution()
    heights = [int(x) for x in input().split()]
    print(s.largestRectangleArea(heights))

                


        