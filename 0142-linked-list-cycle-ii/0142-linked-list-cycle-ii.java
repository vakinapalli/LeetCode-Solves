/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode a = head;
        ListNode b = head;
        boolean cyc = false;
        while(b != null && b.next != null){
            a = a.next;
            b = b.next.next;

            if(a == b){
                cyc = true;
                break;
            }

        }
        if(!cyc){
            return null;
        }
        ListNode c = head;
        while(a != c){
            a = a.next;
            c = c.next;
        }
        return c;
    }
}