with open ("day1.txt") as text:
    

    lines = text.readlines() # list containing lines of file
    sum = 0
    words = ["one",
             "two",
             "three",
             "four",
             "five",
             "six",
             "seven",
             "eight",
             "nine"]

    for line in lines:
        nums = []
        # print("before conversion: " + line)
        for index, char in enumerate(line):
            if (char.isnumeric()):
                nums.append(int(char))
            for i, word in enumerate(words):
                if line[index:].startswith(word):
                    nums.append(i+1)
                
        sum += nums[0] * 10
        sum += nums[-1]
                               
print(sum)
    