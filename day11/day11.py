


class Ship:
    def __init__(self, facing, horz, vert):
        self.facing = facing
        self.horz = horz
        self.vert = vert

    def move(self, action, value):
        if action in ['L','R']:
            #print(f"turning {action}...")
            bearing = 0
            if self.facing == "N":
                bearing = 0
            elif self.facing == "E":
                bearing = 90
            elif self.facing == "S":
                bearing = 180
            elif self.facing == "W":
                bearing = 270

            mul = 0
            if action == "L":
                mul = -1
            else:
                mul = 1

            value = value * mul

            if value == -90:
                value = 270
            if value == -180:
                value = 180
            if value == -270:
                value = 90


            bearing = bearing + value
            if bearing >= 360:
                bearing = bearing % 360

            if bearing == 0:
                self.facing = "N"
            elif bearing == 90:
                self.facing = "E"
            elif bearing == 180:
                self.facing = "S"
            elif bearing == 270:
                self.facing = "W"



        elif action in ['F']:
            ##print("Moving foward")
            facing = self.facing
            if facing == "E":
                self.horz += value
            if facing == "N":
                self.vert += value
            if facing == "S":
                self.vert -= value
            if facing == "W":
                self.horz -= value
        else:
            #print(f"Moving {action}...")
            if action == "N":
                self.vert += value
            if action == "S":
                self.vert -= value
            if action == "E":
                self.horz += value
            if action == "W":
                self.horz -= value
    def report(self):
        return [self.horz, self.vert]

    def tellFacing(self):
        ##print(self.facing)
        return self.facing




def Tests():
    ship = Ship("E",0,0)
    assert ship.report() == [0, 0]
    print("Passed!")

    ship.move("F",10)
    assert ship.report() == [10, 0]
    print("Passed!")

    ship.move("N",3)
    assert ship.report() == [10, 3]
    print("Passed!")

    ship.move("F",7)
    assert ship.report() == [17, 3]
    print("Passed!")

    ship.move("R",90)
    assert ship.report() == [17, 3]
    assert ship.tellFacing() == "S"
    print("Passed!")

    ship.move("F",11)
    assert ship.report() == [17, -8]
    print("Passed!")

    ship.move("F",1)
    assert ship.report() == [17, -9]
    print("Passed!")



Tests()
directions = []
ship = Ship("E",0,0)
with open("puzzle_data.txt") as f:
    for line in f:
        action = line[0]
        value = int(line[1:])
        directions.append([action, value])




for d in directions:
    action = d[0]
    value = d[1]
    ship.move(action, value)


loc = ship.report()

print(abs(loc[0]  ) + abs(loc[1]))
