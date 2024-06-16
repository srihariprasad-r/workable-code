package src.JavaCollections;

import java.util.Iterator;
import java.util.LinkedList;

class Node {
    int data;
    Node next;
}

public class LinkedListClass extends Node implements Iterable<Integer>  {
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

    void insertAtEndNode(int val) {
        Node node = head;

        while ((node.next != null )) {
            node = node.next;
        }
        Node newNode = new Node();
        newNode.data = val;
        node.next = newNode;
        //newNode.next = node.next;
    }

    void insertAfterNode(int val, int afterNode) {
        Node node = head;
        Node prev = null;

        while ((node.next != null ) && (node.data != afterNode)) {
            prev = node;
            node = node.next;
        }
        Node newNode = new Node();
        newNode.data = val;
        prev.next = newNode;
        newNode.next = node.next;
    }

    public Iterator<Integer> iterator() {
        return new Iterator<Integer>() {
            Node node = head;

            @Override
            public boolean hasNext() {
                return node != null;
            }

            @Override
            public Integer next() {
                Node node = head;

                while (node.hasNext()) {
                    Integer data = node.v;
                }
            }
    }


    public static void main(String[] args) {
        LinkedListClass ls = new LinkedListClass();
        System.out.println("----Insert nodes into linked list-----");
        ls.addNewNode(2);
        ls.addNewNode(3);
        ls.addNewNode(4);
        ls.getNode();
        System.out.println("----Insert node after removing node in linked list-----");
        ls.insertAfterNode(5, 3);
        ls.getNode();
        System.out.println("----Insert node at the end in linked list-----");
        ls.insertAtEndNode(6);
        ls.getNode();
        ls.iterateLinkedList();
    }
}
