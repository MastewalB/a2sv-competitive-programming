/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

void invert(struct TreeNode * node){
    if(node == NULL)
        return;
    invert(node->left);
    invert(node->right);
    
    struct TreeNode * left = node->left;
    node->left = node->right;
    node->right = left;
    
}

struct TreeNode* invertTree(struct TreeNode* root){
    invert(root);
    return root;
}