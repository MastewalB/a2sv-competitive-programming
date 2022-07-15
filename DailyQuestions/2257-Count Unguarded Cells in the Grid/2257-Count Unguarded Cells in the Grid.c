#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool inBound(int x, int y, int m, int n) {
  return (0 <= x && x < m && 0 <= y && y < n);
}

int countUnguarded(int m, int n, int **guards, int guardsSize,
                   int *guardsColSize, int **walls, int wallsSize,
                   int *wallsColSize) {
  int **grid = (int **)malloc(m * sizeof(int **));

  int directions[4][2] = {{0, -1}, {-1, 0}, {1, 0}, {0, 1}};

  for (int i = 0; i < m; i++)
    grid[i] = (int *)calloc(n, sizeof(int));

  for (int i = 0; i < wallsSize; i++)
    grid[walls[i][0]][walls[i][1]] = 1;

  for (int i = 0; i < guardsSize; i++)
    grid[guards[i][0]][guards[i][1]] = 1;

  int guarded = 0;
  for (int i = 0; i < guardsSize; i++) {
    grid[guards[i][0]][guards[i][1]] = 1;

    for (int d = 0; d < 4; d++) {

      int count = 1;
      int g = 0;
      while (true) {
        int new_x = guards[i][0] + (count * directions[d][0]);
        int new_y = guards[i][1] + (count * directions[d][1]);
        if (!inBound(new_x, new_y, m, n) || grid[new_x][new_y] == 1)
          break;
        if (grid[new_x][new_y] != -1)
          g++;
        grid[new_x][new_y] = -1;
        count++;
      }
      guarded += g;
    }
  }

  return (m * n) - (guarded + guardsSize + wallsSize);
}