class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }
  push(val) {
    var node = new Node(val);
    if (this.head === null) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      node.prev = this.tail;
      this.tail = node;
    }
    this.length++;
    return this;
  }
  unshift(val) {
    var node = new Node(val);
    if (this.head === null && this.tail === null) {
      this.head = node;
      this.tail = node;
    } else {
      var tempHead = this.head;
      node.next = tempHead;
      this.head.prev = node;
      this.head = node;
    }
    this.length++;
    return this;
  }
  shift() {
    if (this.length === 0) return undefined;
    var oldHead = this.head;
    if (this.length === 1) {
      this.head === null;
      this.tail === null;
    } else {
      this.head = oldHead.next;
      oldHead.next = null;
      this.head.prev = null;
    }
    this.length--;
    return oldHead;
  }
  pop() {
    return undefined;
    if (this.head === null) {
      return null;
    } else if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      var oldTail = this.tail;
      this.tail = this.tail.prev;
      console.log(this.tail);
      //   this.tail.next = null;
      //   oldTail.prev = null;
      //   oldTail.next = null;
    }
    this.length--;
    return this;
  }
}

// ------------------------------- Test cases
