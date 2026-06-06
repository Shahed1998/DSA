class Solution:
    def decodeString(self, s: str) -> str:

        # Stores previous contexts:
        # (string_before_bracket, repeat_count)
        stack = []

        # String being built in the current context
        curr_str = ""

        # Number currently being read
        # Example: reading "12[a]" should produce 12
        curr_num = 0

        for ch in s:

            # Build multi-digit numbers
            # Example:
            # '1' -> 1
            # then '2' -> 12
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            # Entering a new nested context
            elif ch == '[':

                # Save everything we need to return later:
                # - string built so far
                # - repeat count for the upcoming block
                stack.append((curr_str, curr_num))

                # Start fresh for the inner string
                curr_str = ""
                curr_num = 0

            # Finished current nested context
            elif ch == ']':

                # Recover the previous context
                prev_str, repeat = stack.pop()

                # Expand current string and attach it
                # to the previous string
                #
                # Example:
                # prev_str = "a"
                # curr_str = "c"
                # repeat   = 2
                #
                # result = "a" + "cc"
                #        = "acc"
                curr_str = prev_str + curr_str * repeat

            # Regular character
            else:
                curr_str += ch

        return curr_str


        



s = Solution()
# s.decodeString(s = "3[a]xyz2[bc]")
s.decodeString(s = "3[a2[c]]")