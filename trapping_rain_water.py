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
    def trap(self, height: list[int]) -> int:
        first_ref=height[0]
        bott_ref=0
        container=[0]*max(height)
        total=0
        for new_val in height[1:]:
            if first_ref == 0:
                first_ref = new_val
                bott_ref = first_ref
                continue
            elif first_ref>0:
                if new_val < first_ref:
                    for x in range(new_val,first_ref):
                        container[x]+=1

                    if new_val > bott_ref:
                        # check if at this level container is filled
                        for x in range(bott_ref, new_val):
                            if container[x] >= 1:
                                total+=container[x]
                                container[x]=0
                    bott_ref = new_val

                elif new_val >= first_ref:
                    first_ref = new_val
                    bott_ref = first_ref
                    total+=sum(container)
                    container=[0]*max(height)
        return total
def test_solution():
    A=Solution()
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    #print("input: ", height)
    assert A.trap(height) == 6
    height = [4,2,0,3,2,5]
    #print("input: ", height)
    assert A.trap(height) == 9
    height =[0,7,1,4,6]
    assert A.trap(height) == 7
test_solution()
