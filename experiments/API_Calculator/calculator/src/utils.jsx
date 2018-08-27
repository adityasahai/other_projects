import React from 'react';

export function calcVal(op1, op2, op) {
  switch (op) {
    case '/':
      return (Number.parseFloat(op1, 10) / Number.parseFloat(op2, 10)).toString();
      break;
    case '*':
      return (Number.parseFloat(op1, 10) * Number.parseFloat(op2, 10)).toString();
      break;
    case '+':
      return (Number.parseFloat(op1, 10) + Number.parseFloat(op2, 10)).toString();
      break;
    case '-':
      return (Number.parseFloat(op1, 10) - Number.parseFloat(op2, 10)).toString();
      break;
  }
}
