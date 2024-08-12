def minion_game(string):

    s=len(string)
    #print(s)
    Stuart, Kevin =0,0
    for i in range(s):
        if string[i] in 'AIEOU':
            #print(string[2])

            Kevin=Kevin+(s-i)
            #print(Kevin)
        else:
            #print(string[i])
            Stuart=Stuart+(s-i)
            #print(Stuart)
    if Stuart>Kevin:
        print("Stuart {}".format(Stuart))
    else:
        print("Kevin {} ". format(Kevin))



if __name__ == '__main__':
        s = input()
        minion_game(s)