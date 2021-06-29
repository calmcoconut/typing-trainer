import getch
import pretty_errors # pretty_errors for colored error msgs

# MY FUNCTIONS ================================================================

def clear_term():
    '''non portable way to clear the terminal screen'''
    print(chr(27) + "[2J")

def get_user_input_characters(user_input, output_row):
    '''
    get user input; 
    refresh the screen if backspace () or delete line ()
    '''
    while True:

        # get new line if correct
        if user_input == output_row:
            user_input = ''
            return True, user_input

        c = getch.getche() # consider not echoing, print later?
        # this must be after checking the row... it causes the loop to stop
            # and wait for input

        # completely clear line
        if c == '':
            user_input = ''
            return False, user_input
        
        # backspace one char
        if c == '':
            user_input = user_input[:-1] # trim last char using str slicing
            return False, user_input

        # must come after error checking so that refreshing works correctly
        user_input += c

        # LATER implement kill one word back  (^w) and  (^backspace)

def get_row_10_words(user_input_correct, word_idx, row_len):

    curr_row = []
    while True:
        curr_row.append(words_arr[word_idx])
        word_idx += 1
        # limit to only 10 words in a row
        if (word_idx % row_len) == 0:
            return curr_row, word_idx

# END MY FUNCTIONS ============================================================

# temp reading of file.. this should be stored into an arr instead
my_file = './words.txt'

with open(my_file, 'r') as fp:
    for line in fp:
        words_arr = line.split()

        word_idx = 0
        row_len = 10
        user_input_correct = True
        user_input = '' # keep outside because the user_input must
            # keep its state

        while True: # master loop
            if user_input_correct:
                current_row, word_idx = \
                    get_row_10_words(user_input_correct, word_idx, row_len)

            output_row = ' '.join(current_row) # convert arr of words to str

            clear_term()
            print(f'{output_row}\n{user_input}', end = '')

            user_input_correct, user_input = \
                get_user_input_characters(user_input, output_row)
