class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
       int m = matrix.length;
        int n = matrix[0].length;
        int processed = 0;
        int array_length = 0;
        List<Integer> output = new ArrayList<>(m*n);

        while (array_length < m * n){
            for (int i = processed; i < n - processed; i++) {
                output.add(matrix[processed][i]);
                array_length++;
            }
            for (int j = processed + 1; j < m - processed; j++){
                output.add(matrix[j][n - processed - 1]);
                array_length++;
            }
            if(array_length == m *n )
                break;
            
            for (int i = n - processed - 2; i > processed - 1; i--){
                output.add(matrix[m - processed - 1][i]);
                array_length++;
            }
            for (int j = m - processed - 2; j > processed; j--){
                output.add(matrix[j][processed]);
                array_length++;
            }
            if(array_length == m *n )
                break;
            processed++;
        }
        
        return output;
        
    }
}