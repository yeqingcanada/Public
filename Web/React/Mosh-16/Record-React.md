- 1-Getting Started
- 2-ES6 Refresher
- 3-Components
- 4-Composing Components
- 5-Pagination, Filtering, and Sorting
- 6-Routing
- 7-Forms
- 8-Calling Backend Services
- 9-Authentication and Authorization
- 10-Deployment
- 11-Advanced Topics

# Table of contents

- [Table of contents](#table-of-contents)
- [1-Getting-Started](#1-getting-started)
  - [2](#2)
  - [3- Your First React App](#3--your-first-react-app)
  - [5- Custom Configs](#5--custom-configs)
- [2-ES6-Refresher](#2-es6-refresher)
  - [2- Let vs Var vs Const](#2--let-vs-var-vs-const)
  - [3- Objects](#3--objects)
  - [4- The this Keyword](#4--the-this-keyword)
  - [5- Binding this](#5--binding-this)
  - [6- Arrow Functions](#6--arrow-functions)

# 1-Getting-Started
|    ||   |
|  ----  | ---- | ----  |
| import {} from…  || 跟export的名字必须一模一样 |
| import 自己命名 from… || import的是default export的内容 |
| () => { return <div>}  || div必须跟return在同一行，如果想分行写，需要写(); |
| () => ()  || 不必写return |

## 2
- Download node  
npm I -g create-react-app
- Vs code插件:  
Simple react snippets  
Prettier  

##  3- Your First React App
Create-react-app app-name  
Jsx: javascript xml  
Babeljs.io/repl：一个compiler可以翻译jsx  
registerServiceWorker：it serves assets from a local cache in a production environment 

Virtual DOM, a light weight in memory representation of the UI  

Whenever the state of the object(a part of the virtual DOM) changes, react will get a new react element. Then the react will compare this element with the previous element, it will figure out what is changed, and then it will reach out to the real DOM and update it accordingly.  

## 5- Custom Configs
Customize the default configuration that comes with the project  

For example: web pack configuration, that's when you use the eject喷射逐出 command  

Build: building this application for production  

Eject: you can run this command to eject from (create react app)(这是这种app的名字) and customize all the tools and configurations that come with this project。这个操作是单项的，一旦eject不可撤销，结果是所有config工作可以被释放，app开发者自己做。  

babel：js的编译器，将高版本的ES6转为低版本的ES5代码  

eslint：用于编码规范，Lint 是检验代码格式工具的一个统称

# 2-ES6-Refresher
## 2- Let vs Var vs Const
- var，应该尽量少的使用var
- let，定义一个变量，使这个变量只能在它被定义的block中被访问  
var -> function  
let -> block  
vonst -> block  

for 外面访问不到变量i
```javascript
function sayHello(){
    for (let i = 0, i < 5, i++){
        console.log(i)
    }
    console.log(i)
}
sayHello()
```

## 3- Objects
如果我们在一个object中有一个function，我们倾向于称这个function为method。We refer to that function as a method.  
下面第二个是object中method的简写方式
```javascript
const person = {
    name: 'Qing',
    walk: function() {},
    talk() {}
};
const person = {
    name: 'Qing',
    walk() {},
    talk() {}
};
```
访问object的属性property，有两种方式，点和[]。  
When we don't know ahead of time what property or method we're going to access, 使用\[\]。  

## 4- The this Keyword
This 总是返回reference to 当前object，但是js中this有点不同。If we call a function as a method in an object, this will always return a reference to that object,参考下图中person.walk()
```javascript
const person = {
    name: 'Qing',
    walk() {
        console.log(this);
    }
};
person.walk();
```
If we call a function as a stand-alone（不属于任何object） object or outside of an object（下图中const walk）, this will return the global object---window object, 但是利用strict mode就会返回undefined
```javascript
const person = {
    name: 'Qing',
    walk() {
        console.log(this);
    }
};
person.walk();
const walk = person.walk;
walk();
```
## 5- Binding this
在js中，functions是object，拥有members，其中就包括bind方法，to bind a function to an object  
.bind(person)将会返回这个walk function的一个新的实例，并且将console.log中的this指向这个person object
```javascript
const person = {
    name: 'Qing',
    walk() {
        console.log(this);
    }
};
person.walk();
const walk = person.walk.bind(person);
walk();
```
## 6- Arrow Functions
主意下面filter的用法，过滤保留符合条件的元素
```javascript
const person = {
    name: 'Qing',
    talk() {
        console.log(this);
    }
};
person.walk();
const walk = person.walk;
walk();
```