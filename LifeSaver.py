def life_saver(NK, player_heights):
    """
        Counts the number of players taller than the shooting height.

        Parameters:
        NK : A list containing N (total number of players) and K (required height).
        player_heights : Heights of the players.

        Result:
        Prints the number of players to be shot.
    """
    count = 0
    for shot in range(NK[0]):
        if player_heights[shot] > NK[1]:
            count += 1
    # Number of people to get shot
    print(count)


if __name__ == '__main__':
    total_test_case = int(input("Enter total test cases : "))
    test = []
    for test_value in range(total_test_case):
        detail = list(map(int, input("").split()))
        heights = list(map(int, input("").split()))
        test.append({
            'testDetail': detail,
            'testHeight': heights
        })

    for test_case in test:
        life_saver(test_case['testDetail'], test_case['testHeight'])
