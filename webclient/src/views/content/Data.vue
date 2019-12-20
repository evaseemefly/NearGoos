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
                <div class="center-center ">
                  <div class="center-center-left blue-green-bg">
                <!-- 统计的title -->
                <div class="statistics-title">STATISTICS</div><br>
                <!-- 下面的具体内容 -->
                <div class="statistics-form">
                    <!-- station -->
                    <div  class="card-form">
                        <div class="title">Buoy</div>
                        <div class="body">
                            <ul>
                              <!-- v-for循环没有成功,先遗留 -->
                                  <li>file numbers:<span>{{statistics_result[0].fileNumber}}</span></li>
                                <li>total size(Byte): <span>{{statistics_result[0].size}}</span></li>
                                <li>begin time: <span>{{statistics_result[0].beginTime}}</span></li>
                                <li>end time: <span>{{statistics_result[0].endTime}}</span></li>
                                <li>format: xml</li>
                            </ul>
                        </div>
                    </div>
                    <!-- fub -->
                    <div class="card-form">
                        <div class="title">Station</div>
                        <div class="body">
                            <ul>
<li>file numbers:<span>{{statistics_result[1].fileNumber}}</span></li>
                                <li>total size(Byte): <span>{{statistics_result[1].size}}</span></li>
                                <li>begin time: <span>{{statistics_result[1].beginTime}}</span></li>
                                <li>end time: <span>{{statistics_result[1].endTime}}</span></li>
                                <li>format: txt</li>
                            </ul>
                        </div>
                    </div> -->
                    <!-- ship -->
                    <div class="card-form">
                        <div class="title">Ship</div>
                        <div class="body">
                            <ul>
                              <li>file numbers:<span>{{statistics_result[2].fileNumber}}</span></li>
                                <li>total size(Byte): <span>{{statistics_result[2].size}}</span></li>
                                <li>begin time: <span>{{statistics_result[2].beginTime}}</span></li>
                                <li>end time: <span>{{statistics_result[2].endTime}}</span></li>
                                <li>format: -</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="center-center-right default-bg">
                <div class="statistics-title">
                    SEARCH
                </div><br>
                <!-- 搜索条件form -->
                <form>
                    <div class="form-group">
                        <label for="">Category</label>
                        <select>
                            <option value="volvo">All Area</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="">Area</label>
                        <select>
                            <option value="volvo">All Area</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="">Source</label>
                        <select>
                            <option value="volvo">All Area</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="">start date</label>
                        <select>
                            <option value="volvo">All Area</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="">end date</label>
                        <select>
                            <option value="volvo">All Area</option>
                        </select>
                    </div>
                    <div class="btn">
                        <button type="submit" class="btn btn-primary col-md-6">Search</button>
                    </div>
                </form>
            </div>
        </div>
  </div>
</template>
<script lang="ts">
import { Component, Prop, Vue, Watch } from "vue-property-decorator";
import axios from 'axios';
const host = 'http://localhost:8083'
@Component({})
export default class DataView extends Vue {
  mydata: any = null;
  statistics_result: any = [];
  
  // params = 'FUB';
  // statistics_fileNumber: any= '-';
  // statistics_size: any = '-';
  // statistics_beginTime:any = '-';
  // statistics_endTime: any='-';
  // statistics_name : string = '';
created() {
      getStatisticsByCategory().then((res:any)=>{
      if(res.status ===200){
        this.statistics_result = res.data;
        // alert(this.statistics_result[0].size);
      //   //时间转换为UTC时间
      //   //优化：长度缓存，避免重复获取，数组很大时优化效果明显
      // for(var j = 0, len = this.statistics_result.length; j< len; j++) {
      //   if(this.statistics_result[j].beginTime == null){

      //   }else{
      //     this.statistics_result[j].beginTime = this.statistics_result[j].beginTime.toUTCString();
      //     this.statistics_result[j].endTime = this.statistics_result[j].endTime.toUTCString();
      //   }
      // }
      }else{
        alert('请求失败');
      }
    })
  }
  get computedTest() {
    return null;
  }
}
//统计栏数据交互
// var statisticVM = new Vue({
//   el:'#statistics',
//   data:{
//     statistics_data:[]
//   },
//   created:function(){
//     var self = this;
//     getStatisticsByCategoryName().then((res:any)=>{
//       if(res.status ===200){
//         self.statistics_data = res.data
//         alert('成功');
//       }else{
//         alert('请求失败');
//       }
//     })
//   }
// })



//获取统计信息
const getStatisticsByCategory =  () => {
  let url = `${host}/data/statistics`
  return axios.get(
    url,
    {
      params: []
    }
  
  )
}

// var getStatictisByCategory = new Vue({
//   el:'#statistics',
//   data:{
//     answer:'222'
//     },
//   mounted:function(){

//   }
// })
</script>
<style scoped lang="less">
@import "../styles/base.less";
@margindefault: {
  margin: 1em;
};
@thumbnail: {
};
@borderradius: {
  border-radius: 1em;
};
//蓝色背景
@bluebackground: {
  
  background: rgba(51, 204, 204, 1);
};
//灰色背景
@graybackground: {
  
  background: rgba(215, 215, 215, 0.7);
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
            font-size: 1.2rem;
            font-weight: 400;
            color: #000000;
          }
          width: 60%;
          @margindefault();
        }
      }
    }
  }

  // 中间部分
  // 横向排列
  .center-center {
    display: flex;
    flex: 1;
    // background: rgb(145, 172, 73);

    // 中间部分的统计信息（station|fub|ship）的一些有序列表
    .center-center-left {
      display: flex;
      flex: 3;
      // background: rgba(39, 216, 216, 0.897);
      @bluebackground();
      flex-direction: column;
      @margindefault();
      @borderradius();
      .statistics-title {
        // color: yellow;
        // font-family: Arial, Helvetica, sans-serif;
        // text-shadow: 2px 2px 10px #000;
        font-size: 3em;
        @minortitle();
      }

      .statistics-form {
        display: flex;
        flex-direction: row;
        justify-content: center;

        .card-form {
          display: flex;
          flex: 1;
          flex-direction: column;
          // 注意此处为副轴方向
          align-items: center;
          font-family: Arial, Helvetica, sans-serif;
          text-shadow: 2px 2px 10px #000;
          .title {
            font-size: 2em;
            color: white;
          }

          .body {
            ul {
              li {
                line-height: 3em;
                color: white;
                font-size: 1em;
              }
            }
          }
        }

        // 非最后一个都加入右侧的边框（白色）
        .card-form:not(:last-of-type) {
          // 加入右侧的边框
          border-right: 1px solid white;
        }
      }
    }

    .center-center-right {
      display: flex;
      flex: 1;
      flex-direction: column;
      // background: rgb(15, 177, 163);
      @graybackground();
      @margindefault();
      @borderradius();
      .statistics-title {
        // @minortitle();
        font-size: 2em;
        color: black;
        // font-size: ;
      }
      form {
        display: flex;
        flex-direction: column;

        .form-group {
          display: flex;
          justify-content: space-around;
          
          font-size: 1.5em;
          
          label {
            // @whitefont();
            color: black;
          }
        }
        .btn {
          display: flex;
          justify-content: center;
          button {
            @bluebackground();
            border:none
            // background-color: #2bbbad !important;
          }
        }
      }
    }
  }

  .center-footer {
    display: flex;
    flex: 2;
    // background: rgb(42, 134, 146);
    @bluebackground();
    flex-direction: column;
    @margindefault();
    @borderradius();
    .center-footer-card-header {
      @minortitle();
    }

    .center-footer-card-body {
      background: white;
    }
  }
}
</style>
