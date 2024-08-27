## useImperativeHandle

```JavaScript
import React, { forwardRef, useImperativeHandle, useRef } from 'react';

// 子组件
const ChildComponent = forwardRef((props, ref) => {
  const internalRef = useRef(null);

  // 使用 useImperativeHandle 定义向父组件暴露的方法
  useImperativeHandle(ref, () => ({
    // 暴露的方法1
    doSomething: () => {
      console.log('ChildComponent is doing something.');
    },
    // 暴露的方法2
    getValue: () => {
      return internalRef.current.value;
    },
  }));

  return (
    <input
      ref={internalRef}
      type="text"
      placeholder="Type something..."
    />
  );
});

export default ChildComponent;
```

```JavaScript
import React, { useRef } from 'react';
import ChildComponent from './ChildComponent';

function ParentComponent() {
  const childRef = useRef(null);

  const handleButtonClick = () => {
    // 使用子组件的方法
    childRef.current.doSomething();
    const value = childRef.current.getValue();
    console.log('Value from ChildComponent:', value);
  };

  return (
    <div>
      <h2>Parent Component</h2>
      <ChildComponent ref={childRef} />
      <button onClick={handleButtonClick}>Do Something</button>
    </div>
  );
}

export default ParentComponent;
```
