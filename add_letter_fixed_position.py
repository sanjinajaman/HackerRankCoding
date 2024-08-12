
def mutate_string(string, position, character):
    a=string[:position]+character+string[position+1:]
    return a


'''string=input()
position=int(input())
character=input()
print(mutate_string(string, position, character))'''


string=input()
position,character=input().split()
print(mutate_string(string,int( position), character))