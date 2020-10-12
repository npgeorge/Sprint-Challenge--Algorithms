'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #initialize count
    count = 0
    
    #if less than 2, return count 0, aka base case
    if len(word) < 2:
        return count
    
    # initialize index
    x = 0
    # defining window to search 2 places in array
    th_window = word[x:x+2]
    
    # if window finds th, add to count, keep searching
    if th_window == 'th':
        # add to count
        count += 1
        # move index over by 1
        x += 1
        # count + recursively call until end of word
        return count + count_th(word[x:])
    else:
        # otherwise, return the word
        return count_th(word[1:])

print(count_th('thththththth'))
