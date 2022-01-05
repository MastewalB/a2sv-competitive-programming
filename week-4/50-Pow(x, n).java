class Solution {
    public double myPow(double x, int n) {
        if(x == 0) return 0;
        if(n == 0) return 1;
        if(n == 1) return x;
        if(n ==-1) return 1 / x;
        
        double y = myPow(x, n / 2);
        if(n % 2 == 0) return (double)Math.round(y * y * 1000000d) / 1000000d;
        return (double)Math.round(x * y * y * 1000000d) / 1000000d;
    }
}