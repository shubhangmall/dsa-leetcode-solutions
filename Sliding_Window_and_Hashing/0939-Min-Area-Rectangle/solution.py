class Solution:
    # time: O(n^2) - nested loops through points
    # space: O(n) - set for points
    def minAreaRect(self, points: List[List[int]]) -> int:
        # store all points in a hashset so we can check if a point exists in O(1)
        point_set = set()
        # go through each point in the list
        for point in points:
            # add the point as a tuple so it can be stored in a set
            point_set.add((point[0], point[1]))

        # start with infinity so any real area we find will be smaller
        min_area = float('inf')

        # pick every pair of points as potential diagonal corners
        for i in range(len(points)):
            # j starts at i+1 so we don't check the same pair twice
            for j in range(i + 1, len(points)):
                # get the x and y of the first diagonal corner
                x1, y1 = points[i]
                # get the x and y of the second diagonal corner
                x2, y2 = points[j]

                # skip if the two points share the same x or y
                # they can't form a rectangle diagonal if they do
                if x1 == x2 or y1 == y2:
                    continue

                # check if the other two corners of the rectangle exist
                # (x1,y2) is top left or bottom left corner
                # (x2,y1) is top right or bottom right corner
                if (x1, y2) in point_set and (x2, y1) in point_set:
                    # calculate the area of this rectangle
                    area = abs(x2 - x1) * abs(y2 - y1)
                    # update minimum area if this one is smaller
                    min_area = min(min_area, area)

        # if no rectangle was found return 0 otherwise return minimum area
        return 0 if min_area == float('inf') else min_area