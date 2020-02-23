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
                        <ul class="num-box">
                            <li>
                              <p class="num">
                                <span id="num">{{statistics_result[0].fileNumber}}</span>
                              </p>
                             <p class="text">
                                <span id="fileNumber_text">file numbers</span>
                              </p>
                            </li>
                            <li>
                              <p class="num">
                                <span id="size_num">{{statistics_result[0].size}}</span>
                              </p>
                              <p class="text">
                                <span id="size_text">total size(Byte)</span>
                              </p>
                            </li>
                        </ul>
                        <div class="body">
                            <ul>
                              <!-- v-for循环没有成功,先遗留 -->
                                <!-- <li>file numbers:<span>{{statistics_result[0].fileNumber}}</span></li>
                                <li>total size(Byte): <span>{{statistics_result[0].size}}</span></li> -->
                                <li>begin time: <span>{{statistics_result[0].endTime}}</span></li>
                                <li>end time: <span>{{statistics_result[0].beginTime}}</span></li>
                                <li>format: xml</li>
                            </ul>
                        </div>
                    </div>
                    <!-- fub -->
                    <div class="card-form">
                        <div class="title">Station</div>
                            <ul class="num-box">
                            <li>
                              <p class="num">
                                <span id="num">{{statistics_result[1].fileNumber}}</span>
                              </p>
                             <p class="text">
                                <span id="fileNumber_text">file numbers</span>
                              </p>
                            </li>
                            <li>
                              <p class="num">
                                <span id="size_num">{{statistics_result[1].size}}</span>
                              </p>
                              <p class="text">
                                <span id="size_text">total size(Byte)</span>
                              </p>
                            </li>
                        </ul>
                        <div class="body">
                            <ul>
                                <!-- <li>file numbers:<span>{{statistics_result[1].fileNumber}}</span></li>
                                <li>total size(Byte): <span>{{statistics_result[1].size}}</span></li> -->
                                <li>begin time: <span>{{statistics_result[1].endTime}}</span></li>
                                <li>end time: <span>{{statistics_result[1].beginTime}}</span></li>
                                <li>format: txt</li>
                            </ul>
                        </div>
                    </div> 
                    <!-- ship -->
                    <div class="card-form">
                        <div class="title">Ship</div>
                                           <ul class="num-box">
                            <li>
                              <p class="num">
                                <span id="num">{{statistics_result[2].fileNumber}}</span>
                              </p>
                             <p class="text">
                                <span id="fileNumber_text">file numbers</span>
                              </p>
                            </li>
                            <li>
                              <p class="num">
                                <span id="size_num">{{statistics_result[2].size}}</span>
                              </p>
                              <p class="text">
                                <span id="size_text">total size(Byte)</span>
                              </p>
                            </li>
                        </ul>
                        <div class="body">
                            <ul>
                              <!-- <li>file numbers:<span>{{statistics_result[2].fileNumber}}</span></li>
                                <li>total size(Byte): <span>{{statistics_result[2].size}}</span></li> -->
                                <li>begin time: <span>{{statistics_result[2].endTime}}</span></li>
                                <li>end time: <span>{{statistics_result[2].beginTime}}</span></li>
                                <li>format: -</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <div class="center-center-right default-bg">
                <div class="search-title">
                    Search XXX XXXXXXXXXXXXXXXXXXXXXXXXX...... 
                    <div class="search-subtitle">
                    From XXXXXXXXXXXXXXXXXXXXX...... 
                </div>
                </div><br>
                
                <!-- 搜索条件form -->
                <el-form :model="search_form">
                    
                        <el-form-item >
                            <el-select  v-model="category_selected" value-key="id" placeholder="select category">
                              <el-option v-for="item in category_list" :key="item.id" :label="item.name" :value="item.id"></el-option>
                            </el-select>
                        </el-form-item>
                    
                   
                        <el-form-item >
                            <el-select v-model="area_selected" value-key="id"  placeholder="select area">
                              <el-option v-for="item in area_list" :key="item.id" :label="item.name" :value="item.id"></el-option>
                            </el-select>
                        </el-form-item>
                    
                    
                        <el-form-item >
                            <el-select v-model="source_selected" value-key="id" placeholder="select source">
                              <el-option v-for="item in source_list" :key="item.id" :label="item.name" :value="item.id"></el-option>
                            </el-select>
                        </el-form-item>
                    
                    
                        <el-form-item>
                            <el-date-picker class="time_select" v-model="startTime_selected" type="datetime" placeholder="select start time(UTC)" @change="dataSearch" value-format="yyyy-MM-dd HH" format="yyyy-MM-dd HH"></el-date-picker>
                        </el-form-item>
                    
                    
                        <el-form-item>
                         <el-date-picker class="time_select" v-model="endTime_selected" type="datetime" placeholder="select end time(UTC)" @change="dataSearch" value-format="yyyy-MM-dd HH" format="yyyy-MM-dd HH"></el-date-picker>
                        </el-form-item>
                    <el-form-item>
                    <!-- <div class="btn"> -->
                        <el-button type="success" class="btn btn-primary col-md-6" @click="submitForm">Search Data</el-button>
                    <!-- </div> -->
                    </el-form-item>
                </el-form>
            </div>
          </div>
            <!-- 查询结果 -->
            <div class="center-footer">
                <div class="center-footer-card-header">
                RESULTS
            </div>
                 <div class="center-footer-card-body">
                   <!-- 表头内容 -->
                   <!-- <div class="table table-striped table-bordered"> -->
                  <el-table class="result_table" :data="results_data" ref="multipleTable"> 
                    <el-table-column type="selection"></el-table-column>
                    <el-table-column type="index" label="Index" width="80px"></el-table-column>
                    <el-table-column prop="id" label="Id" ></el-table-column>
                    <el-table-column prop="name" label="Filename" ></el-table-column>
                    <el-table-column prop="date" label="Date" ></el-table-column>
                    <el-table-column prop="category" label="Category" ></el-table-column>
                    <el-table-column prop="area" label="Area" ></el-table-column>
                    <el-table-column prop="source" label="Source" ></el-table-column>
                    <el-table-column prop="size" label="Size(Byte)" ></el-table-column>
                    <el-table-column label="action">
　　　　<template slot-scope="scope">
　　　　　　<el-button type="info" class="btn_show" @click="showData('/'+ scope.row.url)">show data</el-button>
　　　　</template>
　　</el-table-column>
                  </el-table>
                  <el-button type="success" class="btn_download" @click="download">Download Data</el-button>

                 <div>
                 </div>
            <!-- </div> -->
        </div>
  </div>
</div>
</template>
<script lang="ts">
import { Component, Prop, Vue, Watch } from "vue-property-decorator";
import axios from 'axios';
import JSZip from 'jszip';
import FileSaver from 'file-saver'
const host = 'http://localhost:8083'
@Component({})
export default class DataView extends Vue {
  mydata: any = null;
  statistics_result: any = [];
  area_list : any = [];
  source_list: any =[];
  category_list:any=[];
  category_selected : any = null;
  area_selected : any = null;
  source_selected :any = null;
  startTime_selected :any = null; 
  endTime_selected :any = null;
  results_data: any =[];
  url:any = null;
  
// lifecycle hook
mounted() {
      getStatisticsByCategory().then((res:any)=>{
      if(res.status ===200){
        this.statistics_result = res.data;

      }else{
        alert('数据统计请求失败');
      }
    })
    //获取全部区域
    getAllArea().then((res:any)=>{
      if(res.status ===200){
          this.area_list = res.data;
      }else{
        alert('区域获取请求失败');
      }
    })
       //获取全部数据类型
    getAllCategory().then((res:any)=>{
      if(res.status ===200){
          this.category_list = res.data;
      }else{
        alert('区域获取请求失败');
      }
    })
    //获取全部数据源
    getAllSource().then((res:any)=>{
      if(res.status ===200){
          this.source_list = res.data;
      }else{
        alert('数据源获取请求失败')
      }
    })


  }

  //computed
  get computedTest() {
    return null;
  }

  //methods
  showData(showData_url:string){
    showData_url = showData_url.replace(/\\/g,'/');
    window.open(showData_url)
  }



  submitForm(){
    // let formData = new FormData();
//     let config = {
//    headers: {
//     'Content-Type': 'multipart/form-data;boundary = ' + new Date().getTime()
//     } 
// }
  let url = `${host}/data/getDataInfoResultsByQuery`
  //绑定数据

  let data = {
    'categoryId': this.category_selected ,
    'areaId': this.area_selected,
    'sourceId': this.source_selected,
    'beginTime': this.startTime_selected,
    'endTime': this.endTime_selected
  }
  // formData.append('categoryId', this.category_selected);
  // formData.append('areaId', this.area_selected);
  // formData.append('sourceId', this.source_selected);
  // formData.append('beginTime', this.startTime_selected);
  // formData.append('endTime', this.endTime_selected);
  
  axios.post(url,data).then(res=>{
    alert(res.data);
        if(res.data[0].state){
          this.results_data = res.data;
          // alert(this.results_data[0].url)
        }else{
          alert(res.data[0].msg)
        }
        
  }).catch(err=>{
    alert('err');
  });


  }
}

//获取全部海区
const getAllArea = () =>{
  let url = `${host}/data/getAllArea`
  return axios.get(
    url,
    {
      params: []
    }
  )
}

//获取全部数据源
const getAllSource = () => {
  let url = `${host}/data/getAllSource`
  return axios.get(
    url,
    {
      params: []
    }
  )
}


//获取全部数据类型
const getAllCategory = () => {
  let url = `${host}/data/getAllCategory`
  return axios.get(
    url,
    {
      params: []
    }
  )
}

//根据类别获取统计信息
const getStatisticsByCategory =  () => {
  let url = `${host}/data/statistics`
  return axios.get(
    url,
    {
      params: []
    }
  
  )
}

//初始化时间
const initData = () =>{
      var now   = new Date();
      var monthn = now.getUTCMonth()+1;
      var yearn  = now.getUTCFullYear();
      var dayn = now.getUTCDate();
      var h = now.getUTCHours();
      var m = now.getUTCMinutes();
      var s = now.getUTCSeconds
      return yearn+"-"+monthn+"-"+dayn+" "+h+" "+m+" "+s;
}


//查询
const searchData = () =>{


}


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
    flex-direction: column;
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
        font-size: 3rem;
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
            font-size: 2rem;
            color: white;
          }
          .num-box{
            column-count:2;
            color: white;
            list-style: none;
            .num{
              font-size: 3rem
            }
            .text{
              font-size: 1.5rem
            }

          }
          .body {
            ul {
              li {
                line-height: 3em;
                color: white;
                font-size: 1rem;
                list-style: none
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
      .search-title {
        // @minortitle();
        text-align:left;
        font-size: 2rem;
        color: black;
        padding-left:40px;
        // font-size: ;
      
      .search-subtitle {
        // @minortitle();
        font-size: 1.5rem;


      }
      }
      .el-form {
        display: flex;
        flex: 1;
        flex-direction: row;
        flex-wrap:wrap;
        align-items: center;
        justify-content: center;
        .el-select {
          display: flex;
          flex: 1;
          justify-content: center;
          font-size: 1.5rem;
          width:300px;
          // border:40px #33CCCC;
          //已取消label
          label {
            // @whitefont();
            color: black;
            font-size: 2rem;
          }
        }
        .time_select{
          width:320px;
          // border: 10px #33CCCC;
        }
        // .btn {
          
          button {
            display: flex;
          justify-content: center;
            @bluebackground();
            border:none;
            // background-color: #2bbbad !important;
            width:250px
          }
        // }
      }
    }
  }

  .center-footer {
    display: flex;
    flex: 2;
    // background: rgb(42, 134, 146);
    @graybackground();
    flex-direction: column;
    @margindefault();
    @borderradius();
    .center-footer-card-header {
      font-size: 2rem;
      color: black;
      //  @minortitle();
    }

    .center-footer-card-body {
      background: white;
      font-size: 1rem;
        color: black; 
        align-self: auto;
        .result_table{
          height: 500px;
          overflow: scroll;
        }
// 修改滚动条样式
    // .table table-striped table-bordered::-webkit-scrollbar-thumb{
    //     border-radius: 2px;
    //     height: 50px;
    //     background: #eee;
    // }
    // .table table-striped table-bordered::-webkit-scrollbar-track{
    //     box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
    //     border-radius: 2px;
    //     background: rgba(0,0,0,0.4);
    // }
          .btn_show {
          display: flex;
          margin:0 auto;
            @bluebackground();
            border:none
            // background-color: #2bbbad !important;
          
        }
        .btn_download {
          display: flex;
          justify-content: center;
          margin:0 auto;
          width: 200px;
            @bluebackground();
            border:none
            // background-color: #2bbbad !important;
          
        }
    }
  }
}
</style>
