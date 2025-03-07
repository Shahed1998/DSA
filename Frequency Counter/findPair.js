function findPair(list, diff) {
  var obj = {};

  for (var i of list) {
    obj[i] = (obj[i] || 0) + 1;
  }

  if (diff === 0) {
    for (var num in obj) {
      if (obj[num] > 1) return true;
    }
    return false;
  }

  for (var num of list) {
    if (num - diff in obj || num + diff in obj) return true;
  }

  return false;
}

console.log(findPair([6], 0)); // false
console.log(findPair([6, 1, 4, 10, 2, 4], 2)); // true
console.log(findPair([8, 6, 2, 4, 1, 0, 2, 5, 13], 1)); // true
console.log(findPair([4, -2, 3, 10], -6)); // true
console.log(findPair([6, 1, 4, 10, 2, 4], 22)); // false
console.log(findPair([], 0)); // false
console.log(findPair([5, 5], 0)); // true
console.log(findPair([-4, 4], -8)); // true
console.log(findPair([-4, 4], 8)); // true
console.log(findPair([1, 3, 4, 6], -2)); // true
console.log(findPair([0, 1, 3, 4, 6], -2)); // true
