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

  insert(index, val) {
    if (index < 0 || index >= this.length) {
      return false;
    } else if (index === 0) {
      return this.unshift(val);
    } else if (index === this.length - 1) {
      return this.push(val);
    } else {
      var node = new Node(val);
      var prevNode = this.get(index - 1);
      node.next = prevNode.next;
      prevNode.next = node;
      node.prev = prevNode;
      node.next.prev = node;
      this.length++;
      return true;
    }
  }

  remove(index) {
    if (index < 0 || index >= this.length) {
      return undefined;
    } else if (index === 0) {
      return this.shift();
    } else if (index === this.length - 1) {
      return this.pop();
    } else {
      var prevNode = this.get(index - 1);
      var remNode = prevNode.next;
      prevNode.next = remNode.next;
      remNode.prev = null;
      remNode.next = null;
      this.length--;
      return remNode;
    }
  }
  pop() {
    if (this.length === 0) {
      return undefined;
    } else if (this.length === 1) {
      this.length--;
      return this.head;
    } else {
      var oldTail = this.tail;
      this.tail = oldTail.prev;
      this.tail.next = null;
      oldTail.next = null;
      oldTail.prev = null;
      this.length--;
      return oldTail;
    }
  }
  reverse() {}
}

// ------------------------------- Test cases
let doublyLinkedList = new DoublyLinkedList();
doublyLinkedList.push(5).push(10).push(15).push(20);
doublyLinkedList.reverse(); // singlyLinkedList;
doublyLinkedList.length; // 4
doublyLinkedList.head.val; // 20
doublyLinkedList.head.next.val; // 15
doublyLinkedList.head.next.next.val; // 10
doublyLinkedList.head.next.next.next.val; // 5
