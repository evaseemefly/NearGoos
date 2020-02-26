<template>
  <div class="my-content">
    <div class="content-1">
      <div class="content-1-title">
        <h1>NEAR-GOOS China</h1>
        <h4>
          NEAR (North-East Asian Regional)-GOOS is a regional pilot project of
          GOOS in the North-East Asian Region, implemented by China, Japan, the
          Republic of Korea and the Russian Federation as one activity of IOC
          Sub-Commission for the Western Pacific (WESTPAC). NEAR-GOOS was
          conceived and initiated upon the formal adoption of the NEAR-GOOS
          Implementation Plan and Operational Manual the Intergovernmental
          Oceanographic Commission following a recommendation from the WESTPAC
          Regional Sub commission of IOC earlier in the year. It became one of
          the first regional pilot projects of GOOS. The primary aim of
          NEAR-GOOS in its first phase was to facilitate the sharing of
          oceanographic data gathered by agencies of the partner countries using
          the internet, to support the daily mapping of conditions in the
          marginal seas bordered by the partner countries. Although it was
          anticipated that this should eventually lead to improvement in the
          availability of information and ocean services for all kinds of
          beneficial purposes, it is important to note that these flow-on
          outcomes were not specific goals for the first phase.
        </h4>
      </div>
    </div>
    <div class="content-introduce">
      <!-- 左侧导航栏 -->
      <ul>
        <li
          :key="item.key"
          v-for="item in tabContent"
          @click="setTabIndex(item.key)"
        >
          {{ item.title }}
        </li>
        <!-- <li>About NEAR-GOOS</li>
        <li>First Phase Success</li>
        <li>Objectives Basis</li>
        <li>Activities</li>
        <li>Scientific Basis</li>
        <li>Principles</li>
        <li>Data</li> -->
      </ul>
      <!-- <div class='left-bar'>
        </div> -->
      <!-- 右侧具体内容 -->

      <div class="right-content">
        <transition name="tabcontent" mode="out-in">
          <h4 class="item" :key="TabContent.key">
            {{ TabContent.val }}
          </h4>
        </transition>
      </div>
    </div>
    <div class="content-2">
      <div class="content-1-title">
        <h1>Goals</h1>
        <h4>
          The goals of NEAR-GOOS in its second phase is to development of a
          basic integrated ocean observing and operational forecasting system in
          the NEAR-GOOS area adhering to the GOOS Principles and building on the
          data management and exchange mechanisms developed in the first phase
          through the inclusion of additional parameters, increased coverage in
          space and time, the generation of a generic suite of data products and
          adequate quality control and quality assurance procedures.
        </h4>
      </div>
    </div>
    <div class="content-3">
      <div class="content-1-title">
        <h1>Missions</h1>
        <div class="minor_title">
          <h4>
            The mission of NEAR-GOOS in its second phase is to develop a
            comprehensive and sustained ocean observing network in the
            North-East regional seas and coastal regions, especially focused on
            observations, monitoring and other activities that cannot be easily
            implemented by countries acting independently. This network will
            embrace a wide range of data types and will be accompanied by the
            participating members and as a contribution to the GOOS and other
            global observing initiatives.
          </h4>
        </div>
      </div>
    </div>
    <div class="content-4">
      <div class="content-1-title">
        <h1>Area of NEAR-GOOS</h1>
        <div class="minor_title">
          <h4>
            The area of NEAR-GOOS is the North-East Asian Region, which is a
            part of the WESTPAC region, bounded by China, Republic of Korea,
            Democratic People's Republic of Korea and the Russian Federation
            along its western boundary, and by the Russian Federation and Japan
            along the eastern boundary.
          </h4>
        </div>
      </div>
    </div>
  </div>
</template>
<script scoped lang="ts">
import { Component, Prop, Vue, Watch } from 'vue-property-decorator';
@Component({})
export default class OverView extends Vue {
  mydata: any = null;
  tabIndex: number = 0;
  tabContent: { key: number; title: string; val: string }[] = [
    {
      key: 0,
      title: 'About NEAR-GOOS',
      val:
        'NEAR (North-East Asian Regional)-GOOS is a regional pilot project of GOOS in the North-East Asian Region, implemented by China, Japan, the Republic of Korea and the Russian Federation as one activity of IOC Sub-Commission for the Western Pacific (WESTPAC). NEAR-GOOS was conceived and initiated upon the formal adoption of the NEAR-GOOS Implementation Plan and Operational Manual the Intergovernmental Oceanographic Commission following a recommendation from the WESTPAC Regional Sub commission of IOC earlier in the year. It became one of the first regional pilot projects of GOOS. The primary aim of NEAR-GOOS in its first phase was to facilitate the sharing of oceanographic data gathered by agencies of the partner countries using the internet, to support the daily mapping of conditions in the marginal seas bordered by the partner countries. Although it was anticipated that this should eventually lead to improvement in the availability of information and ocean services for all kinds of beneficial purposes, it is important to note that these flow-on outcomes were not specific goals for the first phase.',
    },
    {
      key: 1,
      title: 'First Phase Success',
      val: 'First Phase Success 内容',
    },
    {
      key: 2,
      title: 'Objectives Basis',
      val: 'Objectives Basis 内容',
    },
    {
      key: 3,
      title: 'Activities',
      val: 'Activities 内容',
    },
    {
      key: 4,
      title: 'Scientific Basis',
      val: 'Scientific Basis 内容',
    },
    {
      key: 5,
      title: 'Principles',
      val: 'Principles 内容',
    },
    {
      key: 6,
      title: 'Data',
      val: 'Data 内容',
    },
  ];
  mounted() {}
  setTabIndex(val: number) {
    this.tabIndex = val;
  }
  get computedTest() {
    return null;
  }
  @Watch('tabIndex')
  onTabIndex(val: number) {}

  get TabContent() {
    const tempContent = this.tabContent.find(temp => {
      if (temp.key === this.tabIndex) {
        return temp;
      }
    });
    if (tempContent != undefined) {
      return tempContent;
    }
  }
}
</script>
<style scoped lang="less">
// 含图片的背景
.basecontent() {
  height: 600px;
  display: flex;
  font-family: Arial, Helvetica, sans-serif;
}
// 所有的描述性文字的样式（主要是行高）
.desfont() {
  line-height: 1.8;
}
// 定义的 白色的描述性字体
.deswhite() {
  color: aliceblue;
  font-size: 600;
}
.h4() {
  font-size: 18px;
}
.content-1 {
  background: url('/images/background/home_1_1.jpg');
  .basecontent();
  flex-direction: column;
  .content-1-title {
    display: flex;
    justify-content: center;
    flex: 1;
    flex-direction: column;
    align-items: center;
    h1 {
      display: flex;
      justify-content: center;
      flex: 1;
      font-weight: 700;
      color: rgba(255, 255, 255, 0.849);
    }
    h4 {
      display: flex;
      justify-content: center;
      flex: 3;
      // color: rgba(199, 190, 159, 0.801);
      color: aliceblue;
      font-size: 600;
      width: 50%;
      .desfont();
      .h4();
    }
  }
}
// 具体的介绍含导航栏
.content-introduce {
  .basecontent();
  // display: flex;
  background: url('/images/background/home_1_9.jpg');
  flex-direction: row;
  justify-content: center;
  align-items: center;
  // width: 80%;
  ul {
    display: flex;
    flex: 1;
    flex-direction: column;
    align-items: flex-end;
    .desfont();
    .deswhite();
    // justify-content: flex-start;
  }
  .right-content {
    display: flex;
    flex: 2;
    // margin-left: 50px;
    h4 {
      padding: 100px;
      .desfont();
      .deswhite();
      .h4();
    }
  }
}
// goals
.content-2 {
  background: url('/images/background/home_1_2.jpg');
  .basecontent();
  .content-1-title {
    display: flex;
    flex-direction: row;
    h1 {
      display: flex;
      flex: 1;
      justify-content: center;
      align-items: center;
      color: aliceblue;
    }
    h4 {
      display: flex;
      flex: 1;
      align-items: center;
      color: aliceblue;
      width: 50%;
      // TODO:[*] 19-11-11暂时先加内间距
      padding: 100px;
      .desfont();
      .h4();
    }
  }
}
// mission
.content-3 {
  .basecontent();
  background: url('/images/background/home_1_3.jpg');
  .content-1-title {
    display: flex;
    flex-direction: column;
    h1 {
      display: flex;
      flex: 1;
      justify-content: center;
      color: aliceblue;
      align-items: center;
    }
    .minor_title {
      display: flex;
      flex: 1;
      // width: 70%;
      justify-content: center;
      color: aliceblue;
      h4 {
        width: 50%;
        .desfont();
        .h4();
      }
    }
  }
}
// area
.content-4 {
  background: url('/images/background/home_1_5.jpg');
  .basecontent();
  .content-1-title {
    display: flex;
    flex-direction: row;
    h1 {
      display: flex;
      flex: 1;
      justify-content: center;
      align-items: center;
      order: 2;
      color: aliceblue;
    }
    .minor_title {
      display: flex;
      flex: 1;
      // 交叉轴上的对齐方式
      align-items: center;
      h4 {
        display: flex;
        justify-content: center;
        flex: 1;
        order: 1;
        color: aliceblue;
        // TODO:[*] 19-11-11暂时先加内间距
        padding: 100px;
        .desfont();
        .h4();
      }
    }
  }
}

// 加入切换时的过度效果
// .tabcontent-enter-active,
// .tabcontent-leave-active {
//   transition: all 1s;
// }
// .tabcontent-enter,
// .tabcontent-leave-to {
//   opacity: 0;
//   transform: translateY(30px);
// }

.tabcontent-enter-active {
  animation: tabFade 1s;
}

@keyframes tabFade {
  0% {
    // background-color: yellow;
    opacity: 0;
    transform: translateY(30px);
  }
  100% {
    opacity: 1;
  }
}

// 0% {
//   background: black;
// }
// 100% {
//   background: red;
//   // opacity: 0;
//   // transform: translateY(30px);
// }
</style>
