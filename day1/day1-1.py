with open ("day1.txt") as text:
    

    lines = text.readlines() # list containing lines of file
    sum = 0

    for line in lines:
        #print(line)
        line = line.strip() # remove leading/trailing white spaces
        for ch in line:
            i = 0
            if ch.isdigit():
                if i == 0:
                    sum += int(ch) * 10
                    i = 1
                    break
                
        for ch in reversed(line):
            i = 0
            if ch.isdigit():
                if i == 0:
                    sum += int(ch)
                    print(sum)
                    i = 1
                    break
    print(sum)

