# Part 1
# Load the file
with open('input.txt', 'r') as f:
    data = f.readlines()
    id_sum = 0
    for line in data:
        prefix = line.split(' ')[0:2]
        # Get the id of the current game
        id = int(prefix[1][:-1])
        prefix = ' '.join(prefix)
        games = line.removeprefix(prefix).split(';')
        # Remove newline
        games[-1] = games[-1].rstrip()
        valid_id = True
        for game in games:
            red = 0
            blue = 0
            green = 0
            # Remove all commas from the string
            game = game.replace(',', '')
            # Split game into number of balls and colours
            game = game.split(' ')[1:]
            for index, element in enumerate(game):
                match element:
                    case 'red':
                        red = int(game[index - 1])
                    case 'blue':
                        blue = int(game[index - 1])
                    case 'green':
                        green = int(game[index - 1])
            # Check if the game is valid
            if red > 12 or green > 13 or blue > 14:
                valid_id = False
                break
        if valid_id:
            id_sum += id
    print(id_sum)


# Part 2
# Load the file
with open('input.txt', 'r') as f:
    data = f.readlines()
    id_sum = 0
    for line in data:
        prefix = line.split(' ')[0:2]
        # Get the id of the current game
        id = int(prefix[1][:-1])
        prefix = ' '.join(prefix)
        games = line.removeprefix(prefix)
        # Remove newline
        games = games.rstrip()
        red = 0
        blue = 0
        green = 0
        # Remove all commas from the string
        games = games.replace(',', '')
        # Remove all semicolons from the string
        games = games.replace(';', '')
        # Split game into number of balls and colours
        game = games.split(' ')[1:]
        print(game)
        for index, element in enumerate(game):
            match element:
                case 'red':
                    red = max(int(game[index - 1]), red)
                case 'blue':
                    blue = max(int(game[index - 1]), blue)
                case 'green':
                    green = max(int(game[index - 1]), green)

        product = red * blue * green
        id_sum += product
    print(id_sum)



