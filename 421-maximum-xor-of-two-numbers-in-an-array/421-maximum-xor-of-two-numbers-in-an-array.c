#define MAX(a, b) (((a) > (b)) ? (a) : (b))
typedef struct Trie{
    struct Trie * children[2];
}Trie;

Trie * trieCreate(){
    Trie * trieNode = (Trie *)malloc(sizeof(Trie));
    for(int i = 0; i < 2; i++)
        trieNode->children[i] = NULL;
    return trieNode;
}

void trieInsert(Trie * trie, int number){
    Trie * curr = trie;
    for(int i = 31; i >= 0; i--){
        int val = (number >> i) & 1;
        if(curr->children[val] == NULL)
            curr->children[val] = trieCreate();
        curr = curr->children[val];
    }
}

int trieSearch(Trie * trie, int number){
    Trie * curr = trie;
    int result = 0;
    
    for(int i = 31; i >= 0; i--){
        int val = (number >> i) & 1;
        if(curr->children[1 - val] != NULL){
            result |= (1 << i);
            curr = curr->children[1 - val];
        }else 
            curr = curr->children[val];
    }
    
    return result;
}

int findMaximumXOR(int* nums, int numsSize){
    Trie * trie = trieCreate();
    int result = 0;
    
    for(int i = 0; i <numsSize; i++)
        trieInsert(trie, nums[i]);
    
    for(int i = 0; i <numsSize; i++)
        result = MAX(result, trieSearch(trie, nums[i]));
    
    return result;
}