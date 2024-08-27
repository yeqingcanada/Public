JavaScript 中两种事件传播模式：

1. Capturing/trickling 从外向内
2. Bubbling 从内向外，默认模式

多个元素在页面上重叠，点击重叠部分，trigger 事件顺序，默认 bubbling，最先触发最内元素绑定的事件

我上面的例子中没有涉及到点击 click 链接，为什么呢？大家可以试一下，点击 click 会发生什么？它会又立即跳转到了当前页面(因为我们 href 是一个空连接，这是链接元素的一个默认特性)，虽然我们的监听函数被执行了，但是有时候我们不想这个默认特性被执行，比如，我们可能想在监听函数里面改变 div 的背景颜色等等，这样如果这个链接元素 a 默认特性的存在就会立即“刷新”了该页面，让我们的改变背景颜色无法进行。

event.stopPropagation(); 传播链就会终止，只触发第一层级的事件，不触发按照默认 bubbling 顺序或者非默认 trickling 顺序的下一个事件

Target vs. currentTarget:target 一直是中间一层，currentTarget 第一次是中间一层，第二次是外面一层 JS Event target versus currentTarget

- 变量名，小驼峰

- common js functions
- 将一个包含 object 的 array 变成一个只包含 object 的 value 的 array

```javascript
let result = objArray.map((a) => a.foo);
let result = objArray.map(({ foo }) => foo);
```

- array of object,生成一个新 array/object，由原 array 转换而来  
  data: array of object  
  dataValidate: 新的 array，只包含一部分 key：value  
  reduce 是遍历 array，累积结果。assign 是 merge 累积的结果

```javascript
var dataValidate = data.reduce(
  (obj, item) => Object.assign(obj, { [item.input_list_category]: item.value }),
  {}
);
var dataValidate = data.reduce(
  (array, item) =>
    array.concat({
      Header: item.title,
      accessor: item.title.replace(/\s/g, ""),
    }),
  []
);
```

- 遍历 object  
  let [key, value] of Object.entries(object)

- indexOf vs. findIndex  
  区别是参数列表，第一个需要一个值/object，第二个需要一个函数

- 将 array 的每个 object 元素添加一个新的 attribute  
  新建一个 array，将原 array 中的元素 element 写入，并且加入新 attribute description

```javascript
siteChangeOfCapacityData.forEach((element) => {
  const selectedCurrentLkuSiteMaster = tableData.find(
    (tableDataElement) =>
      tableDataElement.system === element.system &&
      tableDataElement.site === element.site &&
      tableDataElement.plant === element.plant &&
      tableDataElement.whno === element.whno &&
      tableDataElement.systemarea === element.systemarea
  );
  element["description"] = selectedCurrentLkuSiteMaster.description;
});
```
