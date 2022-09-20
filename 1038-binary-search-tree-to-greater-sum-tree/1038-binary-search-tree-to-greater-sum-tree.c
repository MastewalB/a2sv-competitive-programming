/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int greaterSum(struct TreeNode * root, int sum){
    if(root == NULL)
        return sum;
    root->val += greaterSum(root->right, sum);
    return greaterSum(root->left, root->val);
}

struct TreeNode* bstToGst(struct TreeNode* root){
    greaterSum(root, 0);
    return root;
}