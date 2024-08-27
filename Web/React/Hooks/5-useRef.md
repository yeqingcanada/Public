## useRef

- 访问 DOM 元素：你可以使用 useRef 创建一个引用来访问组件中的 DOM 元素。这在需要直接操作 DOM 的情况下非常有用，例如获取输入框的焦点、测量元素的尺寸或执行其他与 DOM 交互相关的任务。

```JavaScript
import React, { useRef, useEffect } from 'react';

function MyComponent() {
  const inputRef = useRef();

  useEffect(() => {
    inputRef.current.focus(); // 设置输入框焦点
  }, []);

  return <input ref={inputRef} />;
}
```

- 存储组件状态：与 useState 不同，useRef 创建的引用不会触发组件重新渲染。这使得它非常适合存储组件内部的数据，而不会导致重新渲染。

```JavaScript
import React, { useRef, useEffect } from 'react';

function MyComponent() {
  const count = useRef(0);

  useEffect(() => {
    count.current = count.current + 1; // 在不触发重新渲染的情况下更新 count
    console.log(`Count: ${count.current}`);
  }, []);

  // console会显示1，页面不会显示1，页面依然是0
  return <div>Count: {count.current}</div>;
}
```

- 在渲染之间共享数据：useRef 的值在每次组件渲染之间保持不变。这使得它成为在不触发重新渲染的情况下存储和共享数据的好方式。例如，在使用 setTimeout (用于在指定的延迟时间之后执行一个函数或一段代码) 或 setInterval (用于周期性地重复执行一个函数或一段代码，直到被取消) 时，可以在渲染之间保留计时器的 ID。

```JavaScript
import React, { useRef, useEffect } from 'react';

function MyComponent() {
  const timerId = useRef();

  useEffect(() => {
    timerId.current = setInterval(() => {
      console.log('Timer tick');
    }, 1000);

    return () => {
      clearInterval(timerId.current); // 在组件卸载时清除计时器
    };
  }, []);

  return <div>Timer is running...</div>;
}
```
