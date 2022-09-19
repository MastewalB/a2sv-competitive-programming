

bool judgeSquareSum(int c){
    int a = 0;
    double c_sqrt = sqrt(c);
    
    while(a < c_sqrt){
        int b = c - pow(a, 2);
        double b_sqrt = sqrt(b);
        if(floor(b_sqrt) == ceil(b_sqrt))
            return true;
        a++;
    }
    
    return (c == 0) ? true : false;
}