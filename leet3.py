def lengthOfLongestSubstring(s):
    # don't repeat the same character
    start = 0
    end = 0

    for i in range(0, len(s)):
        if s[i] not in s[start:end]:
            end += 1
        else:
            for j in range(start, end):
                if s[j] == s[i]:
                    start = j + 1
                    break  # end는 그대로 유지하면 됨
    return end - start + 1
print(lengthOfLongestSubstring('dvdf'))
print(lengthOfLongestSubstring('pekwwabw'))