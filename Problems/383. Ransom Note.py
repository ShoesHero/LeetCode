class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False

        record = {}
        for i in magazine:
            if i not in record:
                record[i] = 1
            else:
                record[i] += 1

        for i in ransomNote:
            if i not in record or record[i] <= 0:
                return False
            else:
                record[i] -= 1

        return True
