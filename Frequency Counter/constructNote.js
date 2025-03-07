function constructNote(message, letters) {
  // add whatever parameters you deem necessary - good luck!
  var obj = {};

  for (var i of letters) {
    if (i in obj) obj[i] += 1;
    else obj[i] = 1;
  }

  for (var i of message) {
    if (i in obj && obj[i] > 0) {
      obj[i] -= 1;
    } else {
      return false;
    }
  }
  return true;
}

console.log(constructNote("aa", "abc")); // false
console.log(constructNote("abc", "dcba")); // true
console.log(constructNote("aabbcc", "bcabcaddff")); // true
