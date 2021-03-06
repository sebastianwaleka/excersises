'''
Emma is playing a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus.
She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2.
She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting
postion to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.
For example c = [0,1,0,0,0,1,0] indexed from 0...6. The number on each cloud is its index in the list
so she must avoid the clouds at indexes 1 and 5. She could follow the following two paths:
0 -> 2 -> 4 -> 6 or 0 -> 2 -> 3 -> 4 -> 6. The first path takes 3 jumps while the second takes 4.

Complete the jumpingOnClouds function in the editor below.
It should return the minimum number of jumps required, as an integer
'''


def jumping_on_clouds(clouds, way):
    steps = 0
    i = 0
    while i < clouds - 1:
        if i + 2 < clouds and way[i + 2] == '0':
            steps += 1
            i += 2
        else:
            steps += 1
            i += 1

    return steps


def test_jumping_on_clouds_correct():
    assert jumping_on_clouds(7, '0100010') == 3
    assert jumping_on_clouds(5, '00100') == 3
    assert jumping_on_clouds(8, '00010000') == 4


def test_jumping_on_clouds_false():
    assert not jumping_on_clouds(3, '000') == 2
    assert not jumping_on_clouds(5, '01010') == 3
    assert not jumping_on_clouds(7, '0001010') == 5
