class solution(object):
    def merge_alternately(self, word1: str, word2: str) -> str:
        """Returns a string with alternating iterated letters from word1 and word2.
        Args:
            word1 (str): first word
            word2 (str): second word

        Returns:
            str: returned string
        """
        length_1 = len(word1)
        length_2 = len(word2)
        
        shorter = min(length_1, length_2)
        
        result = ""
        for i in range(shorter):
            result += word1[i] + word2[i]
        result += word2[shorter:]
        return  result

    print("pqrst"[10:])