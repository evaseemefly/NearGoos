- 本文档为进度计划

- 19-10-19~20

- [x] 1. 完成了`product`的`service`以及`entity`映射
- [x] 2. 完成了`document`的`service`以及`entity`的部分映射
- [x] 3. 完成了`document`的`tab`与`base`的业务逻辑

  - [x] 获取指定 level 的 tab
  - [x] 获取所有一级的 tab
  - [x] 获取指定 id 的 tab 以及 children
  - [x] 根据 tab id 获取对应的 base

  数据库设计修改如下:
  ![avatar](/document/img/readme/TIM截图20191020210124.png)
  ![avatar](/document/img/readme/TIM截图20191020210205.png)
  业务逻辑如下:
  ![avatar](/document/img/readme/TIM截图20191020210232.png)
  ![avatar](/document/img/readme/TIM截图20191020210246.png)
  ![avatar](/document/img/readme/TIM截图20191020210253.png)

---

- 19-10-21
- [x] 1. 完成了根据 base 获取对应的 image(`getImageByBase(Long id)`)
