function factorialize(num) {
  if (num == 1)
    return 1
  return num * factorialize(num - 1);
}

console.log(factorialize(5));
console.log(factorialize(20));
