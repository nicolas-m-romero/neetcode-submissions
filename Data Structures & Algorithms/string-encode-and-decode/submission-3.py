class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for i in range(len(strs)):
            encoded += strs[i] + "DELIM"

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = s.split("DELIM")

        return decoded[0:-1]
