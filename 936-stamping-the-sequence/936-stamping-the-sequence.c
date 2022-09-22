

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */


void reverse(int ** array, int length){
    int left = 0, right = length - 1;
    while(left < right){
        int temp = (*array)[left];
        (*array)[left++] = (*array)[right];
        (*array)[right--] = temp;
    }
}

int* movesToStamp(char * stamp, char * target, int* returnSize){
    int stampLen = strlen(stamp);
    int targetLen = strlen(target);
    int tenFold = targetLen * 10;
    
    int * moves = (int *)malloc(sizeof(int) * (10 * targetLen));
    *returnSize = 0;
    bool continueFlag = true, changedAnything = true;
    
    
    while(continueFlag && *returnSize <= (tenFold)){
        continueFlag = false;
        changedAnything = false;
        for(int t = 0; t <= (targetLen - stampLen); t++){
            bool completeFlag = true;
            
            
            for(int s = 0; s < stampLen; s++){
                if(target[t + s] == '*')
                    continue;
                if(target[t + s] != stamp[s]){
                    completeFlag = false;
                    break;
                }
                
            }
            
            if(completeFlag){
                for(int i = t; i < t + stampLen; i++){
                    if(target[i] != '*')
                        changedAnything = true;
                    target[i] = '*';
                }

                moves[(*returnSize)++] = t;
            }
        }
        
        if(changedAnything)
            continueFlag = true;
        
    }
    
    
    for(int t = 0; t < targetLen; t++)
        if(target[t] != '*'){
            *returnSize = 0;
            return;
        }
    
    reverse(&moves, *returnSize);
    
    return moves;
}