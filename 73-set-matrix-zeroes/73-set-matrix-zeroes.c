

void setZeroes(int** matrix, int matrixSize, int* matrixColSize){
    int r = false, c = false;
    int matColSize = matrixColSize[0];
    
    for(int i = 0; i < matColSize; i++)
        if(matrix[0][i] == 0) r = true;
    for(int j = 0; j < matrixSize; j++)
        if(matrix[j][0] == 0) c = true;
    
    for(int i = 1; i < matrixSize; i++){
        for(int j = 1; j < matColSize; j++){
            if(matrix[i][j] == 0){
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }
    
    for(int i = 1; i < matrixSize; i++){
        for(int j = 1; j < matColSize; j++){
            if(matrix[i][0] == 0 || matrix[0][j] == 0){
                matrix[i][j] = 0;
            }
        }
    }
    
    if(r)
       for(int i = 0; i < matColSize; i++)
            matrix[0][i] = 0;
    if(c)
        for(int j = 0; j < matrixSize; j++)
            matrix[j][0] = 0;
        
}