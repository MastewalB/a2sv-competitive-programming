/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

void changeSign(struct ListNode * head){
    while(head){
        head->val *= -1;
        head = head->next;
    }
}
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    changeSign(headA);
    while(headB){
        if(headB->val < 0) break;
        headB = headB->next;
    }
    changeSign(headA);
    return headB;
}