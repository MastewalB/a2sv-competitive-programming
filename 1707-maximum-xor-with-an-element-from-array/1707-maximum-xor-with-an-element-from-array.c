#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int numCmp(const void * a, const void * b){
    return *(int *)a - *(int *)b;
}
int cmp(const void * a, const void * b){
    return (*(int **)a)[1] - (*(int **)b)[1];
}

typedef struct Trie{
    struct Trie * children[2];
}Trie;

Trie * trieCreate(){
    Trie * trie = (Trie *)malloc(sizeof(Trie));
    trie->children[0] = NULL;
    trie->children[1] = NULL;
    return trie;
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
        }else{
            curr = curr->children[val];
            if(curr == NULL) return -1;
        }
    }
    return result;
}


int* maximizeXor(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize){
    int * res = (int *)malloc(sizeof(int) * queriesSize);
    int ** queriesSorted = (int **)malloc(sizeof(int *) * queriesSize);
    *returnSize = queriesSize;
    
    for(int i = 0; i < queriesSize; i++){
        queriesSorted[i] = (int *)malloc(sizeof(int) * 3);
        queriesSorted[i][0] = queries[i][0];
        queriesSorted[i][1] = queries[i][1];
        queriesSorted[i][2] = i;
    }
    
    qsort(queriesSorted, queriesSize, sizeof(int **), cmp);
    qsort(nums, numsSize, sizeof(int), numCmp);
    
    Trie * trie = trieCreate();

    int j = 0;
    for(int i = 0; i < queriesSize; i++){
        
        while(j < numsSize && nums[j] <= queriesSorted[i][1]){
            trieInsert(trie, nums[j]);
            j++;
        }
        
        res[queriesSorted[i][2]] = trieSearch(trie, queriesSorted[i][0]);
    }
    return res;
}












