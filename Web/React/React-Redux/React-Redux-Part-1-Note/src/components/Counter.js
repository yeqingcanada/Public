import { React } from "react";
import { useSelector, useDispatch } from "react-redux";

import { counterActions } from "../store/counter";
import classes from "./Counter.module.css";

const Counter = () => {
  const dispatch = useDispatch();
  const counter = useSelector((state) => state.counter.counter);
  const showCounter = useSelector((state) => state.counter.showCounter);

  const toggleCounterHandler = () => {
    // dispatch({ type: "toggleCounter" });
    dispatch(counterActions.toggleCounter());
  };

  const incrementHandler = () => {
    /*dispatch方法一*/
    // dispatch({ type: "increment" });
    /*dispatch方法二*/
    dispatch(counterActions.increment());
  };

  /*Attaching Payloads to Actions*/
  const increaseHandler = () => {
    // dispatch({ type: "increase", amount: 10 });
    dispatch(counterActions.increase(10)); // { type: SOME_UNIQUE_IDENTIFIER, payload: 10 }
  };

  const decrementHandler = () => {
    // dispatch({ type: "decrement" });
    dispatch(counterActions.decrement());
  };

  return (
    <main className={classes.counter}>
      <h1>Redux Counter</h1>
      {showCounter && <div className={classes.value}>{counter}</div>}
      <div>
        <button onClick={incrementHandler}>Increment</button>
        <button onClick={increaseHandler}>Increase by 10</button>
        <button onClick={decrementHandler}>Decrement</button>
      </div>
      <button onClick={toggleCounterHandler}>Toggle Counter</button>
    </main>
  );
};

export default Counter;
