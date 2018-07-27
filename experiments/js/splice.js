function frankenSplice(arr1, arr2, n) {
  // It's alive. It's alive!
  let arr3 = [...arr2];
  arr1.forEach(e => {
    arr3.splice(n, 0, e);
    n++;
  });
  console.log(arr3);
  return arr3;
}
frankenSplice([1, 2, 3], [4, 5, 6], 1);
