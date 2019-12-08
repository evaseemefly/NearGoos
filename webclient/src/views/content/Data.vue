<template>
  <div class="center">
  <div class="center-welcome">
    <div class="title">
      <h1>WELCOME TO</h1><div class="important"><h1> RTDB</h1></div>
    </div>
    <div class="content">
      <h3>To dowonload data, please read data introduction before  </h3>
    </div>
  </div>
<div class="center-header ">

            <div class="card-form center-header-left">
                <div class="detail-card">
                    <div class="thumbnail">
                        <img src="/images/logo/BUOY_LOGO.png">
                        <div class="caption">
                            <h3>Buoy</h3>
                            <p>North Sea Buoy hourly data including elements: buoy id with longitude and latitude; year, month, date, hour (UTC); sea level air pressure, sea level air temperature; significant wave height, maximum wave height; sea surface temperature; data file format .csv.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card-form center-header-mid">
                <div class="detail-card">
                    <div class="thumbnail">
                        <img src="/images/logo/STATION_LOGO.png">
                        <div class="caption">
                            <h3>Station</h3>
                            <p>14 stations hourly data including elements: station name with longitude and latitude; year, month, date, hour (UTC); wind direction, wind speed; sea level air pressure, sea level air temperature; wave period, significant wave height, maximum wave height; swell direction, swell period, swell height; sea surface temperature; data file format .csv.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card-form center-header-right">
                <div class="detail-card">
                    <div class="thumbnail">
                        <img src="/images/logo/SHIP_LOGO.png">
                        <div class="caption">
                            <h3>Volunteer Ship</h3>
                            <p>Chinese volunteer ships hourly data including elements: ship name with longitude and latitude; year, month, date, hour (UTC); wind direction, wind speed; sea level air pressure, sea level air temperature; data file format .csv.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
  </div>
</template>
<script lang="ts">
import { Component, Prop, Vue, Watch } from "vue-property-decorator";
@Component({})
export default class DataView extends Vue {
  mydata: any = null;
  mounted() {}
  get computedTest() {
    return null;
  }
}
</script>
<style scoped lang="less">
@import "../styles/base.less";
//蓝色背景
@bluebackground: {
  
  background: rgba(51, 204, 204, 1);
};
// 统一白色form中的font样式
@whitefont: {
  font-family: Arial, Helvetica, sans-serif;
  text-shadow: 2px 2px 10px #000;
  color: white;
};
// 为二级标题加了一个左+上的间距
@minortitle: {
  // 统计title加一个左+上的间距
  margin-left: 1.5em;
  margin-top: 1em;
  font-size: 200%;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
  text-shadow: 2px 2px 10px #000;
};
// 中间的区域
.center {
  flex: 1;
  display: flex;
  flex-direction: column;
  // .center-header-welcome{
  //   display: flex;
  //   flex: 1;
  //   flex-direction: row;
  //   .title{
  //     display: flex;
  //     flex: 1;
  //   }
  //   .content{
  //     display: flex;
  //     flex: 1;
  //   }
  // }
  // 横向排列，显示三个说明
  .center-welcome{
    display: flex;
    flex-direction: column;
    align-items:center;
    justify-content:center;
    .title{
      display: flex;
    .important{
      display: flex;
      h1{
      color: #33CCCC;
      white-space: pre;
      }
    }
    }


  }
  .center-header {
    display: flex;
    flex: 1;
    // background: rgb(59, 126, 51);

    // 三种data的缩略图card样式父样式
    .card-form {
      display: flex;
      flex: 1;
      .detail-card {
        display: flex;
        justify-content: center;
        .thumbnail {
          img {
              width: 150px;
              height: 150px;
          }
          h3 {
            text-align: center;
            font-weight: bolder;
            color: #000000;
            // font-family: "Roboto",sans-serif;
          }
          p {
            font-size: 0.9rem;
            font-weight: 400;
            color: #000000;
          }
          width: 60%;
          @margindefault();
        }
      }
    }
  }

  // // 中间部分
  // // 横向排列
  // .center-center {
  //   display: flex;
  //   flex: 1;
  //   // background: rgb(145, 172, 73);

  //   // 中间部分的统计信息（station|fub|ship）的一些有序列表
  //   .center-center-left {
  //     display: flex;
  //     flex: 3;
  //     // background: rgba(39, 216, 216, 0.897);
  //     @bluebackground();
  //     flex-direction: column;
  //     @margindefault();
  //     @borderradius();
  //     .statistics-title {
  //       // color: yellow;
  //       // font-family: Arial, Helvetica, sans-serif;
  //       // text-shadow: 2px 2px 10px #000;
  //       @minortitle();
  //     }

  //     .statistics-form {
  //       display: flex;
  //       flex-direction: row;
  //       justify-content: center;

  //       .card-form {
  //         display: flex;
  //         flex: 1;
  //         flex-direction: column;
  //         // 注意此处为副轴方向
  //         align-items: center;
  //         font-family: Arial, Helvetica, sans-serif;
  //         text-shadow: 2px 2px 10px #000;
  //         .title {
  //           font-size: 2.5em;
  //           color: white;
  //         }

  //         .body {
  //           ul {
  //             li {
  //               line-height: 3em;
  //               color: white;
  //             }
  //           }
  //         }
  //       }

  //       // 非最后一个都加入右侧的边框（白色）
  //       .card-form:not(:last-of-type) {
  //         // 加入右侧的边框
  //         border-right: 1px solid white;
  //       }
  //     }
  //   }

  //   .center-center-right {
  //     display: flex;
  //     flex: 1;
  //     flex-direction: column;
  //     // background: rgb(15, 177, 163);
  //     @bluebackground();
  //     @margindefault();
  //     @borderradius();
  //     .statistics-title {
  //       @minortitle();
  //       // font-size: ;
  //     }
  //     form {
  //       display: flex;
  //       flex-direction: column;

  //       .form-group {
  //         display: flex;
  //         justify-content: space-around;
  //         label {
  //           @whitefont();
  //         }
  //       }
  //       .btn {
  //         display: flex;
  //         justify-content: center;
  //         button {
  //           color: #fff;
  //           // 暂时对提交按钮 先不上色了
  //           // background-color: #2bbbad !important;
  //         }
  //       }
  //     }
  //   }
  }

//   .center-footer {
//     display: flex;
//     flex: 2;
//     // background: rgb(42, 134, 146);
//     @bluebackground();
//     flex-direction: column;
//     @margindefault();
//     @borderradius();
//     .center-footer-card-header {
//       @minortitle();
//     }

//     .center-footer-card-body {
//       background: white;
//     }
//   }
// }
</style>
