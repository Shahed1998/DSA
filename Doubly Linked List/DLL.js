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
  }
  get(index) {
    if (this.length <= 0 || index >= this.length || index < 0) {
      return null;
    }
    var mid = Math.floor(this.length / 2);
    if (index <= mid) {
      var current = this.head;
      for (let i = 0; i < index + 1; i++) {
        if (i === index) {
          return current;
        }
        current = current.next;
      }
    } else if (index > mid) {
      var current = this.tail;
      for (let i = this.length - 1; index - 1; i--) {
        if (i === index) {
          return current;
        }
        current = current.prev;
      }
    }
  }
  set(index, value) {
    var node = this.get(index);
    if (node === false) {
      return false;
    }
    node.val = value;
    return true;
  }
  remove() {}
  pop() {}
}

// ------------------------------- Test cases
// var doublyLinkedList = new DoublyLinkedList();

// doublyLinkedList.push(5).push(10).push(15).push(20);
// doublyLinkedList.get(0).val; // 5
// doublyLinkedList.get(1).val; // 10
// doublyLinkedList.get(2).val; // 15
// doublyLinkedList.get(3).val; // 20
// console.log(doublyLinkedList.get(4)); // null
