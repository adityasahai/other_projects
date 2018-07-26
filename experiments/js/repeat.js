function repeatStringNumTimes(str, num) {
  // repeat after me
  for (let i = 0; i < num; i++) {
    str += str;
  }
  console.log(str);
  return str; 
}

repeatStringNumTimes("abc", 3);
