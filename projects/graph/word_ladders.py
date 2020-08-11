from util import Queue
import string


# from graph import get_neighbors
##Build our graph
# could filter our word list by length
# rememeber to lower case stuff

#BFS

class Graph:
    pass

# len(word) * 26
# 0(n*26)

word__list = set()
for word in words:
        word__list.add(word.lower())

def get_neighbors(word):
    neighbors = []
    #for every letter in the word
    for letter_index in range(len(word)):
        for letter in string.ascii_lowercase:
            word_list = list(word)
            word_list[letter_index] = letter
                
            word = "".join(word_list)

                if word in word_list and word != start_word:
                        neighbors.append(word)

    return neighbors
#BFS
def word_ladders(start_word, end_word):
    q = Queue()
    visited = set()
    q.enqueue([start_word])

    while q.size() > 0:

        current_path = q.dequeue()
        current_word = current_path[-1]

        if current_word == end_word:
            return current_path

        if current_word not in visited:
            visited.add(current_word)

            neighbors = get_neighbors(current_word)

            for neighbor in neighbors:
                new_path = current_path + [neighbor]
                q.enqueue(new_path)
