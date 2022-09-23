/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

bool compare(char ** target, char ** stamp, int start, int stampLen){
    for(int i = 0; i < stampLen; i++){
        if((*target)[start + i] == '*')
            continue;
        if((*target)[start + i] != (*stamp)[i])
            return false;
    }
    return true;
}

void reverse(int ** array, int length){
    int left = 0, right = length - 1;
    while(left < right){
        int temp = (*array)[left];
        (*array)[left++] = (*array)[right];
        (*array)[right--] = temp;
    }
}

bool changeLetters(char ** target, int start, int stampLen){
    bool changedAnything = false;
    for(int i = start; i < start + stampLen; i++){
        if((*target)[i] != '*')
            changedAnything = true;
        (*target)[i] = '*';
    }
    return changedAnything;
}

int* movesToStamp(char * stamp, char * target, int* returnSize){
    int stampLen = strlen(stamp), targetLen = strlen(target), tenFold = targetLen * 10;
    
    int * moves = (int *)malloc(sizeof(int) * (10 * targetLen));
    *returnSize = 0;
    bool continueFlag = true, changedAnything = true;
    
    
    while(continueFlag && *returnSize <= (tenFold)){
        continueFlag = false;
        changedAnything = false;
        for(int t = 0; t <= (targetLen - stampLen); t++){
            
            if(compare(&target, &stamp, t, stampLen)){
               if(changeLetters(&target, t, stampLen)){
                   moves[(*returnSize)++] = t;
                   continueFlag = true;
               }
            }
        }
    }
    
    for(int t = 0; t < targetLen; t++)
        if(target[t] != '*'){
            *returnSize = 0;
            return;
        }
    reverse(&moves, *returnSize);
    
    return moves;
}