with open("day02/input.txt", "r") as input:
    words = input.readline().split(",")
    line = [int(word) for word in words]

    ip = 0
    san = 0

    print(line)

    while (line[ip] != 99):
        san += 1
        if san > 100000:
            print("Reached sanity end, breaking")
            break

        opcode = line[ip]
        iptr1 = line[ip+1]
        iptr2 = line[ip+2]
        optr = line[ip+3]

        print("Tick %i word: [%i,%i,%i,%i]" % (san, opcode, iptr1, iptr2, optr))

        if opcode == 1:
            line[optr] = line[iptr1] + line[iptr2]
        elif opcode == 2:
            line[optr] = line[iptr1] * line[iptr2]
        else:
            print("Invalid opcode %i at PC %i, tick %i" % (line[ip], ip, san))
            break

        print("storing %i in [%i]" % (line[optr], optr))
        
        ip += 4
    
    print(line)
    print("result: %i pc: %i" % (line[0], ip))