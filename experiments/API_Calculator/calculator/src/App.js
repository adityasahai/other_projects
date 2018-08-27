import React, { Component } from 'react';
import './App.css';
import { Button, ButtonToolbar } from 'react-bootstrap';

import { calcVal } from './utils';

class App extends Component {
  constructor() {
    super();

    this.state = {
      value: '0',
      operator: '',
      operand1: '',
      operand2: '',
      inProgress: false,
    };

    this.renderCalc = this.renderCalc.bind(this);
    this.onNumber = this.onNumber.bind(this);
    this.onOperator = this.onOperator.bind(this);
    this.onEqual = this.onEqual.bind(this);
    this.onAc = this.onAc.bind(this);
    this.logStateUpdate = this.logStateUpdate.bind(this);
  }

  logStateUpdate() {
    console.log(this.state);
  }

  onEqual() {
    if (this.state.inProgress) {
      const value = calcVal(this.state.value, this.state.operand2, this.state.operator);
      this.setState(
        prevState => ({
          ...prevState,
          value,
          operator: '',
          operand1: value,
          operand2: '',
          inProgress: true,
          operatorAdded: false,
        }),
        () => this.logStateUpdate(),
      );
    }
  }

  onNumber(event) {
    const val = event.target.value;
    const { inProgress, operatorAdded } = this.state;
    if (inProgress) {
      if (operatorAdded) {
        let { operand2 } = this.state;
        operand2 = `${operand2}${val}`;
        const value = calcVal(this.state.value, operand2, this.state.operator);
        this.setState(
          prevState => ({
            ...prevState,
            operand2,
            value,
          }),
          () => this.logStateUpdate(),
        );
      } else {
        let { operand1 } = this.state;
        operand1 = `${operand1}${val}`;
        this.setState(
          prevState => ({
            ...prevState,
            operand1,
            value: operand1,
          }),
          () => this.logStateUpdate(),
        );
      }
    } else {
      this.setState(
        prevState => ({
          ...prevState,
          operand1: val,
          value: val,
          inProgress: true,
        }),
        () => this.logStateUpdate(),
      );
    }
  }

  onOperator(event) {
    const val = event.target.value;
    const { inProgress, operatorAdded } = this.state;
    if (inProgress) {
      if (!operatorAdded) {
        this.setState(
          prevState => ({
            ...prevState,
            operator: val,
            operatorAdded: true,
          }),
          () => this.logStateUpdate(),
        );
      }
    }
  }

  onAc() {
    this.setState(
      prevState => ({
        ...prevState,
        operand1: '',
        operand2: '',
        operator: '',
        value: '0',
        inProgress: false,
        operatorAdded: false,
      }),
      () => this.logStateUpdate(),
    );
  }

  renderCalc() {
    return (
      <div>
        <input value={this.state.value} />
        <ButtonToolbar>
          <Button value="1" onClick={this.onNumber}>
            1
          </Button>
          <Button value="2" onClick={this.onNumber}>
            2
          </Button>
          <Button value="3" onClick={this.onNumber}>
            3
          </Button>
          <Button value="/" onClick={this.onOperator}>
            /
          </Button>
        </ButtonToolbar>
        <ButtonToolbar>
          <Button value="4" onClick={this.onNumber}>
            4
          </Button>
          <Button value="5" onClick={this.onNumber}>
            5
          </Button>
          <Button value="6" onClick={this.onNumber}>
            6
          </Button>
          <Button value="*" onClick={this.onOperator}>
            *
          </Button>
        </ButtonToolbar>
        <ButtonToolbar>
          <Button value="7" onClick={this.onNumber}>
            7
          </Button>
          <Button value="8" onClick={this.onNumber}>
            8
          </Button>
          <Button value="9" onClick={this.onNumber}>
            9
          </Button>
          <Button value="-" onClick={this.onOperator}>
            -
          </Button>
        </ButtonToolbar>
        <ButtonToolbar>
          <Button bsStyle="primary" onClick={this.onAc}>
            AC
          </Button>
          <Button value="00" onClick={this.onNumber}>
            00
          </Button>
          <Button value="0" onClick={this.onNumber}>
            0
          </Button>
          <Button value="+" onClick={this.onOperator}>
            +
          </Button>
        </ButtonToolbar>
        <ButtonToolbar>
          <Button onClick={this.onEqual}>=</Button>
        </ButtonToolbar>
      </div>
    );
  }

  render() {
    return <div className="App">{this.renderCalc()}</div>;
  }
}

export default App;
