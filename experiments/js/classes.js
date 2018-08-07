class Test {
  constructor(num) {
    this.value = num;
  }

  print() {
    console.log(this.value);
  }
}

arr = [1, 2, 3];

b = arr.map((e) => new Test(e));

console.log(b);
b.forEach((e) => console.log(e.print()));
