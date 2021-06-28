import getch
import sys
import pretty_errors

# MY FUNCTIONS ================================================================

def clear_term():
    print(chr(27) + "[2J") # non portable clear screen

# END MY FUNCTIONS ============================================================

# temp reading of file.. this should be stored into an arr instead
my_file = './words.txt'

with open(my_file, 'r') as fp:
    for line in fp:
        words_arr = line.split()
        # print(words_arr)

        # the loop to present words and take input here
        word_idx = 0
        row_len = 10
        user_input_correct = True

        while True: # master loop
            # change to control by flag variable??

            if user_input_correct: # if false, do not inc; keep curr line
                curr_row = [] # reset curr_row
                # get 10 words
                while True:
                    curr_row.append(words_arr[word_idx])
                    word_idx += 1
                    # limit to only 10 words in a row
                    if (word_idx % row_len) == 0:
                        break

            # curr_row.append('\n') # add newline
            output_row = ' '.join(curr_row) # convert to str
            print(output_row)

            user_input = '' # init user input as a str
            while True:
                c = getch.getche() # stream in one char at a time
                user_input += c # immediately append to the buffer
                if user_input == output_row:
                    # if the word is right, stick into arr and continue?
                    print(user_input, end = '')
                    user_input_correct = True
                    break
                if c == '':
                    user_input_correct = False
                    break

        clear_term()
