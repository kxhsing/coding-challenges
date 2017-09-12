function LinkedList() {
    this.head = null;
    this.tail = null;
}

function Node(value, next, prev) {
    this.value = value;
    this.next = next;
    this.prev = prev;
}

LinkedList.prototype.push = function(value) {
    var newNode = new Node(value, this.head, null);
    if (this.head) {
        this.head.prev = newNode;
    }
    else {
        this.tail = newNode;
    }

    this.head = newNode;

}

LinkedList.prototype.pop = function() {
    if (!this.head) {
    return null;
    }
    var val = this.head.val;
    this.head = this.head.next;

    if (this.head) {
    this.head.prev = null;
    }
    else {
    this.tail = null;
    }

    return val;
}

LinkedList.prototype.peek = function() {
    if (!this.head) {
    return null;
    }
    else return this.head.value;
}