"""LeetCode 271: Encode and Decode Strings (Compact Guided Practice)

Problem URL: https://leetcode.com/problems/encode-and-decode-strings/
Difficulty: Medium
Category: Arrays & Hashing

Pattern Context:
    Stateless serialization of a list of strings into a single string.
    Naively joining on a delimiter (like comma or slash) fails if the strings themselves
    contain that delimiter.
    Robust Protocol: Length-Prefixed Chunking (similar to HTTP Chunked Transfer Encoding):
        Format: "<length>#<string>" (e.g. "4#lint4#code")
    During decode, we read the length integer until '#', extract that exact slice, and repeat.

Format:
    Guided TODO = None placeholders with step-by-step hints.
    Complete the assignment below to pass the offline verification suite.

Run standalone:
    python 01_arrays_and_hashing/lc_0271_encode_and_decode_strings_compact.py
"""

from __future__ import annotations
from typing import List

# Sentinel placeholder for exercise tasks
TODO = None


class Codec:
    """Encodes a list of strings to a single string and decodes it back."""

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.

        Algorithmic Requirements:
        - Time Complexity: O(N) where N is the total number of characters across all strings.
        - Space Complexity: O(1) auxiliary space (excluding encoded string).
        """
        res = []
        for s in strs:
            # <<< YOUR CODE HERE >>>
            # Hint: Format each string as f"{len(s)}#{s}"
            chunk = TODO  # Replace with: f"{len(s)}#{s}"
            if chunk is None:
                raise NotImplementedError("TODO: Encode string with length prefix.")
            res.append(chunk)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string back to a list of strings.

        Algorithmic Requirements:
        - Time Complexity: O(N) where N is the length of string s.
        - Space Complexity: O(1) auxiliary space (excluding output list).
        """
        res: List[str] = []
        i = 0
        while i < len(s):
            # Locate the '#' delimiter
            j = i
            while s[j] != "#":
                j += 1

            # <<< YOUR CODE HERE >>>
            # Hint: Extract the length integer from s[i:j], then slice the word
            length = TODO  # Replace with: int(s[i:j])
            if length is None:
                raise NotImplementedError("TODO: Parse chunk length.")

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

    print("Running verification for lc_0271_encode_and_decode_strings_compact.py...")
    for idx, strs in enumerate(test_cases, 1):
        encoded = codec.encode(strs)
        decoded = codec.decode(encoded)
        assert decoded == strs, f"Case {idx} failed: got {decoded}, expected {strs}"
        print(f"  [PASS] Test Case {idx} (Encoded: {repr(encoded)[:30]}...)")
    print("All tests passed with 100% success rate!")
