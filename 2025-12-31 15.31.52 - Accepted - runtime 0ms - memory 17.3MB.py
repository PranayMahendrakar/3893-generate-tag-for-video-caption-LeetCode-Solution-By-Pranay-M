class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        result = '#'
        for i, word in enumerate(words):
            # Keep only letters
            cleaned = ''.join(c for c in word if c.isalpha())
            if not cleaned:
                continue
            if i == 0:
                result += cleaned.lower()
            else:
                result += cleaned[0].upper() + cleaned[1:].lower()
        return result[:100]