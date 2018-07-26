function arrayMax(arr) {
  return arr.reduce((a, b) => {
    if (a > b)
      return a;
    return b;
  });
}

function largestOfFour(arr) {
  // You can do this!
  let newArr = []
  arr.filter((e) => newArr.push(arrayMax(e)));
  return newArr;
}
console.log(largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]));
