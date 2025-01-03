function collectStrings(obj) {
  if (typeof obj == "string") {
    return [obj];
  } else if (typeof obj != "object" || obj === null) {
    return [];
  }

  var keys = Object.keys(obj);

  var result = [];

  for (var key of keys) {
    result = result.concat(collectStrings(obj[key]));
  }

  return result;
}

const obj = {
  stuff: "foo",
  data: {
    val: {
      thing: {
        info: "bar",
        moreInfo: {
          evenMoreInfo: {
            weMadeIt: "baz",
          },
        },
      },
    },
  },
};

console.log(collectStrings(obj)); // ["foo", "bar", "baz"])
