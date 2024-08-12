import textwrap

def wrap(string):
    return textwrap.fill(string)

if __name__ == '__main__':
    string= input()
    result = wrap(string)
    print(result)