'''
John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
Given an array of integers representing the color of each sock, determine how many pairs of socks
with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one of color .
There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing
the number of matching pairs of socks that are available.

Sock Merchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock

Input Format
    The first line contains an integer , the number of socks represented in .
    The second line contains  space-separated integers describing the colors  of the socks in the pile.

Constraints
    1 <= n <= 100
    1 <= ar[i] <= 100 where 0 <= i < n

Output Format
    Print the total number of matching pairs of socks that John can sell.

Sample Input
    9
    10 20 20 10 10 30 50 10 20

Sample Output
    3
'''


def socks(number_of_socks, socks_colors):
    socks_pairs = {}
    pairs = 0
    if len(socks_colors) == number_of_socks:
        for sock in socks_colors:
            socks_pairs[sock] = socks_pairs.get(sock, 0) + 1
        for value in socks_pairs.values():
            pairs += (value // 2)
        return pairs
    else:
        return 'Number of socks must be equal to socks colors!'


while True:  # do while rule 1 <= n <= 100 is not met
    try:
        number_of_socks = int(input('Enter number of socks in pile:'))
        if 1 <= number_of_socks <= 100:
            break  # rule is met - we need only one number
        else:
            print('Number of socks must be in range 1-100.')
    except ValueError:
        print('Wrong input. Must be single integer.')  # raise error if wrong input type is given

socks_colors = []  # creating empty list to store socks colors

while len(socks_colors) < number_of_socks:
    colors = input('Enter colors: ')
    colors = colors.split(' ')  # spliting by 'whitespace' if string is given in input.
    socks_colors.extend(colors)  # .extend becouse .append makes list of lists. Extend only extends actual list
    for sock in socks_colors:
        if int(sock) > 100 or int(sock) < 1:  # checking whether rule 1<= ar[i]<=100 is met.
            socks_colors.remove(sock)  # If not - remove wrong value

if len(socks_colors) > number_of_socks:
    socks_colors = socks_colors[:number_of_socks]  # cutting to correct lenght if more values were given

print(socks(number_of_socks, socks_colors))
