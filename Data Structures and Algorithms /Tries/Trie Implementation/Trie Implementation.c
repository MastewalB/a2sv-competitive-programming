#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define CHAR_SIZE 26

typedef struct
{
    bool isLeaf;
    struct Trie *children[CHAR_SIZE];
} Trie;

Trie *trieCreate()
{
    Trie *node = (Trie *)malloc(sizeof(Trie));
    node->isLeaf = false;
    for (int i = 0; i < CHAR_SIZE; i++)
        node->children[i] = NULL;
    return node;
}

void trieInsert(Trie *obj, char *word)
{
    Trie *curr = obj;
    while (*word)
    {
        if (curr->children[*word - 'a'] == NULL)
            curr->children[*word - 'a'] = trieCreate();
        curr = curr->children[*word - 'a'];
        word++;
    }
    curr->isLeaf = 1;
}

bool trieSearch(Trie *obj, char *word)
{
    if (obj == NULL)
        return false;

    Trie *curr = obj;
    while (*word)
    {
        curr = curr->children[*word - 'a'];
        if (curr == NULL)
            return false;
        word++;
    }
    return curr->isLeaf;
}

bool trieStartsWith(Trie *obj, char *prefix)
{
    if (obj == NULL)
        return false;
    Trie *curr = obj;
    while (*prefix)
    {
        curr = curr->children[*prefix - 'a'];
        if (curr == NULL)
        {
            return false;
        }
        prefix++;
    }
    return true;
}

void trieFree(Trie *obj)
{
    int i;
    if (!obj)
    {
        return;
    }

    for (i = 0; i < CHAR_SIZE; i++)
    {
        obj->children[i] = NULL;
    }
    free(obj);
}

/**
 * Your Trie struct will be instantiated and called as such:
 * Trie* obj = trieCreate();
 * trieInsert(obj, word);

 * bool param_2 = trieSearch(obj, word);

 * bool param_3 = trieStartsWith(obj, prefix);

 * trieFree(obj);
*/