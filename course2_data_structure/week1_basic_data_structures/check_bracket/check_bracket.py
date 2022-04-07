# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append( Bracket(next, i+1))
            # Process opening bracket, write your code here
            
            pass

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                position = i+1
                return position
            else:
                last = opening_brackets_stack[-1]
                if are_matching(last.char, next):
                    opening_brackets_stack.pop()
                else:
                    position = i+1
                    return position

    if len(opening_brackets_stack) == 0:
        return 'Success'
    else:
        return opening_brackets_stack[0].position

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
