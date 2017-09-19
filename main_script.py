import sys

INT_STR = None

def is_palindrome(string):
    __str = string.replace(' ', '')
    __str = __str.lower()
    for i, char in enumerate(__str):
        if char != __str[-i-1]:
            return False
    return True

def main():
    if is_palindrome(INT_STR):
        print('It\'s palindrome')
    else:
        print('It\'s not palindrome')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        INT_STR = sys.argv.pop()
    else:
        INT_STR = input('input interesting string: ')
    main()
