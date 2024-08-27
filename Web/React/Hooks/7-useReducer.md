## useReducer

```JavaScript
import React, { useReducer } from 'react';

// 定义 reducer 函数，接受当前状态和操作，并返回新状态
function cartReducer(state, action) {
  switch (action.type) {
    case 'ADD_TO_CART':
      return {
        ...state,
        cartItems: [...state.cartItems, action.payload],
      };
    case 'REMOVE_FROM_CART':
      return {
        ...state,
        cartItems: state.cartItems.filter(item => item.id !== action.payload.id),
      };
    default:
      return state;
  }
}

function ShoppingCart() {
  // 使用 useReducer 初始化状态和 reducer 函数
  const [cartState, dispatch] = useReducer(cartReducer, { cartItems: [] });

  // 计算购物车中的总价
  const total = cartState.cartItems.reduce((acc, item) => acc + item.price, 0);

  return (
    <div>
      <h2>Shopping Cart</h2>
      <ul>
        {cartState.cartItems.map(item => (
          <li key={item.id}>
            {item.name} - ${item.price}
            <button onClick={() => dispatch({ type: 'REMOVE_FROM_CART', payload: item })}>
              Remove
            </button>
          </li>
        ))}
      </ul>
      <p>Total Price: ${total}</p>
      <button
        onClick={() =>
          dispatch({
            type: 'ADD_TO_CART',
            payload: { id: 1, name: 'Product A', price: 10 },
          })
        }
      >
        Add Product A to Cart
      </button>
    </div>
  );
}

export default ShoppingCart;
```
