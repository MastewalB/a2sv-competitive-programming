

char * shiftingLetters(char * s, int* shifts, int shiftsSize){
    int N = strlen(s);
    
    for(int i = shiftsSize - 2; i > -1; i--)
        shifts[i] += (shifts[i + 1] % 26);
    
    for(int i = 0; i < N; i++){
        int curr = ((s[i] - 'a') + shifts[i]) % 26;
        s[i] = (curr >= 0) ? 97 + curr : 123 + curr;
    }
    return s;
}