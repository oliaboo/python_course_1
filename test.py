with open('log.txt') as list:
    for line in list:
        line_list = line.split(' ')
        time_list = line_list[3].split(':')
        if (line_list[0]=='64.242.88.10')and((int(time_list[1])==16  and int(time_list[2])>=10)or(int(time_list[1])==17 and int(time_list[2])<=20))and line_list[8]!= '200':
            line_list[9] = line_list[9].replace('\n','')
            sum1 = 0
            for i in range(len(line_list[9])):
                sum1 += int(line_list[9][i])
            if sum1 > 20:
                print(line_list)
            
