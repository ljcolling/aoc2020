
tickets = []
with open("tickets.txt") as f:
  for line in f:
        ticket = [x for x in line.split(",")]
        tickets.append(ticket)
