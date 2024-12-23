function capitalizedWords(words, index = 0) {
  // add whatever parameters you deem necessary - good luck!
  if (words.length == index) return;
  words[index] = words[index].toUpperCase();
  capitalizedWords(words, ++index);
  return words;
}

let words = ["i", "am", "learning", "recursion"];
console.log(capitalizedWords(words)); // ['I', 'AM', 'LEARNING', 'RECURSION']
