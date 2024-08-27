# Hooks

React Hook 是 React 16.8 版本引入的一种特性，它允许函数式组件（Functional Components）在不引入类组件的情况下，拥有管理组件状态 State 和生命周期等功能。React Hook 的引入使得在函数式组件中更容易地操作状态、副作用和其他 React 特性。

# Custom Hooks

- React v16.8 hook permits you for reusing the stateful logic without any need for component hierarchy restructuring
- React v16.8 hook 允许您重用有状态逻辑，而无需重构组件层次结构
- 将跟 state 的有关的逻辑进行，打包，复用

## 例子一：

```JavaScript
import React, { useState } from 'react';

function SignUpForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // 执行用户名和密码验证逻辑
    if (/* 验证逻辑 */) {
      // 提交表单
    } else {
      // 显示错误消息
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={username} onChange={handleUsernameChange} />
      <input type="password" value={password} onChange={handlePasswordChange} />
      <button type="submit">Sign Up</button>
    </form>
  );
}

function ProfileForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // 执行用户名和密码验证逻辑
    if (/* 验证逻辑 */) {
      // 提交表单
    } else {
      // 显示错误消息
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" value={username} onChange={handleUsernameChange} />
      <input type="password" value={password} onChange={handlePasswordChange} />
      <button type="submit">Update Profile</button>
    </form>
  );
}
```

```JavaScript
import React, { useState } from 'react';

// 自定义 Hook 用于处理表单输入和验证逻辑
function useFormInput(initialValue) {
  const [value, setValue] = useState(initialValue);

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return {
    value,
    onChange: handleChange,
  };
}

function SignUpForm() {
  const usernameInput = useFormInput('');
  const passwordInput = useFormInput('');

  const handleSubmit = (event) => {
    event.preventDefault();

    // 执行用户名和密码验证逻辑
    if (/* 验证逻辑 */) {
      // 提交表单
    } else {
      // 显示错误消息
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" {...usernameInput} />
      <input type="password" {...passwordInput} />
      <button type="submit">Sign Up</button>
    </form>
  );
}

function ProfileForm() {
  const usernameInput = useFormInput('');
  const passwordInput = useFormInput('');

  const handleSubmit = (event) => {
    event.preventDefault();

    // 执行用户名和密码验证逻辑
    if (/* 验证逻辑 */) {
      // 提交表单
    } else {
      // 显示错误消息
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" {...usernameInput} />
      <input type="password" {...passwordInput} />
      <button type="submit">Update Profile</button>
    </form>
  );
}
```

## 例子二：

```JavaScript
import React, { useState, useEffect } from 'react';

function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // 发送请求获取用户数据
    fetchUsers()
      .then((data) => {
        setUsers(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}

function PostList() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // 发送请求获取文章数据
    fetchPosts()
      .then((data) => {
        setPosts(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```

```JavaScript
import React, { useState, useEffect } from 'react';

// 自定义 Hook 用于处理数据获取和状态管理
function useDataFetching(fetchFunction) {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // 发送请求获取数据
    fetchFunction()
      .then((data) => {
        setData(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err);
        setLoading(false);
      });
  }, [fetchFunction]);

  return { data, loading, error };
}

function UserList() {
  const { data: users, loading, error } = useDataFetching(fetchUsers);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
}

function PostList() {
  const { data: posts, loading, error } = useDataFetching(fetchPosts);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error.message}</p>;
  }

  return (
    <ul>
      {posts.map((post) => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
}
```
