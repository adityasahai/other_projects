function getIndexToIns(arr, num) {
  // Find my place in this sorted array.
  arr.sort();
  console.log(arr);
  let i = 0;
  for (i = 0; i < arr.length; i++) {
    if (arr[i] >= num) {
      return i;
    }
  }
  return i;
}

console.log(getIndexToIns([5, 3, 20, 3], 5));
