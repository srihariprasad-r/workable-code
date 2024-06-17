package src.JavaCollections;

class NodeDLL {
    int data;
    NodeDLL nxt;
    NodeDLL prev;
}

class formLinkedList {
    NodeDLL head;
    NodeDLL tail;
    int size;

    void addNode(int val) {
        NodeDLL new_node = new NodeDLL();
        new_node.data = val;
        new_node.nxt = null;

        if (size == 0) {
            head = tail = new_node;
            tail.nxt = null;
            head.prev = null;
            size++;
        } else {
            tail.nxt = new_node;
            new_node.prev = tail;
            tail = new_node;
            tail.nxt = null;
        }
    }

    void displayNodes() {
        NodeDLL node = head;

        while (node != null) {
            System.out.println(node.data);
            node = node.nxt;
        }
    }
}


class DoublyLinkedListClass {
    public static void main(String[] args) {
        formLinkedList dl = new formLinkedList();
        dl.addNode(2);
        dl.addNode(3);
        dl.displayNodes();
    }
}
