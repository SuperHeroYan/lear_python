the_board = {'top-L': '0', 'top-M': '0', 'top-R': '0',
            'mid-L': 'x', 'mid-M': 'x', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': 'x'}


def print_board(board):
    print( board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print( board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print( board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

print_board(the_board)