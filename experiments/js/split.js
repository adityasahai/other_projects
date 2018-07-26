function findLongestWordLength(str) {
  let words = str.split(' ');
  let max = words[0].length;
  for (let i = 1; i < words.length; i++) {
    console.log(words[i] + ' ' + words[i].length);
    if (max < words[i].length) {
      max = words[i].length;
    }
  }
  console.log(max);
  return max;
}

findLongestWordLength("The quick brown fox jumped over the lazy dog");
