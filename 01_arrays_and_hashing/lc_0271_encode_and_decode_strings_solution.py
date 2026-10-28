"""LeetCode 271: Encode and Decode Strings (Reference Solution)

Problem URL: https://leetcode.com/problems/encode-and-decode-strings/
Difficulty: Medium
Category: Arrays & Hashing

Complexity Analysis:
- Time Complexity: O(N) where N is the total number of characters across all strings.
  Encoding performs a single linear pass to construct length-delimited chunks.
  Decoding scans character-by-character, directly jumping by parsed slice lengths.
- Space Complexity: O(1) auxiliary space beyond the required encoded string and decoded list.
"""

from __future__ import annotations
from typing import List


class Codec:
    """Encodes and decodes a list of strings using length-prefixed chunking."""

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string using `<len>#<string>` format."""
        res: List[str] = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes length-prefixed chunks back into original list of strings."""
        res: List[str] = []
        i = 0
        while i < len(s):
            # Locate the '#' character marking end of length prefix
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            end = start + length
            res.append(s[start:end])
            i = end

        return res


# =====================================================================
# Offline Test Harness
# =====================================================================
if __name__ == "__main__":
    codec = Codec()
    test_cases = [
        ["lint", "code", "love", "you"],
        ["we", "say", ":", "yes"],
        [""],
        [],
        ["123#abc", "##", "hello#world#!"],
        ["   ", " ", "a"],
    ]

    print("Running verification for lc_0271_encode_and_decode_strings_solution.py...")
    for idx, strs in enumerate(test_cases, 1):
        encoded = codec.encode(strs)
        decoded = codec.decode(encoded)
        assert decoded == strs, f"Case {idx} failed: got {decoded}, expected {strs}"
        print(f"  [PASS] Test Case {idx} (Encoded: {repr(encoded)[:30]}...)")
    print("All tests passed with 100% success rate!")
