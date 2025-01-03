function stringifyNumbers(obj) {
  if (typeof obj == "number") {
    return obj.toString();
  } else if (typeof obj != "object" || obj == null) {
    return obj;
  }

  var copy = Array.isArray(obj) ? obj.slice() : Object.assign({}, obj);

  var keys = Object.keys(copy);

  keys.forEach((key) => {
    copy[key] = stringifyNumbers(copy[key]);
  });

  return copy;
}

let obj = {
  num: 1,
  test: [1, false, "a"],
  data: {
    val: 4,
    info: {
      isRight: true,
      random: 66,
    },
  },
};

console.log(stringifyNumbers(obj));
console.log(obj);
