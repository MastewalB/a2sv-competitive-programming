# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        begin = 1
        end = n
        while (begin < end):
            pivot = begin + (end - begin) // 2
            if (isBadVersion(pivot)):
                end = pivot
            else:
                begin = pivot + 1

        return begin
