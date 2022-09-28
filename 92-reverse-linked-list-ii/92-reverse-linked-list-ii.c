/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseBetween(struct ListNode* head, int left, int right){
    if(left == right)
        return head;
    int N = right - left + 1;
    
    int * nodes = (int *)malloc(sizeof(int) * N);
    struct ListNode * curr = head;
    struct ListNode * leftNode = head;
    
    
    int count = 0, index = 0;
    while(count <= right - 1){
        count++;
        if(count == left)
            leftNode = curr;
        if(count >= left && count <= right)
            nodes[index++] = curr->val;
        curr = curr->next;
    }
    
    for(int i = 0; i < N; i++){
        leftNode->val = nodes[N - i - 1];
        leftNode = leftNode->next;
    }
    return head;
}