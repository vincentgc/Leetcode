class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        hand = {5:0,10:0}
        for b in bills:
            if b == 5:
                hand[5] += 1
            elif b == 10:
                hand[10] += 1
                if hand[5] < 1:
                    return False
                else:
                    hand[5] -= 1
            else:
                if hand[10]*10+hand[5]*5<15 or not hand[5]:
                    return False
                else:
                    if hand[10] and hand[5]:
                        hand[10] -= 1
                        hand[5] -= 1
                    elif not hand[10]:
                        hand[5] -= 3
        return True