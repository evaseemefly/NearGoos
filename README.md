# near-goos 系统

## 项目主要参与人员

主要参与人员：  
[QuYuan891211](https://github.com/QuYuan891211)
├── 后端

[evaseemefly](https://github.com/evaseemefly)
├── 前端

## 后端项目目录

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
