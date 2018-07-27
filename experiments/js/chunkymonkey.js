function chunkArrayInGroups(arr, size) {
  // Break it up.
  let retArr = [];
  for (let n = 0; n < arr.length; n += size) {
    retArr.push(arr.slice(n, n + size));
  }
  console.log(retArr);
  return retArr;
}

chunkArrayInGroups(['a', 'b', 'c', 'd'], 2);
chunkArrayInGroups([0, 1, 2, 3, 4, 5], 4);
