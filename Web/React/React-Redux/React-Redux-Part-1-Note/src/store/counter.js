import { createStore } from "redux";
import { createSlice, configureStore } from "@reduxjs/toolkit";

const initialCounterState = { counter: 0, showCounter: true };

/*方法二：使用@reduxjs/toolkit*/
const counterSlice = createSlice({
  name: "counter",
  initialState: initialCounterState,
  reducers: {
    increment(state) {
      state.counter++;
    },
    decrement(state) {
      state.counter--;
    },
    increase(state, action) {
      state.counter = state.counter + action.payload;
    },
    toggleCounter(state) {
      state.showCounter = !state.showCounter;
    },
  },
});

/*写法一：*/
// const store = createStore(counterSlice.reducer);

/*写法二：*/
/*这里reducer: 是固定写法，是configureStore需要传入的参数，它的值可以是单个也可以是多个reducer*/
// const store = configureStore({
//   reducer: counterSlice.reducer,
// });

/*写下面这句是为了，在component中可以引用reducer中的方法*/
export const counterActions = counterSlice.actions;

export default counterSlice.reducer;

/*方法一：不使用@reduxjs/toolkit*/
// const counterReducer = (state = initialCounterState, action) => {
//   if (action.type === "increment") {
//     return {
//       /*the reducer will not be merged with the existing state. they will overwrite the existing state*/
//       /*如果这里不写showCounter: state.showCounter，在点击increment的时候，会toggle not show，因为showCounter这时候是undefined，是false*/
//       /*另外，以下做法看起来work，实际不可取：
//       state.counter++
//       retrun state
//       因为不应该mutate the state, the existing state. you should never change the existing state. instead always override it by returning a brand new state object. because objects and arrays are reference values in JS, it is easy to accidentally override and change the existing state
//       */
//       counter: state.counter + 1,
//       showCounter: state.showCounter,
//     };
//   }
//   if (action.type === "increase") {
//     return {
//       counter: state.counter + action.amount,
//       showCounter: state.showCounter,
//     };
//   }
//   if (action.type === "decrement") {
//     return {
//       counter: state.counter - 1,
//       showCounter: state.showCounter,
//     };
//   }
//   if (action.type === "toggleCounter") {
//     return {
//       counter: state.counter,
//       showCounter: !state.showCounter,
//     };
//   }

//   return state;
// };

// const store = createStore(counterReducer);

// export default store;
