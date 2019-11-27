<template>
  <div id="footer">
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
      <div>
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
  }
}
</style>
