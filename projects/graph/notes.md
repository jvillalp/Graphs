solving graph problems:

1. Describe the problem using graphs terminology
    what are your nodes?
        node = word
    when are nodes connected?

    what are your connected components?

2. build your graph, or write  your getNeighbors()
    Figure out how to get the node's edges

3. Choose your algorithm and apply it


EXAMPLE
Given two words (begin_word and end_word), and a dictionary's word list, 
return the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed at a time.

Each transformed word must exist in the word list. Note that begin_word is not a transformed word.

begin_word = "hit"
end_word = "cog"

return: ['hit', 'hot', 'cot', 'cog']

begin_word = "sail"
end_word = "boat"

['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

1. Translate into graphs terminology
    Node: words
    Edges: there's an edge if words are different by one letter an both are in the word list

DFS a better choice?
- Maybe if you want longest path or most relations
- Might be faster, since it goes to a leaf first

If visiting all nodes, then either will work, O(n)

- can do it recursely?