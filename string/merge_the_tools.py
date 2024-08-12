def merge_the_tools(string, k):

    s=''
    c=0
    for i in string:
        if i not in s :
            s=s+i
        c+=1
        print(c)
        if (c==k):
            print(s)
            c=0
            s=''



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

















'''AABCAAADA
3'''