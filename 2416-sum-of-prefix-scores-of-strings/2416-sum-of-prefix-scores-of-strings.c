#define CHAR_SIZE 26

typedef struct{
    bool isLeaf;
    struct Trie * children[CHAR_SIZE];
    int visitedCount;
} Trie;

Trie * trieCreate(){
    Trie * trieNode = (Trie *)malloc(sizeof(Trie));
    trieNode->isLeaf = false;
    trieNode->visitedCount = 0;
    for(int i = 0; i < CHAR_SIZE; i++)
        trieNode->children[i] = NULL;
    return trieNode;
}

void trieInsert(Trie * trieNode, char * word){
    Trie * currNode = trieNode;
    while(*word){
        if(currNode->children[*word - 'a'] == NULL)
            currNode->children[*word - 'a'] = trieCreate();
        currNode = currNode->children[*word - 'a'];
        currNode->visitedCount++;
        word++;
    }
    currNode->isLeaf = true;
}


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumPrefixScores(char ** words, int wordsSize, int* returnSize){
    *returnSize = wordsSize;
    int * response = (int *)malloc(wordsSize * sizeof(int));
    Trie * trie = trieCreate();
    
    for(int i = 0; i < wordsSize; i++){
        trieInsert(trie, words[i]);
    }
    
    for(int i = 0; i < wordsSize; i++){
        Trie * currNode = trie;
        int total = 0;
        while(*words[i]){
            currNode = currNode->children[*words[i] - 'a'];
            total += currNode->visitedCount;
            *words[i]++;
        }
        response[i] = total;
    }
    
    return response;

}