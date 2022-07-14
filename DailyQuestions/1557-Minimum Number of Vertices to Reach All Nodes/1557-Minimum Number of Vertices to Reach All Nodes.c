#include <stdio.h>
#include <stdlib.h>

int *findSmallestSetOfVertices(int n, int **edges, int edgesSize,
                               int *edgesColSize, int *returnSize) {
  int *hasIncoming = (int *)calloc(n, sizeof(int));
  int *result = (int *)malloc(n * sizeof(int));

  for (int i = 0; i < edgesSize; i++) {
    hasIncoming[edges[i][1]] = 1;
  }
  int index = 0;
  for (int j = 0; j < n; j++) {
    if (!hasIncoming[j])
      result[index++] = j;
  }

  *returnSize = index;
  return result;
}