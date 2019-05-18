'''
Gearing Up for Destruction
==========================

As Commander Lambda's personal assistant, you've been assigned the task of con-
figuring the LAMBCHOP doomsday device's axial orientation gears. It should be 
pretty simple - just add gears to create the appropriate rotation ratio. But the
problem is, due to the layout of the LAMBCHOP and the complicated system of
beams and pipes supporting it, the pegs that will support the gears are fixed in
place.

The LAMBCHOP's engineers have given you lists identifying the placement of 
groups of pegs along various support beams. You need to place a gear on each 
peg (otherwise the gears will collide with unoccupied pegs). The engineers have 
plenty of gears in all different sizes stocked up, so you can choose gears of 
any size, from a radius of 1 on up. Your goal is to build a system where the 
last gear rotates at twice the rate (in revolutions per minute, or rpm) of the 
first gear, no matter the direction. Each gear (except the last) touches and 
turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location 
of each peg along the support beam, write a function answer(pegs) which, if 
there is a solution, returns a list of two positive integers a and b represent-
ing the numerator and denominator of the first gear's radius in its simplest 
form in order to achieve the goal above, such that radius = a/b. The ratio a/b 
should be greater than or equal to 1. Not all support configurations will neces-
sarily be capable of creating the proper rotation ratio, so if the task is im-
possible, the function answer(pegs) should return the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could 
have a radius of 12, the second gear could have a radius of 14, and the last 
one a radius of 6. Thus, the last gear would rotate twice as fast as the first 
one. In this case, pegs would be [4, 30, 50] and answer(pegs) should return 
[12, 1].

The list pegs will be given sorted in ascending order and will contain at least
2 and no more than 20 distinct positive integers, all between 1 and 10000 inclu-
sive.
'''
def solution(pegs):
    if len(pegs) < 2:
        return [-1, -1]
    n = sum(2*pegs[i] if i&1 else -2*pegs[i] for i in range(1, len(pegs)-1))
    n -= pegs[0]
    if len(pegs)&1:
        n -= pegs[-1]
        res = [2*n, 1]
    else:
        n += pegs[-1]
        res = [2*n//3, 1] if n % 3 == 0 else [2*n, 3]

    r = res[0] / res[1]
    for i in range(1, len(pegs)):
        r = pegs[i] - pegs[i-1] - r
        if r <= 0:
            return [-1, -1]
    return res
