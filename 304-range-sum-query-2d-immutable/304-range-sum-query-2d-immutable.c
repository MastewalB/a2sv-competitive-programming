typedef struct {
    int rowSize;
    int colSize;
    int ** prefix;
} NumMatrix;


NumMatrix* numMatrixCreate(int** matrix, int matrixSize, int* matrixColSize) {
    NumMatrix * numrix = (NumMatrix *)malloc(sizeof(NumMatrix));
    numrix->rowSize = matrixSize;
    numrix->colSize = matrixColSize[0];
    numrix->prefix = (int **)malloc(numrix->rowSize * sizeof(int *));
    
    for(int i = 0; i < matrixSize; i++){
        numrix->prefix[i] = (int *)malloc(numrix->colSize * sizeof(int));
        for(int j = 0; j < numrix->colSize; j++){
            if(j == 0)
                numrix->prefix[i][j] = matrix[i][j];
            else
                numrix->prefix[i][j] = matrix[i][j] + numrix->prefix[i][j - 1];
        }
    }
    return numrix;
}

int numMatrixSumRegion(NumMatrix* obj, int row1, int col1, int row2, int col2) {
    int total = 0;
    for(int i = row1; i <= row2; i++){
        total += obj->prefix[i][col2];
        if(col1 > 0)
            total -= obj->prefix[i][col1 - 1];
    }
    return total;
}

void numMatrixFree(NumMatrix* obj) {
     for (int r = 0; r < obj->rowSize; r++)
        free(obj->prefix[r]);
    free(obj->prefix);
    free(obj);
}

/**
 * Your NumMatrix struct will be instantiated and called as such:
 * NumMatrix* obj = numMatrixCreate(matrix, matrixSize, matrixColSize);
 * int param_1 = numMatrixSumRegion(obj, row1, col1, row2, col2);
 
 * numMatrixFree(obj);
*/