#Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

#Example 1:
#Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
#Output: 6
#Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

#Example 2:
#Input: height = [4,2,0,3,2,5]
#Output: 9

#Constraints:
#n == height.length
#1 <= n <= 2 * 104
#0 <= height[i] <= 105

class Solution:
    def get_occupied(self, row: list[int]) -> int:
        first_ref=row[0]
        sum=0
        total=0
        for x in row[1:]:
            if first_ref == 0:
                if x==1:
                    first_ref =1
                sum=0
            elif first_ref == 1:
                if x == 0:
                    sum+=1
                elif x == 1:
                    total+=sum
                    sum=0
        #print("total: ", total)
        return total
    def trap(self, height: list[int]) -> int:
        max_row=max(height)
        max_col=len(height)
        #print("Max row: ",max_row," Max col: ", max_col)

        plot=[]
        #print(plot)
        mod_h = height
        for row in range(max_row):
            roww=[]
            for col in range(max_col):
                if mod_h[col]>0:
                    roww.append(1)
                    mod_h[col]-=1
                else:
                    roww.append(0)
            plot.append(roww)
        #print(plot)
        total=0
        for x in plot:
            #print(x)
            total+=self.get_occupied(x)
        return total
def test_solution():
    A=Solution()
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    #print("input: ", height)
    assert A.trap(height) == 6
    height = [4,2,0,3,2,5]
    #print("input: ", height)
    assert A.trap(height) == 9

test_solution()
