function findAllDuplicates(list) {
  var obj = {};
  var duplicateList = [];

  for (var i of list) {
    if (i in obj) {
      duplicateList.push(i);
    } else obj[i] = 1;
  }

  return duplicateList;
}

findAllDuplicates([4, 3, 2, 7, 8, 2, 3, 1]); // array with 2 and 3
findAllDuplicates([4, 3, 2, 1, 0]); // []
findAllDuplicates([4, 3, 2, 1, 0, 1, 2, 3]); // array with 3, 2, and 1
