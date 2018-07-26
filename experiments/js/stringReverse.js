var stringReverse = (string) => {
  let newString = [];

  for (let s in string) {
    newString.unshift(string[s]);
  }
  return newString.join('');
}

console.log(typeof 'aditya');
console.log(stringReverse('aditya'));
