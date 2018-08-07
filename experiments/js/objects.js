let users = [
  {
    age: 27,
    online: true,
  },
  {
    age: 32,
    online: true,
  },
  {
    age: 48,
    online: true,
  },
  {
    age: 19,
    online: true,
  },
];

console.log(users.reduce((val, u) => val && u.online));
