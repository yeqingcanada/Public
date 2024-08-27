# 学习顺序

- v1 + v2 + v3 关键字
  - 阿里巴巴 2022 年 Java 架构师岗面试题.pdf
  - How2J
- 补充材料
  - [web 1](https://javabetter.cn/sidebar/sanfene/nixi.html#pdf版阅读)
  - [web 2](https://javabetter.cn/sidebar/sanfene/mysql.html#_1-%E4%BB%80%E4%B9%88%E6%98%AF%E5%86%85%E8%BF%9E%E6%8E%A5%E3%80%81%E5%A4%96%E8%BF%9E%E6%8E%A5%E3%80%81%E4%BA%A4%E5%8F%89%E8%BF%9E%E6%8E%A5%E3%80%81%E7%AC%9B%E5%8D%A1%E5%B0%94%E7%A7%AF%E5%91%A2)
  - 50w 字程序员面试宝典.pdf

# V1.0

- Intro
- OOP
- Design Pattern
  - DesignPattern 可以改变 Runtimebehavior
  - Factory
  - abstractFactory
- Thread
  - 刷一下多线程的八股文比如死锁什么
- Web
  - servlet 建议写
  - JSP 理解一下就行不用写
- JDBC
  - 比较重要的基础, 需要理解好, 可以不用写, 面试会问为什么不用 JDBC 而用 hibernate
- Maven
  - 实用工具, 知道干啥就行, 知道常见指令, mvn clean install, mvn test
- Hibernate
  - 很重要（北美）
  - 知道 Hibernate 解决了什么问题
- Spring
  - 非常重要
  - 面试 99%会问
- Spring MVC
  - 会问 MVC 是
  - 什么 DispatcherServlet 流程
  - 还有各种 annotation
- ​Spring Security
  - 比较重要
  - 常见的登陆忘记密码
  - 注册
- Spring Boot
  - 非常重要
  - 面试会问 Springboot 和 spring 区别
- Spring Data Repository
- Spring Cache
- Spring Cloud
  - 进阶必备
  - 非常重要
  - 微服务组件
- MySQL
  - 非常重
  - 要面试常考
  - 理解 SQL 和 NoSQL
  - 还有 MySQL 常见八股要背
  - clustered index
  - index 啥作用
- Redis
  - 比较重要
  - Redis 为啥快
  - redis 应用场景
  - 什么样的数据都放 cache 里
  - 进阶了可以看分布式锁
- Docker
  - 比较重要
  - 和 Redis 同理
  - 可以下载一个 Docker 操作一下
  - 工作中这个部分是在 DevOps 上
  - 和 Backend 开发关系不大
- Github
- Swagger
- Postman 同 Swagger
- Kafka/RabbitMq
  - 比较重要
  - 需要知道干什么
  - 解决了什么特性
  - 和其他 MQ 区别
- Junit
  - 单元测试
  - integration test

# V2.0

https://www.1point3acres.com/bbs/thread-742438-1-1.html

一、CS 基础知识
操作系统
计算机网络
计算机组成原理

二、Java 语言基础和提高
Java 并发
JVM 原理

三、Java 集合 ArrayList
LinkedList
HashMap
TreeMap

四、Java 开发基础
JavaWeb 基础
主要内容包括 MySQL 数据库基础
前端 HTML/CSS/JS 基础、jQuery/AJAX
Tomcat 入门、Servlet、JSP、Cookie/Session
Filter/Listener
Maven 入门
Redis 入门
所以主要就是讲 J2EE 基础的 Servlet 和 JSP 现在不会直接拿来用了但不管是 SpringMVC 还是 SpringBoot 本质上都是对其的封装而这个视频对这些 J2EE 的基础讲得很清楚以后再学其他的内容时就肯定会更清晰了并且这个视频后会带你做一个纯 J2EE 的项目

五、Spring 框架
MyBatis 框架
Spring 基础
Spring 源码
SpringMVC
SpringData
SpringBoot
MyBatis 感觉美国这边也不太常用

六、数据库、缓存、消息队列
MySQL 优化
Redis 基础和提高
ActiveMQ
RabbitMQ
这些内容当时在秋招的时候简直是每次面试都会出现
所以到了现在, 就算其他的八股文都忘了, MySQL 和 Redis 还是记得很清晰
MySQL 优化主要讲了索引、SQL 优化、锁、主从复制读写分离等
如果对这些内容一无所知的话建议了解
不过这个视频没怎么讲 MVCC 和事务原理
MySQL 索引刷盘也没有特别深入
导致当时我准备不足挂了两三个面试
建议看完这个视频以后再找找别的资料
不过 SQL 优化他讲得确实还算不错
Redis 的视频挺好的
几乎涵盖了我所有面试的时候被问到的
Redis 全部内容包括持久化、事务、分布式锁、高级数据结构
还有 Redis 的哨兵和集群以及缓存雪崩,击穿穿透等解决方案
因此强烈推荐后面的 MQ 相关的视频
ActiveMQ 还不错
如果对消息队列一无所知的话, 可以看看
但是 RabbitM 就讲得有点糟糕
Kafka 和 RocketMQ 没看

七、微服务与分布式相关组件
SpringCloud
分布式事务
SpringCloudAlibaba
Zookeeper 和 Dubbo
其实还有很多所谓的“分布式组件”就不一一列出来了
我觉得这些东西没太多学的必要
国内的这些资源也大多说的是那些开源的工具
如果在美国求职的话很多组件估计各大公司都有自己的
就算是在国内求职每个公司用的东西也都不一样
以上这些内容也绝不等于美国这边求职面试时候说的 SystemDesign
我看了 SpringCloud 和分布式事务
讲得就那样但是足够入门
知道微服务到底都在干什么
也知道了一些解决方案
后面的什么 springcloudalibaba 真没学的必要
zookeeper 这些还不如直接看美国这边的相关资料或论文

八、其他
这里就不分享视频了
这么一回顾发现自己确实看了很多也学了很多
当时开始学这些东西的根本原因,也是觉得自己作为转码选手真的什么都不知道
所以要补基础、学更多的技术
但是学来学去才发现真正重要的还是自己的 coding 能力, 以及遇到问题后提出解决方案的能力, 也就是“刷题”和“系统设计”
以上这些内容尤其是到后面的各个分布式组件、框架、中间件等只不过一个又一个的技术罢了
如果仅仅知道怎么操作和使用它们或者背它们的源码背八股文那真是一点用都没有
这些绝不是系统设计真正要学的是他们为什么要这么使用
为什么要这么搭建
比如 Redis 的集群哨兵模式是怎么保证整体可用的
比如 RabbitMQ 的可靠性消息投递的方案是怎么设计的, 类似的设计思路又可以被用在哪些其他场景下
遇到类似的问题自己应该怎么解决
学习 SpringCloud 没啥问题, 但要学的绝不仅仅是怎么使用 Eureka、怎么使用 Gateway
更关键的是了解微服务架构中可能存在的问题面对这么多的问题、各自的解决方案是什么
所以我们才有了注册中心、网关、服务熔断等等措施
分布式事务也是要学的不仅是 RocketMQ 的几个 API 美国这边又不用这个
重要的还是解决方案的思想
总之以上就是我作为一个转码选手学习 Java 语言、深入、开发、框架、各个组件的时候所用到的资料
确实也算是从 B 站毕业了 Java 相关的内容
在学生阶段要学的差不多也就这些了以上这些内容
学完了以后再去作为一个应届生面试国内的大中小公司应该是不成问题了
我也是靠着这些去年秋招拿到了几个 offer 想学的话就好好学多学习
知识肯定没有坏处
但是一定不能仅仅局限于背八股文的程度
包括自己在做项目的时候也是
就算是跟着网课视频“做项目”也不能仅仅局限于 spring 是怎么操作的啊、怎么连接数据库的啊、Controller 要标注哪几个 Annotation 啊如果只会这个面试的时候你跟面试官讲什么呢？

# V3.0

- **Web 服务器**
  - 提供静态文件服务并将请求路由到适当的应用程序组件。
  - 示例包括 Nginx、Apache、Express (Node.js)
- **应用服务器**
  - 执行服务器端逻辑并与数据库通信。
  - 示例包括 Tomcat、Gunicorn、uWSGI、Express (Node.js)
- **APIs**
  - 定义应用程序各个组件之间的通信协议。
  - 示例包括 RESTful、GraphQL
- **框架**
  - 为网站应用开发提供预建功能和结构的工具。
  - 示例包括 Spring Boot、Django、Ruby on Rails、Express
- **负载均衡器**
  - 将传入流量分布到多个服务器上，以确保负载均匀分配。
  - 示例包括 HAProxy、Nginx、AWS Elastic Load Balancer
- **安全层**
  - 实施如身份验证、授权和加密等安全措施。
  - 示例包括 SSL/TLS、OAuth、JWT
- **DevOps 工具**
  - 自动化网站应用的部署、监控和扩展。
  - 示例包括 Docker、Kubernetes、Jenkins、Terraform

MySQL：索引与事务的实现原理、SQL 优化、分库分表；  
Redis: 数据结构、缓存、分布式锁、持久化机制、复制机制；  
RabbitMQ: 消息中间件
分布式：分布式事务、一致性问题；  
并发基础：ConcurrentHashMap, AQS, CAS，线程池等；  
高并发：IO 多路复用；缓存问题及方案；

Developed the back-end distributed system for an online platform using the Spring Cloud framework  
Designed and implemented the media service, using MinIO as a distributed file storage system and implemented features for regular file uploads, big file chunked uploads, resumable uploads and rapid file transmission  
Used XXL-Job for distributed task scheduling, combined with multi-threading to implement efficient execution of video transcoding tasks, employed distributed locks to ensure
