

char * replaceDigits(char * s){
    for(char * ptr = s; *ptr; ptr++ ){
        if(isdigit(*ptr))
            *ptr = *(ptr - 1) + (*ptr - '0');
    }
    return s;
}