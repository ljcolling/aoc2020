
timestamp = 939
start_time = timestamp
bus_ids = [7, 13,  59,  31, 19]


f = open("puzzle_data.txt")
timestamp = int(f.readline())
start_time = timestamp
buses = f.readline().split(",")
bus_ids = [int(b) for b in buses if b != "x"]




found = False
bus_to_take = 0
time_to_take = 0
while found == False:
    timestamp += 1
    for bus in bus_ids:
        if (timestamp % bus) == 0:
           time_to_take = timestamp
           bus_to_take = bus
           found = True

# print(time_to_take)
# print(bus_to_take)

print((time_to_take - start_time) * bus_to_take)

def check_offset(t):
    if (t % 7) == 0:
        if (13 - (t % 13)) == 1:
            if (59 - (t % 59)) == 4:
                if (31 - (t % 31)) == 6:
                    if (19 - (t % 19)) == 7:
                        print(t % 7)
                        print(t % (13))
                        print(t % (59))
                        print(t % 31)
                        print(t % 19)
                        print("------")
                        return True 
    else: 
        return False


print([t for t in range(1068780,1000000000000, 1) if check_offset(t) == True])


