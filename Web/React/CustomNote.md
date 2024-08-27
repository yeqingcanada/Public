1. 这个页面会改变的数据，需要这个页面的 state / 父组件中的 state 来管理
   1. 如果由父组件的 state 控制，就往上 trigger setState。子组件就不用自己的 state，就直接用父组件的 state
   2. 如果子组件有自己的 state，就用自己的 state，不需要向上 trigger 父组件的 setState(父组件的数据是来自 redux 的，会被 dispatch 维护)
   3. 要找到数据源头，确保每种数据都有被维护，不论是 state 还是 redux
2. 任何变化后
   1. 通知后端(可以当前页直接，如果有复用，可以传回上几级进行后端通信，这两种没有区别)
   2. 通知 redux，类似通知后端，在那个层级通知 redux 没有影响
