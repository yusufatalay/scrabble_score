letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key: value for key, value in
                    zip(letters, points)}  # matching letters and point as key:value pairs and create a  dictionary of
letter_to_points[" "] = 0


def score_word(word):  # returns the value of corresponding word
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total


player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}


def play_word(_player, _word):  # this function adds new word to given player
    temp_list = player_to_words.get(_player)
    temp_list.append(_word)
    player_to_words[_player] = temp_list


def update_point_totals():  # function for updating the point whenever new word is played
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points


print(player_to_words)
