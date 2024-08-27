之所以不推荐ContextAPI：every component that uses context API will rebuild will re-render when you switch something in that context. 一个context中会包含多个需要维护的state，任何变了，这个context包裹的子组件，都会被从新渲染。
Redux就没有这个问题，redux更复杂，但是可以做到精确到每个state，一个state变化时，跟这个state有关的子组件可以被单独渲染。

https://zhuanlan.zhihu.com/p/352522699
用户操作action
操作不直接更新状态
action被派遣dispatch，到一个中心交换所
其中包含了所有的状态更新相关的逻辑
redux用reducer函数，实现以上模式
当操作（action）被派遣（dispatch）时，reducer 函数被执行，其接受两个参数：当前状态和具体的动作，并据此返回新的状态

导入 reducer 函数以及相应的初始状态， 之后将创建并导出一个组件
1. 用 reducer 函数来创建和维护一个全局状态和对应的派遣
2. 返回一个更高阶的由 React.createContext 函数调用所产生的 Provider 组件。 并把状态和 dispatch 函数封装到一个数组中，并作为一个名称为 value 的 prop 传递给该高阶组件。


国王UI
action（deposit，100dollar）
bank是reducer，账户是store
仆人是action creator
发出action给老鹰，老鹰携带100dollar，飞到（dispatch）银行（reducer）