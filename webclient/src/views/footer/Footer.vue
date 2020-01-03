<template>
  <div id="footer">
    <!-- 选择成员国的友情链接 -->
    <div class="db-select">
      
        <!-- <button
          class="btn btn-default dropdown-toggle"
          type="button"
          id="db"
          data-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="true"
        > -->
        <div class="title">
         <h4> Database</h4>
        </div>
        
          <!-- <span class="caret"></span>
        </button> -->
        <!-- <div class="dropdown">
          <button class="dropbtn">Select Database</button>
          <div class="dropdown-content">
              <a href="#">china</a>
             <a href="#">菜鸟教程 2</a>
              <a href="#">菜鸟教程 3</a>
        </div>
        </div> -->


        <div class="btn-group dropup">
    <button class="btn btn-default dropdown-toggle" data-toggle="dropdown" type="button">Select Database<span class="caret"></span></button>
    <ul class="dropdown-menu">
         <li><a href="#">China National Delay-mode Database</a></li>
         <li><a href="#">Japan Regional Real Time Database</a></li>
         <li><a href="#">Korea National Real Time Database</a></li>
         <li><a href="http://rus.ferhri.ru/esimo/Projects/Neargoos/">Russia National Real Time Database</a></li>
         <li><a href="https://near-goos1.jodc.go.jp/index_j.html">Japan Regional Delay-mode Database</a></li>
         <li><a href="#">Korea National Delay-mode Database</a></li>
         <li><a href="#">Russia National Delay-mode Database</a></li>
    </ul>
</div>
      
    </div>
    <!-- 成员国 -->
    <div class="members">
      <h4>NEAR-GOOS Members Countries</h4>
      <div>
        <img src="/images/logo/chn.jpg" />
        <img src="/images/logo/jap.jpg" />
        <img src="/images/logo/korea.jpg" />
        <img src="/images/logo/rus.jpg" />
      </div>
    </div>
    <!-- 版权 -->
    <div class="copyright">
      <h4>LEGAL</h4>
      <h5>Copyright ©right;</h5>
      <h5>2019 National Marine Environment Forecasting Center(NMEFC)</h5>
      <h5>All Rights Reserved</h5>
    </div>
  </div>
</template>
<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
@Component({})
export default class Footer extends Vue {}
</script>
<style scoped lang="less">
#footer {
  background: url("/images/background/home_1_2.jpg");
  display: flex;
  justify-content: space-around;
  align-items: center;
  .db-select {
    display: flex;
    flex-direction: column;
            .btn {
        
        background-color: white;

        border: none;
        color: black;
        padding: 1px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }
      .btn {
          padding-left: 0;
          padding-right: 0;
          width: 200px;
      }
      // 按钮阴影
      .btn:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
}
      // 圆角按钮
      .btn {border-radius: 8px;}
      .dropdown-menu a{
        color: black;
        font-size: 16px;
        text-decoration: none;
        display: block;
      }
      // 鼠标悬停更改下拉框颜色
    .dropdown-menu a:hover {background-color: rgba(215,215,215,0.7)}

// /* 容器 <div> - 需要定位下拉内容 */
//     .dropdown {
//     // position: relative;
//     display: inline-block;
// }
/* 下拉内容 (默认隐藏) */
// .dropdown-content {
//     display: none;
//     position: absolute;
//     background-color: #f9f9f9;
//     min-width: 160px;
//     box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    
// }
// /* 下拉菜单的链接 */
// .dropdown-content a {
//     color: black;
//     padding: 12px 16px;
//     text-decoration: none;
//     display: block;
// }
// /* 鼠标移上去后修改下拉菜单链接颜色 */
// .dropdown-content a:hover {background-color: #f1f1f1}
/* 在鼠标移上去后显示下拉菜单 */
// .dropdown:hover .dropdown-content {
//     display: block;
// }
/* 当下拉内容显示后修改下拉按钮的背景颜色 */
// .dropdown:hover .dropbtn {
//     background-color: #3e8e41;
// }
    h4 {
      color: white;
    }
  }
  .members {
    display: flex;
    flex-direction: column;
    h4 {
      color: white;
    }
    img {
      margin-right: 0.25em;
    }
  }
  .copyright {
    display: flex;
    flex-direction: column;

    h4 {
      color: white;
    }
      h5 {
      color: white;
    }
  }
}
</style>
