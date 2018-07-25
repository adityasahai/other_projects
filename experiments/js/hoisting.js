/* The following works */

var catName = word => {
  console.log(`my cat says ${word}`);
};

catName('wat!');

/* The following does not because only declarations are hoisted,
   not initilizations */

catName('wat!');

var catName = word => {
  console.log(`my cat says ${word}`);
};
