#!/Users/lc663/.pyenv/shims/python

numbers = [2, 15, 0, 9, 1, 20]

said_numbers = []

for n in numbers:
    if (n in said_numbers) == False:
        said_numbers.append(n)




said_numbers = {2: [1], 15: [2], 0:[3], 9:[4], 1:[5], 20:[6]}
last_number = list(said_numbers.keys())[len(said_numbers) - 1]
max_turns = 30000000
turn = len(said_numbers) + 1
for turn in range(len(said_numbers) + 1, max_turns + 1):
    current_number = last_number
    times_said = len(said_numbers[current_number])
    if times_said == 1:
        last_number = 0
        if last_number in said_numbers.keys():
            current = said_numbers[last_number]
            current = current[len(current) - 1]
            said_numbers[last_number] = [current] + [turn]
        else:
            said_numbers[last_number] = [turn]
    if times_said > 1:
        last_time = said_numbers[current_number]
        last = last_time[len(last_time) - 1]
        second_last = last_time[len(last_time) - 2]
        last_number = last - second_last
        if last_number in said_numbers.keys():
            current = said_numbers[last_number]
            current = current[len(current) - 1]
            said_numbers[last_number] = [current] + [turn]
        else:
            said_numbers[last_number] = [turn]
    if turn == max_turns:
        print(f"The number spoken is {last_number}")
        break

    turn = turn + 1


