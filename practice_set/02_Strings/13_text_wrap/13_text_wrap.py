import textwrap

def wrap1(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))



if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap1(string, max_width)
    print(result)