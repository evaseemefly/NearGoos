<template>
  <div class="my-root">
    <header>
      <div class="main-title">
        <!-- header 加几个logo -->
        <div class="logo">
          <!-- <img src="static/nf-logo.png"> -->
          <img src="/images/logo/nmefclog.png" />
          <img src="/images/logo/ioclog.png" />
        </div>
        <ul>
          <li>Home</li>
          <li>OverView</li>
          <li>Data</li>
          <li>Product</li>
        </ul>
      </div>
    </header>
    <div class="my-content">
      <div class="minor-title">
        <h2>NEAR-GOOS China RTDB</h2>
        <h4>
          North-East Asian Regional Global Ocean Observing System (NEAR-GOOS),
          China Real-Time Data Base, run by National Marine Environmental
          Forecasting Center (NMEFC)
        </h4>
        <button class="btn btn-default">Download Data</button>
      </div>
    </div>
    <footer>
      <!-- 选择成员国的友情链接 -->
      <div class="db-select">
        <div class="dropdown">
          <button
            class="btn btn-default dropdown-toggle"
            type="button"
            id="db"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="true"
          >
            Database
            <span class="caret"></span>
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenu1">
            <li><a href="#">China</a></li>
            <li><a href="#">Japan</a></li>
            <li><a href="#">Korea</a></li>
            <li><a href="#">Russia</a></li>
          </ul>
        </div>
      </div>
      <!-- 成员国 -->
      <div class="members">
        <h4>NEAR-GOOS Members Countries</h4>
        <div class="members-img">
          <img src="/images/logo/chn.jpg" />
          <img src="/images/logo/jap.jpg" />
          <img src="/images/logo/korea.jpg" />
          <img src="/images/logo/rus.jpg" />
        </div>
      </div>
      <!-- 版权 -->
      <div class="copyright">
        <h4>
          Copyright ©right;
        </h4>
        <h4>2013 National Marine Environment Forecasting Center(NMEFC)</h4>
        <h4>All Rights Reserved</h4>
      </div>
    </footer>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "home",
  components: {
    HelloWorld
  }
};
</script>

<style scoped lang="less">
.my-root {
  background: url("/images/background/home_1_7.jpg");
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  .my-content {
    display: flex;
    flex: 10;
    // background: #7f9943;
    .minor-title {
      @minortitle();
    }
  }
}

// 沿主轴居中常量
@centered: {
  display: flex;
  justify-content: center;
};

// 含图片的背景
@basecontent: {
  //   height: 600px;
  //   display: flex;
};
// 所有的描述性文字的样式（主要是行高）
@desfont: {
  line-height: 1.8;
  font-family: Arial, Helvetica, sans-serif;
  text-shadow: 2px 2px 10px #000;
};

footer {
  height: 100px;
  /* flex: 1; */
  //   background: darkcyan;
}

@minortitle: {
  display: flex;
  color: whitesmoke;
  // flex: row;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  font-size: 20px;
  font-size: 600;
  @basecontent();
  h2 {
    @desfont();
  }
  h4 {
    width: 50%;
    @desfont();
  }
  button {
    background: rgba(212, 132, 28, 0.815);
    color: white;
    font-size: 20px;
  }
};

// header的父类
@header: {
  // div底图
  // 上面url tab
  // 中间居中title
  // 下面一个button
  //   background: url("image/home_1_2.jpg");
  // height: 100px;
  display: flex;
  flex: 2;
  flex-direction: column;
  //底部增加一个内padding
  padding-bottom: 50px;
  .logo {
    img {
      height: 100px;
    }
  }
  .main-title {
    display: flex;
    flex-direction: row;
    justify-content: center;
    color: wheat;
    font-weight: 700;
    font-size: 30px;
    align-items: center;
    ul {
      display: flex;
      flex-direction: row;

      li {
        padding-right: 1em;
        // 去掉li的圆点
        list-style: none;
      }
    }
  }
};
//footer的父类
@footer: {
  //   background: url("image/home_1_2.jpg");
  background: rgba(47, 221, 221, 0.329);
  display: flex;
  flex: 1;
  justify-content: space-around;
  align-items: center;
  .db-select {
    display: flex;
    flex: 1;
    @centered();
  }
  .members {
    display: flex;
    flex-direction: column;
    flex: 1;
    justify-content: center;
    h4 {
      color: white;
      @centered();
    }
    .members-img {
      @centered();
      img {
        margin-right: 0.25em;
      }
    }
  }
  .copyright {
    display: flex;
    flex-direction: column;
    flex: 1;
    justify-content: center;
    h4 {
      color: white;
    }
  }
};

// 定义的 白色的描述性字体
.deswhite() {
  color: aliceblue;
  font-size: 600;
}
header {
  // .header();
  @header();
}

footer {
  @footer();
  //   @footer();
}
</style>
