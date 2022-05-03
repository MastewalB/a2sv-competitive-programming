# 720. Longest Word in Dictionary

We can use a Trie to store and look up words easily.
For every word in the List, we can check if the word without the last letter exists(hence building up one character at a time), and if it does, we can add the word to our dictionary increasing our length record.