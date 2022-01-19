public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode answer = new ListNode();
        ListNode temp = new ListNode();
        answer.next = temp;
        int carry = 0;

        while (l1 != null || l2 != null){
            int digit = 0;
            if (l1 == null){
                digit = l2.val + carry;
                carry = 0;
                l2 = l2.next;
            }
            else if (l2 == null){
                digit = l1.val + carry;
                carry = 0;
                l1 = l1.next;
            }
            else{
                digit = l1.val + l2.val + carry;
                carry = 0;
                l1 = l1.next;
                l2 = l2.next;
            }
            if (digit > 9){
                carry = 1;
            }
            temp.val = digit % 10;
            if (l1 != null || l2 != null){
                temp.next = new ListNode();
                temp = temp.next;
            }
        }
        if (carry == 1)
            temp.next = new ListNode(carry);

        return answer.next;
    }
}
