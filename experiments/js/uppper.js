function titleCase(str) {
  let newArr = [];
  str
    .toLowerCase()
    .split(' ')
    .forEach(e => newArr.push(`${e[0].toUpperCase()}${e.slice(1, e.length)}`));
  return newArr.join(' ');
}

console.log(titleCase("I'm a little tea pot"));
