def count_substring(string, sub_string):
    count=0
    x = len(sub_string)
    for i in range(len(string)):
        s=string[i:i+x] #[0:0+3=3]  [1:1+3=4]  [2:2+3=5]

        if s==sub_string:
            count+=1
    return count

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)