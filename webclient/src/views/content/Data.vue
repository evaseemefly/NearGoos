<template>
  <div class="center">
<div class="center-header ">
  <div class="cemter=header-welcome">
    <div class="title">
      <h1>WELCOME TO</h1><h1 class="importent">RTDB</h1>
    </div>
    <div class="content">
      <h2>To dowonload data, please read data introduction before  </h2>
    </div>
  </div>
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
<style scoped lang="less"></style>
