'''
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography.
During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, U,
or a downhill, D  step. Gary's hikes start and end at sea level and each step up or down represents
a unit change in altitude.
We define the following terms:
    A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level
    and ending with a step down to sea level.
    A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level
    and ending with a step up to sea level.

Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

For example, if Gary's path is , he first enters a valley  units deep.
Then he climbs out an up onto a mountain  units high. Finally, he returns to sea level and ends his hike.
'''
def counting_valleys(steps, way):
    downhill = 0
    level = 0
    if len(way) == steps:
        for step in way.upper():
            if step == 'U':
                level += 1
                if level == 0:
                    downhill += 1
            elif step == 'D':
                level -= 1
    else:
        return 'Way lenght must be equal to number of steps.'
    return downhill


def test_counting_valleys_correct():
    assert counting_valleys(8, 'UDDDUDUU') == 1
    assert counting_valleys(4, 'UUDD') == 0
    assert counting_valleys(5, 'DUDUU') == 2
    assert counting_valleys(8, 'DDDUU') == 'Way lenght must be equal to number of steps.'

def test_counting_valleys_false():
    assert not counting_valleys(5, 'DDDDU') == 1
    assert not counting_valleys(3, 'DUD') == 2
    assert not counting_valleys(4, 'DDDD') == 'Way lenght must be equal to number of steps.'