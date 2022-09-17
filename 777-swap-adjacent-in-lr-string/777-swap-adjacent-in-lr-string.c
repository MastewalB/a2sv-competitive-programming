char * replace_char(char * str, char find){
    char *original = str, *new = malloc((strlen(str) + 1) * sizeof(char));
    char * newPtr = new;
    while(*original){
        *new = *original++;
        new += (*new != find);
    }
    *new = '\0';
    return newPtr;
}
bool canTransform(char * start, char * end){
    int N = strlen(start);
    
    
    if(strcmp(replace_char(start, 'X'), replace_char(end, 'X')) != 0)
        return false;
    
    int i = 0, j = 0;
    while(i < N && j < N){
        while(i < N && start[i] == 'X')
            i++;
        while(j < N && end[j] == 'X')
            j++;
        
        if(i < N && ((start[i] == 'L' && i < j) || (start[i] == 'R' && i > j)))
            return false;
        i++;
        j++;
    }
    
    
    return true;
}