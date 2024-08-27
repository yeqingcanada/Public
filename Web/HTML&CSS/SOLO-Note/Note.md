- 10 preloader 0.5
- 11 home 1.5
- 12 about 1
- 13 team 2
- 14 statement 0.5
- 15 services 1.5
- 16 work 2
- 17 testimonials 0.5
- 18 pricing 1
  19 stats 0.5  
  20 clients 0.5  
  21 blog 0.5  
  22 contact 0.5  
  23 map 0.5
- 24 footer
- 25 navigation 1.5
- 26 responsive 5
- 27 animation 1
- 彻底过一遍
  - index.html:
    - 每一个 类/id 从哪里来，如果是 boostrap 自带的类，它有什么效果
  - style.css:
    - 选择器怎么写
    - 每一个 property 有哪些 value，什么效果
  - script.js:
    - import 了哪些 libraries，什么作用
    - 每一个方法，哪些参数，什么作用
  - responsive.css

[好看的图片网站](https://unsplash.com/)
[另一个好看的图片网站](https://www.pexels.com/)
[第三个好看的图片网站](https://picjumbo.com/)
[第四个好看的图片网站](https://gratisography.com/)

## service

- response tab
  - css & js
  - 点击 <a href="#service-tab-1">，展示相应内容<div id="service-tab-1" class="service-tab">
  - 主要实现方法就是在 script.js 中添加以下代码
  - 添加前，div 是全部展开，一个接着一个被全部展示出来的
  - 添加后，只能看到其中一个 active 的 div，看不到其他三个 div
  - services-tabs 以及 service-tab 类，都是自定义类名，不是 response tab 中特别类名
  - response tab 需要一些前提条件：一个 <div id="services-tabs">，内部包含<ul><li><a href="#service-tab-1">Creativity</a></li></ul>,紧跟着，几个<div id="service-tab-1" class="service-tab">

```JavaScript
$(function () {
  $("#services-tabs").responsiveTabs({
    // 切换效果
    animation: "slide",
  });
});
```

## Work/Portfolio

- Isotope
  - ISOTOPE.METAFIZZY.CO
  - filter
  - script.js
- [magnific](https://dimsemenov.com/plugins/magnific-popup/)

## Testimonials

- Owl Carousel

  - 划动展示

## navigation

- Scrollspy
  - 划到某个 section，navbar 中对应的 link 会 highlighted
  - <body data-spy="scroll" data-target=".navbar" data-offset="65">
  - data-spy="scroll" 利用这部分实现
  - boostrap 滚动监听（Scrollspy）插件，即自动更新导航插件，会根据滚动条的位置自动更新对应的导航目标。其基本的实现是随着您的滚动，基于滚动条的位置向导航栏添加 .active class。我们需要写一些 css，给这种 active 类，以实现滚动高光
- 每一个 a/link 都有 smooth-scroll 类，用来自动滑向 a 中所指 section

## animation

- [Animate CSS](http://daneden.github.io/animate.css/)
  - 只有 css
- wow.js
  - 以 Animate CSS 为前提
  - 也需要 js
- 对于实现 animate，有两种方法
  - 一种是添加 animated fadeInDown 类（通过 script.js 添加），这种方法用于 home section 中的 title 部分，因为它是随着 page load 一起发生的
  - 第二种是直接给 div 添加 wow slideInLeft 类，这个类可以实现，伴随滑动到这个位置，再出现 animate 的效果
    - 如果去掉 wow，只保留 slideInLeft，在滑到这部分的时候，是看不到动画效果的，因为动画效果伴随着 page load 已经发生过了，滑到的时候，已经看不到了
    - wow class make the animation avaibable on scroll

## responsive

- Media Query
  - CSS techonique introduced in CSS3
  - @media rule to include a block of CSS properties only if a certain condition is true
- extra small devices phones <768px
- small devices tablets >=768px
- medium devies desktops >=992px
- large devies desktops >=1200px
- test tool
  - http://www.responsinator.com/
  - https://bluetree.ai/screenfly/

## mobile

- 正常 nav（大 show，小 hidden --- boostrap collapse 实现）
- 小 nav
  - open button（大 hidden，小 show --- response.css display: none/block）
  - close button & nav（大 hidden，小&关闭 hidden，小&开启 show --- script.js 根据 mobile-nav 类，conditional 开启/关闭， 初始设为 height: 0%）

### 选择器

1. 元素选择器
2. 类选择器、属性选择器和伪类
   - 属性选择器：
     input[type="text"] {
     border: 1px solid #ccc;
     }
   - 伪类选择器通常以冒号（:）开头，:hover
3. ID 选择器
4. 内联样式: 直接在元素上的 style 属性中定义的样式

### boostrap doc

[boostrap doc](https://getbootstrap.com/docs/3.3/components/#navbar)
