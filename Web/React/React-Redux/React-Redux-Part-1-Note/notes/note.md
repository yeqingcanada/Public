
how redux works
===========================================
component--->dispatch action--->reducer(state, action)--->store/state  
component NEVER change the store data  
it need REDUCER to manipulate the store(global state)  
但是 component 是如果trigger reducer的呢？通过dispatch action  
action只是简单的js object，which describe the kind of operation the reducers should perform  
so components dispatch actions, which describe what should be done, but don't do it directly,  
then these actions are forwarded to the reducer  
the reducer then does what the action wants the reducer to do  
then the reducer spits out吐出 a new state  


reducer
===========================================
input：old state + dispatched action  
output: new state object  
reducer 应该是pure function（same input leads to same output），不应该产生side effect（send HTTP/write something to local   storage/fetch something from local storage）inside the function  
a reducer should really just be a function that takes the given inputs, which are provided by Redux, and then produces the expected output, a new state object



example
===========================================
```javascript
const redux = require('redux');

const counterReducer = (state = { counter: 0 }, action) => {
  if(action.type==='increment'){
    return {
      counter: state.counter + 1
    }
  }
  if(action.type==='decrement'){
    return {
      counter: state.counter - 1
    }
  }
  return state 
}

// we pass the reducer to the redux.creatStore() function. store needs to know which reducer is responsible for changing that store
const store = redux.createStore(counterReducer);


const counterSubscriber = () => {
  const = latestState = store.getStste();
  console.log(latestState);
}

/*
now we just need to make redux aware of this subscriber function(counterSubscriber), tell it that this function(counterSubscriber) should be executed, whenever our state changes. 
and we do that by reaching out to the store, and calling the subscribe method on the store
the subscribe method then wants such a subscriber function(counterSubscriber), so the subscrib method expects a function which redux will then execute for us whenever the data in the store changed. 
so here we pass the counter subscriber to subscribe
*/
/*
不用加括号，因为both the reducer(createStore, subscribe), as well as the subscriber function will be executed by redux
*/
store.subscribe(counterSubscriber);

/*
create and dispatch an action
一般来说counterReducer中应该会有switch，选项就是不同的action
没有下面这句话，不会执行counterReducer中的内容，即使counterSubscriber这里有用到这个state。有了下面这个dispatch，就能够看到counterSubscriber中console的内容
*/
store.dispatch({ type: 'increment' })
store.dispatch({ type: 'decrement' })
```