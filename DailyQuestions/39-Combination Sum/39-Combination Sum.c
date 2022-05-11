/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
void combine(int *candidates, int candidatesSize, int target, int **result, int *resultCount, int **resultColumnCount, int *buffer, int *bufferIndex, int startIndex);

int **combinationSum(int *candidates, int candidatesSize, int target, int *returnSize, int **returnColumnSizes)
{

    int **result = malloc(sizeof(int *) * 200);
    *returnColumnSizes = (int *)malloc(sizeof(int) * 200);
    int *buffer = (int *)malloc(sizeof(int) * 500);
    *returnSize = 0;
    int bufferIndex = 0;
    int startIndex = 0;

    combine(candidates, candidatesSize, target, result, returnSize, returnColumnSizes, buffer, &bufferIndex, startIndex);
    return result;
}

void combine(int *candidates, int candidatesSize, int target, int **result, int *resultCount, int **resultColumnCount, int *buffer, int *bufferIndex, int startIndex)
{
    if (target == 0)
    {
        result[*resultCount] = malloc(*bufferIndex * sizeof(int));
        memcpy(result[*resultCount], buffer, (*bufferIndex * sizeof(int)));
        resultColumnCount[0][*resultCount] = *bufferIndex;
        (*resultCount)++;
        return;
    }
    if (target < 0)
    {
        return;
    }
    if (startIndex >= candidatesSize)
    {
        return;
    }
    for (int i = startIndex; i < candidatesSize; i++)
    {
        buffer[(*bufferIndex)++] = candidates[i];
        combine(candidates, candidatesSize, target - candidates[i], result, resultCount, resultColumnCount, buffer, bufferIndex, i);
        (*bufferIndex)--;
    }
}