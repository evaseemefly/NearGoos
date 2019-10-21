# near-goos 系统

## 项目主要参与人员

主要参与人员：  
[evaseemefly](https://github.com/evaseemefly) and [QuYuan891211](https://github.com/QuYuan891211)

进度参考:
[进度](/document/schedule/README.md)

## 后端项目目录

v1 版本：

> 此版本使用的是`my-batis`作为 orm

<pre><code>.
├──README.MD  
├── document                      <=一些遇见的问题的归档 
├── src/main/java/com/nmefc/neargoos  <=项目源代码  
│ ├── common                      <= 公共的一些组件
│ ├── controller                  <= 控制器均放置至此    
│ ├── dao                         <= 由mybatis根据entity进行映射 
│ ├── entity                      <= 由mybatis根据数据库进行映射 
│ │ ├── management                <= 由mybatis根据数据库进行映射 
│ ├── service 
│ │ ├── management                <= 由mybatis根据entity进行映射后生成的接口层
│ │ ├── impl                      <= 
│ │ │ ├──management               <= 具体的service/management 接口层对应的实现层
│ │ │ ├──BaseServiceImpl.java     <= 供 .management/ 中的实现类继承的抽象方法
│ │ ├── BaseService.java          <= 抽象接口（泛型） 
</code></pre>

v2 版本：

> 此版本使用`Hibernate`并通过`jpa`作为 ORM
> 后端结构如下：

<pre><code>
├──README.MD  
├── document                      <=一些遇见的问题的归档 
├── src/main/java/com/nmefc/neargoos  <=项目源代码  
│ ├── common                      <= 公共的一些组件
│ ├── controller                  <= 控制器均放置至此    
│ ├── entity                      <= 由JPA根据db映射的entity放置于此 
│ │ ├── management                <= management
│ │ ├── data                      <= data
│ │ ├── document                  <= document document
│ │ ├── product                   <= product 产品
│ ├── middleModel                 <= 中间model
│ ├── repository                  <= 所有的Repository放置于此
│ ├── service 
│ │ ├── impl                      <= 实现 
│ │ ├── inte                      <= 接口
</code></pre>

`repository`中的实现类均继承自`JpaSpecificationExecutor`与`JpaRepository`
`service/impl`中通过调用指定的`Repository`调用查询方法
