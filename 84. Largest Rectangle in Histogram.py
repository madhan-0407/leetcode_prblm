from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        list_of_rectangle = []
        heightest_length = max(heights)
        for i in heights:
            list_of_rectangle.append(set(range(1, i + 1)))

        # Make separate copies so modifying one doesn't affect the other
        list_of_rectangle1 = list_of_rectangle.copy()
        list_of_rectangle2 = list_of_rectangle.copy()
        while True:
            if not list_of_rectangle1:
                break
            all_intersect = set.intersection(*list_of_rectangle1)
            if len(all_intersect) * len(list_of_rectangle1) > heightest_length:
                heightest_length = len(all_intersect) * len(list_of_rectangle1)
            '''if len(list_of_rectangle1) == 1:
                break'''
            # Remove last element (since max(set) won't work meaningfully)
            list_of_rectangle1.pop()

        while True:
            if not list_of_rectangle2:
                break
            all_intersect = set.intersection(*list_of_rectangle2)
            if len(all_intersect) * len(list_of_rectangle2) > heightest_length:
                heightest_length = len(all_intersect) * len(list_of_rectangle2)
            '''if len(list_of_rectangle2) == 1:
                break'''
            # Remove first element (since min(set) won't work meaningfully)
            list_of_rectangle2.pop(0)
        for i in range(len(list_of_rectangle)-1):
            set1=list_of_rectangle[i]
            set2=list_of_rectangle[i+1]
            set3=set1.intersection(set2)
            if len(list(set3))>heightest_length:
                return heightest_length


        return heightest_length


print(Solution().largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))
