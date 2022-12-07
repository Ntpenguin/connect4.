from random import *

print("Hunt the Wumpus!")

cave = {1: [2, 5, 8], 2: [1, 3, 10], 3: [2, 4, 12], 4: [3, 5, 14], 5: [1, 4, 6],
        6: [5, 7, 15], 7: [6, 8, 17], 8: [1, 9, 7], 9: [8, 10, 18], 10: [2, 9, 11],
        11: [19, 10, 12], 12: [11, 3, 13], 13: [12, 20, 14], 14: [4, 13, 15],
        15: [6, 14, 16], 16: [15, 17, 20], 17: [7, 18, 16], 18: [19, 17, 9],
        19: [18, 11, 20], 20: [13, 16, 19]}


def randomNumExcluding(bottom, top, exclude):
    return choice(
        [number for number in range(bottom, top)
         if number not in exclude]
    )


unUsable = []
player_position = randint(1, 20)
unUsable.append(player_position)
wumpus_position = randomNumExcluding(1, 20, unUsable)
unUsable.append(wumpus_position)
unUsable.append(player_position)
bat_positions = []
bat_positions.append(randomNumExcluding(1, 20, unUsable))
unUsable.append(bat_positions[0])
bat_positions.append(randomNumExcluding(1, 20, unUsable))
unUsable.append(bat_positions[1])
pit_positions = []
pit_positions.append(randomNumExcluding(1, 20, unUsable))
unUsable.append(pit_positions[0])
pit_positions.append(randomNumExcluding(1, 20, unUsable))


def player_shoot(p_position, arrow_nums, arrow_room):
    arrowlist = []
    for count in arrow_nums:
        if arrow_room in cave[p_position]:
            print("Your arrow landed in room: " + str(arrow_room))
        else:
            print("That was an invalid room. Next time, choose your room wisely...")
            arrow_room = cave[p_position][randint(0, 2)]
            print("Your arrow landed in room: " + str(arrow_room))


def player_move(p_position, w_position):
    for room in cave[p_position]:
        if w_position == room:
            p_position = w_position
            print("The player is now in room: " + str(p_position))


def near_by(p_position, wum_position, b_position, pit_position):
    for room_nearby in cave[p_position]:
        print()


player_shoot(6, 5, 7)
