
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* corpFlightBookings(int** bookings, int bookingsSize, int* bookingsColSize, int n, int* returnSize){
    
    int * flights = (int *)calloc(n + 1, sizeof(int));
    *returnSize = n;
    
    for(int i = 0; i < bookingsSize; i++){
        flights[bookings[i][0] - 1] += bookings[i][2];
        flights[bookings[i][1]] -= bookings[i][2];
    }
    
    for(int i = 0; i < n; i++)
        if(i > 0)
            flights[i] += flights[i - 1];
    
    return flights;
    
}