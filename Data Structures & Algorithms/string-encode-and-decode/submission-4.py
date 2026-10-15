class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            l = len(s)
            encoded += f"{str(l)}#{s}"
            # print(f"Encoding: {s} -> {encoded}")
        # print(f"Final encoded string: {encoded} length: {len(encoded)}")
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            # print(f"======= Decoding at index {i}: {s[i:]} =======")
            le = ""
            while s[i] != "#":
                le += s[i]
                i += 1
            l = int(le)
            i += 1
            new_str = ""
            str_l = l + i
            # print(f"str_l: {str_l}")
            while i < str_l:
                new_str += s[i]
                # print(f"Building string: {new_str}, s[i]={s[i]}")
                i += 1
            # print(f"Decoded string: {new_str}")
            decoded.append(new_str)
        return decoded
