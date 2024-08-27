#

tailwind 需要自己写很多
boostrap 更多 predefind 更改不容易

#

inderited from：当前 tag 的外层 tag 的内容
实心儿的 style：有被 apply 的
虚影儿的 style：table 中 width 是 100%，但是 th 中 width 没有被 apply
画横线的：被覆盖掉了

#

    4. 齿轮setting
    	a. StyledDropdownMenu ： 点击齿轮，出现的大框
    	b. CustomNavDropdownMenu ：点击第一个选项，弹出的左侧大框
    	c. menu 大框/大盒子，toggle 小盒子，item 小盒子里的内容
    		    display: flex;
    		    align-items: center;
    		    justify-content: flex-start;
    		6个row，而非6个column
    		  .dropdown-menu {
    		    position: absolute;
    		    top: -10px;
    		    left: auto;
    		    right: 100%;
    		    background: #e7e7e7 !important;
    		  }
    		出现在右边，背景是灰色
    		  .dropdown-toggle::before {
    		    content: "";
    		    display: inline-block;
    		    margin-right: -0.2rem;
    		  }

    		  .dropdown-toggle::after {
    		    content: none;
    		  }
    		单击，之前，之后，没有效果（2.0版本，是有效果的，有篮筐）

- 框套框的原因: 大框是一个部分,内部的内容是一个部分

# 下次改 setting icon

1. git checkout 1889780b28bc53f02c692eb4509055b53d905e65
2. 去 styled 文件夹里面找 App.js ---> NavBar
3. NavBar

```JavaScript
      <>
        {user.user_name && (
          <>
            <SettingIcon />
            <UserIcon />
          </>
        )}

        <SettingIcon />
        <UserIcon />
      </>
```

4. SettingIcon component 里变化
5. git checkout master

# css 被应用的顺序

1. 后面的会覆盖前面的, 下面的会覆盖上面的
