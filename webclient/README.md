# neargoos 前端工程

## 安装

```
1.控制台安装node js，npm, cnpm, vue
```


```
npm install
```

### 启动

```
npm run serve
```

## 项目目录说明

<pre><code>
├──./                             <=vue前端项目工程
├──README.MD  
├── document                      <=一些遇见的问题的归档 
├── src                           <=项目源代码  
│ ├── views 
│ │  ├── content                  <= 内容页面 ，我习惯将所有的view跳转到的主要的view视图页面放置于此 
│ │  ├── footer                   <= footer 放置于此处
│ │  ├── header                   <= header 放置于此处
│ │  ├── x member x               <= 我之前是将全局的组件放置在members中，本项目不再使用此种方式  
├── components                     <= 将全局的组件放在此处
│ ├── xx_a                         <= xx_a 视图组件
│ │ ├── base                       <= xx_a 的基础组件
│ │ ├── bar                        <= xx_a 的bar组件
│ ├── common                       <= 一些公共的组件
├── router                         <= vue的router文件在此
├── store                          <= vuex 的所在路径
├── App.vue                        <= vue的起始视图页面，在 main.ts文件中引用 
├── main.ts                        <= vue的入口文件，我们使用了ts，所以为.ts 
</code></pre>

还有一些额外的说明

```
├── App.vue             <= 以前是将header与footer直接写在此处，由于此项目的实际home页面并没有header与footer，所以此处只有一个路由视图
│ ├── views
│ │  ├── Home.vue       <=  为不含header与footer的首页
│ │  ├── Content.vue    <=  保留header与footer组件的基础页面，其中会嵌套子路由
```

### 技术路线说明

vue + vuex + vue-router+webpack+es6+less

### 引用的一些组件

使用了`vue-property-decorator`
