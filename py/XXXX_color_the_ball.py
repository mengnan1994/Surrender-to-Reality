"""
Description
N个气球排成一排，从左到右依次编号为1,2,3…N.每次给定2个整数a b(a <= b),lele便为骑上他的“小飞鸽"牌电动车从气球a开始到气球b依次给每个气球涂一次颜色。但是N次以后lele已经忘记了第I个气球已经涂过几次颜色了，你能帮他算出每个气球被涂过几次颜色吗？

Input
每个测试实例第一行为一个整数N,(N <= 100000).接下来的N行，每行包括2个整数a b(1 <= a <= b <= N)。
当N = 0，输入结束。

Output
每个测试实例输出一行，包括N个整数，第I个数代表第I个气球总共被涂色的次数。

Sample Input
3
1 1
2 2
3 3
3
1 1
1 2
1 3
0

Sample Output
1 1 1
3 2 1
"""

class Solution(object):
    def color_the_ball