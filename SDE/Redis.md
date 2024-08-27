# Redis 连接

- Miebach-Capacity-Planner.redis.cache.windows.net:6380,password=cY9cbxFwFp1RP5Eb1NtpBqTzobaYHUUtJAzCaA5OAvg=,ssl=True,abortConnect=False
- rediss://:cY9cbxFwFp1RP5Eb1NtpBqTzobaYHUUtJAzCaA5OAvg=@Miebach-Capacity-Planner.redis.cache.windows.net:6380/0
- redis-cli -h myredis.redis.cache.windows.net -p 6380 -a your_primary_key --tls
- redis-cli -h Miebach-Capacity-Planner.redis.cache.windows.net -p 6380 -a cY9cbxFwFp1RP5Eb1NtpBqTzobaYHUUtJAzCaA5OAvg= --tls

# Redis 通信

`SCAN 0` 命令的结果表示你正在遍历 Redis 数据库中的键，命令返回了以下信息：

1. **"0"**: 这是游标（cursor），表示当前的扫描已经结束。如果返回的游标是非零的，比如 "1" 或其他数字，这意味着还有更多的键需要扫描。你需要使用这个游标作为下一个 `SCAN` 命令的输入，继续扫描剩余的键。

2. **键名列表**:

   - `_kombu.binding.celery.pidbox`
   - `_kombu.binding.celeryev`
   - `_kombu.binding.celery`

   这些是 Redis 中存在的键名，通常与 [Celery](https://docs.celeryproject.org/en/stable/index.html) 任务队列系统有关。Celery 使用 Redis 作为消息队列时，会创建这些键来管理消息和任务的分发。

### 这些键名的含义：

- **`_kombu.binding.celery`**: 这是 Celery 使用 Kombu（Celery 的消息传输库）创建的绑定键，用于管理 Celery 队列中的消息路由。
- **`_kombu.binding.celeryev`**: 类似地，这是 Celery 事件队列（`celeryev`）的绑定键，通常用于事件监控。
- **`_kombu.binding.celery.pidbox`**: 这个键与 Celery 的 `pidbox` 功能有关，`pidbox` 是 Celery 内部使用的一种通信机制。

### 下一步操作

如果你正在查找 Celery 任务队列（即任务列表），你可能会看到一个类似 `celery` 或 `celery.queue_name` 的键，它可能是实际存储任务的列表（queue）。

你可以继续使用 `SCAN` 命令来进一步查找其他键名，或者使用 `LLEN` 和 `LRANGE` 命令来查看这些键是否是你感兴趣的队列（即列表）。

例如：

```bash
LLEN celery
```

如果你猜测 `celery` 可能是一个队列的键名，可以用 `LLEN` 检查其长度。如果长度是大于零的数字，说明它是一个列表，你可以进一步用 `LRANGE` 来查看其内容。

# Redis 命令行

- reids 有多种数据类型
- 下面这个例子，使用了 LPUSH 将三个值插入了名为 runoobkey 的列表当中

```redis
redis 127.0.0.1:6379> LPUSH runoobkey redis
(integer) 1
redis 127.0.0.1:6379> LPUSH runoobkey mongodb
(integer) 2
redis 127.0.0.1:6379> LPUSH runoobkey mysql
(integer) 3
redis 127.0.0.1:6379> LRANGE runoobkey 0 10

1) "mysql"
2) "mongodb"
3) "redis"
```

# Redis one instance multiple database

- select 0-15
  - 选择任何一个数据库
  - 显示 OK
- scan 0
  - 扫描这个数据库
