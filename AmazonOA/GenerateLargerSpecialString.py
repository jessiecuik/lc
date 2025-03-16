
# Given a string K, generate a string of the same length:
# - no matching adjacent characters (i.e. jj)
# - should be lexicographically greater than the input string (abcd -> abce)
# - return -1 if lexicographically next string cannot be generated within K size

# abcc -> abcd
# abccss -> abcdab
# cc replaced with cd as that’s lexicographically the next one.
# Then we could just append ababababab until the limit allows.


def generateLargerSpecialString(input_string: str) -> str:
    generated_string = ''
    stk = []
    l = len(input_string)
    for i in range(l):
        if stk and stk[-1] == input_string[i]:
            stk.append(input_string[i])
            break
        stk.append(input_string[i])
    last_char = stk.pop()
    while stk and last_char == 'z' or (last_char == 'y' and stk[-1] == 'z'):
        last_char = stk.pop()
    if last_char == 'z':
        return "-1"
    next_char = chr(ord(last_char) + 1)
    if next_char == stk[-1]:
        next_char = chr(ord(last_char) + 2)
    stk.append(next_char)
    while len(stk) < l:
        next_char = 'a' if stk[-1] > 'a' else 'b'
        stk.append(next_char)
    generated_string = ''.join(stk)
    return generated_string

def main():
    input_string = input()
    print(generateLargerSpecialString(input_string))

if __name__ == '__main__':
    main()