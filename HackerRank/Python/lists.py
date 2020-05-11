L = []
N = int(input())
while 1:
    try:
        inp = raw_input().strip()
        while "  " in inp: inp.replace("  "," ")
        command = map(str,inp.split())
    except:
        break
    if len(command)>1: command[1]=int(command[1])
    if len(command)>2: command[2]=int(command[2])
        
    if command[0]=="sort":
        L.sort()
    elif command[0]=="print":
        print L
    elif command[0]=="reverse":
        #L.reverse()
        L=L
    elif command[0]=="pop":
        L.pop()
    elif command[0]=="insert":
        L.insert(command[1],command[2])
    elif command[0]=="append":
        L.append(command[1])
    elif command[0]=="remove":
        L.remove(command[1])
