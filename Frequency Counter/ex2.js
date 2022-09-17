function sameFrequency(num1, num2) {
  if (!(num1 > 0 && num2 > 0)) return false;
  let a = String(num1),
    b = String(num2);
  if (a.length !== b.length) return false;
  let paramDict = {};
  for (const i of a) !paramDict[i] ? (paramDict[i] = 1) : paramDict[i]++;
  for (const i of b) {
    if (!paramDict[i] || !paramDict[i] > 0) {
      return false;
    }
    paramDict[i]--;
  }

  return true;
}

console.log(sameFrequency(22, 222));
