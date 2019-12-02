<template>
  <div class="center">
    <!-- 主要内容 -->
    <div class="my-content">
      <!-- 中间上部区域 -->
      <div class="center-header">
        <!-- 产品内容 -->
        <div class="product-show">
          <!-- 中间上部左侧区域 -->
          <div class="center-header-left">
            <!-- 菜单栏 -->
            <div class="product-menu">
              <!-- 此处只为示意，之后使用elementui实现功能 -->
              <!-- <ul class="elements-ul">
                <li>Wave</li>
                <li>Sea Surface Temperature</li>
                <li>Current</li>
                <li>Sea Ice</li>
                <li>Far East</li>
              </ul>-->
              <!-- TODO:[*] 19-12-02 此处改为使用elementui -->
              <el-row class="tac">
                <el-col :span="24">
                  <!-- <h5>Type</h5> -->
                  <el-menu
                    default-active="2"
                    class="el-menu-vertical-demo"
                    @open="handleOpen"
                    @close="handleClose"
                    background-color="#33cccc"
                    text-color="#fff"
                    active-text-color="#ffd04b"
                    :default-openeds="openList"
                  >
                    <el-submenu index="father.key" v-for="(father, x) in menuList" :key="x">
                      <template slot="title">
                        <i class="el-icon-location"></i>
                        <span>{{father.val}}</span>
                      </template>
                      <el-menu-item
                        index="child.key"
                        v-for="(child, y) in father.children"
                        :key="y"
                        @open="selectMenu"
                        @click.native="selectMenu(father.key,child.key)"
                      >{{child.val}}</el-menu-item>
                    </el-submenu>
                  </el-menu>
                </el-col>
              </el-row>
            </div>
          </div>
          <!-- 中间上部右侧区域 -->
          <div class="center-header-right">
            <!-- 产品展示 -->
            <div class="product-exhibition">
              <!-- 标题 -->
              <div class="product-title">
                <div class="title">China Sea XXX Numeric Forecast</div>
                <!-- 预报时效选择框 -->
                <div class="interval-form">
                  <ul class="interval-ul">
                    <li v-for="(item, index) in getIntervalList" :key="index">{{item}}</li>
                  </ul>
                </div>
              </div>
              <!-- 产品图片 -->
              <div class="product-img">
                <img src="image/Product_img.jpg" width="70%" height="70%" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 中间区域-->
      <div class="product-data">
        <div class="product-search">
          <!-- 搜索部分 -->
          <div class="center-center">
            <div class="search-form">
              <div class="title">SEARCH</div>
              <!-- 搜索条件form -->
              <form>
                <div class="form-group">
                  <label for>Category</label>
                  <select>
                    <option value="volvo">All Area</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for>Area</label>
                  <select>
                    <option value="volvo">All Area</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for>Elements</label>
                  <select>
                    <option value="volvo">All Area</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for>Period</label>
                  <select>
                    <option value="volvo">All Area</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for>start date</label>
                  <select>
                    <option value="volvo">All Area</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for>end date</label>
                  <select>
                    <option value="volvo">All Area</option>
                  </select>
                </div>
                <div class="btn">
                  <button type="submit" class="btn btn-primary col-md-6">SEARCH</button>
                </div>
              </form>
            </div>
          </div>
        </div>
        <div class="product-result">
          <!-- 结果部分 -->
          <div class="center-footer">
            <div class="center-footer-card-header">Result</div>
            <div class="center-footer-card-body">
              <table class="table table-striped table-bordered">
                <thead>
                  <!-- <th>
                    <td>header1</td>
                    <td>header2</td>
                    <td>header3</td>
                    <td>header4</td>
                    <td>header5</td>
                    <td>header6</td>
                  </th>-->
                </thead>
                <tbody>
                  <tr>
                    <td>1</td>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                    <td>d</td>
                    <td>e</td>
                    <td>f</td>
                  </tr>
                  <tr>
                    <td>1</td>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                    <td>d</td>
                    <td>e</td>
                    <td>f</td>
                  </tr>
                  <tr>
                    <td>1</td>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                    <td>d</td>
                    <td>e</td>
                    <td>f</td>
                  </tr>
                  <tr>
                    <td>1</td>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                    <td>d</td>
                    <td>e</td>
                    <td>f</td>
                  </tr>
                  <tr>
                    <td>1</td>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                    <td>d</td>
                    <td>e</td>
                    <td>f</td>
                  </tr>
                  <tr>
                    <td>1</td>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                    <td>d</td>
                    <td>e</td>
                    <td>f</td>
                  </tr>
                  <tr>
                    <td>1</td>
                    <td>a</td>
                    <td>b</td>
                    <td>c</td>
                    <td>d</td>
                    <td>e</td>
                    <td>f</td>
                  </tr>
                </tbody>
              </table>
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
export default class ProductView extends Vue {
  mydata: any = null;
  openList: Array<string> = ["2", "3"];
  menuList: Array<{
    key: string;
    val: string;
    children: Array<{ key: string; val: string }>;
  }> = [
    {
      key: "1",
      val: "wave",
      children: [{ key: "2", val: "ChinaSea" }, { key: "3", val: "Northwest" }]
    },
    {
      key: "4",
      val: "Current",
      children: [
        { key: "5", val: "EastChinaSea" },
        { key: "6", val: "Northwest" },
        { key: "7", val: "FarEast" }
      ]
    },
    {
      key: "8",
      val: "Ice",
      children: [{ key: "9", val: "Bohai" }]
    },
    {
      key: "4",
      val: "Template",
      children: [
        { key: "5", val: "EastChinaSea" },
        { key: "6", val: "Northwest" }
      ]
    }
  ];

  intervalList: Array<{ key: string; val: Array<number> }> = [
    { key: "2", val: [24, 48, 72, 96] },
    { key: "3", val: [24, 48, 72, 96, 120] }
  ];
  menuIndex: string = "2";

  handleOpen() {
    console.log("展开");
  }
  selectMenu(father: string, child: string) {
    console.log(father + "|" + child);
    this.menuIndex = child;
  }
  handleClose() {}
  mounted() {}
  get computedTest() {
    return null;
  }

  get getIntervalList(): Array<number> {
    let myself = this;
    // TODO:[-] 19-12-02 此处bug已解决
    let res = myself.intervalList.find(temp => myself.menuIndex === temp.key);
    if (res != undefined) {
      return res.val;
    } else {
      return [];
    }
  }
}
</script>
<style scoped lang="less">
@import "../styles/base.less";
@bluebackground: {
  // background: rgba(39, 216, 216, 0.897);
  background: #33cccc;
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
// 统一白色form中的font样式
@whitefont: {
  font-family: Arial, Helvetica, sans-serif;
  text-shadow: 2px 2px 10px #000;
  color: white;
};
// 中间的区域
.center {
  flex: 1;
  display: flex;
  flex-direction: column;

  //产品展示区域,横向排列
  .center-header {
    display: flex;
    flex: 1;
    flex-direction: row;
    justify-content: space-around;

    .product-show {
      display: flex;
      .center-header-left {
        //菜单栏
        display: flex;
        flex: 1;
        flex-direction: row;
        justify-content: flex-start;

        .elements-ul {
          display: flex;
          flex: 1;
          flex-direction: column;
          // width: 700px;
          // height: 50px;
          list-style: none;
          margin: 0;
          padding: 0 20px;
          font-size: 30px;
          line-height: 50px;
          background: #33cccc;
          color: white;
        }
      }
      .center-header-right {
        //产品
        display: flex;
        flex: 3;
        flex-direction: row;
        justify-content: flex-end;

        .title {
          font-size: 36px;
          line-height: 50px;
          background: #33cccc;
          color: white;
        }

        .interval-ul {
          width: 700px;
          height: 50px;
          list-style: none;
          margin: 0;
          padding: 0 20px;
          font-size: 30px;
          line-height: 50px;
          background: #33cccc;
          color: white;
        }

        .interval-ul li {
          width: 70px;
          margin: 0 10px;
          float: left;
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
    @bluebackground();
    @margindefault();
    @borderradius();

    .title {
      @minortitle();
      // font-size: ;
    }

    form {
      display: flex;
      flex-direction: row;
      justify-content: space-around;

      .form-group {
        display: flex;
        justify-content: center;

        label {
          @whitefont();
        }
      }

      .btn {
        display: flex;
        justify-content: center;

        button {
          color: #fff;
          // 暂时对提交按钮 先不上色了
          // background-color: #2bbbad !important;
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
