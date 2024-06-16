package src.JavaCollections;

class Node {
    int data;
    Node next;
}

public class LinkedListClass {
    Node head;
    Node tail;
    int size;

    void addNewNode(int value) {
        Node new_node = new Node();
        new_node.data = value;
        new_node.next = null;
        if (size == 0) {
            head = tail = new_node;
        } else {
            tail.next = new_node;
            tail = new_node;
        }
        size++;
    }

    public void getNode() {
        Node node = head;

        while (node != null) {
            System.out.println(node.data);
            node = node.next;
        }
    }

    public static void main(String[] args) {
        LinkedListClass ls = new LinkedListClass();
        ls.addNewNode(2);
        ls.addNewNode(3);
        ls.addNewNode(4);
        //System.out.println(newNode);
        ls.getNode();
    }
}
