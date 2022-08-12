

double myPow(double x, int n){
    if(n == 0)
        return 1;
    
    double half = myPow(x, n / 2);
    
    return (n % 2 == 0) ? half * half : (n > 0) ? half * half * x : half * half * (1 / x);
    
}