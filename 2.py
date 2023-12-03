import re

file = open('2.txt', 'r').readlines()
games = {}
not_possible_ids = []
possible_ids = 0
for line in file:
    num_rounds = line.count(';')
    game_num = int(line.split(': ')[0].split(' ')[1])
    games[game_num] = {}
    green = 0
    blue = 0
    red = 0
    for round in range(num_rounds+1):
        colors = line.split(': ')[1].split('; ')[round].split(', ')
        for color in colors:
            if 'green' in color:
                if int(color.split(' ')[0]) > green:
                    green = int(color.split(' ')[0])
                if int(color.split(' ')[0]) > 13:
                    not_possible_ids.append(game_num)
            elif 'red' in color:
                if int(color.split(' ')[0]) > red:
                    red = int(color.split(' ')[0])
                if int(color.split(' ')[0]) > 12:
                    not_possible_ids.append(game_num)
            elif 'blue' in color: 
                if int(color.split(' ')[0]) > blue:
                    blue = int(color.split(' ')[0])
                if int(color.split(' ')[0]) > 14:
                    not_possible_ids.append(game_num)
        games[game_num]['red'] = red
        games[game_num]['blue'] = blue
        games[game_num]['green'] = green


total_sum = 0
for i in range(100):
    round_sum = 1
    for j in games[i+1]:
        print(j, games[i+1][j])
        round_sum *= games[i+1][j]
    total_sum += round_sum
    print(i+1, round_sum, total_sum)
    if i+1 not in not_possible_ids:
        possible_ids += i+1

#16260 too low
#1210618 too high
print(possible_ids)
print(total_sum)
