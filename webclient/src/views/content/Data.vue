<template>
  <div class="center">
    <div class="center-header">
      <div class="buoy-overview">
        <h3>Buoy</h3>
          <div class="content">
          <p>North Sea Buoy hourly data including elements: buoy id with longitude and latitude; year, month, date, hour (UTC); sea level air pressure, sea level air temperature; significant wave height, maximum wave height; sea surface temperature; data file format .csv.</p>
          </div>
      </div>
      <div class="station-overview">
        <h3>Station</h3>
          <div class="content">
          <p>14 stations hourly data including elements: station name with longitude and latitude; year, month, date, hour (UTC); wind direction, wind speed; sea level air pressure, sea level air temperature; wave period, significant wave height, maximum wave height; swell direction, swell period, swell height; sea surface temperature; data file format .csv.</p>
          </div>
      </div>
      <div class="Ship-overview">
        <h3>Chinese volunteer ships</h3>
          <div class="content">
          <p>Hourly data including elements: ship name with longitude and latitude; year, month, date, hour (UTC); wind direction, wind speed; sea level air pressure, sea level air temperature; data file format .csv.</p>
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
<style scoped lang="less"></style>
