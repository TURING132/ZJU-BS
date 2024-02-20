<template>
    <top-bar :mobileFlag="mobileFlag"></top-bar>
    <template v-if="mobileFlag===1">
            <Menu :position_list="position_list" 
            @move_show="(device)=>{
                moveToLocation(device.latitude,device.longitude)
                showLabel(device.latitude,device.longitude)
            }"
            @show_history="(device)=>{
                showHistory(device)
            }"
            >
                
            </Menu>
    </template>
    <div class="container">
        <template v-if="mobileFlag===0">
            <div class="left-bar">
                <div v-for="(device) in position_list" :key="device.id" class="item-wrapper" 
                            @click="()=>{
                                moveToLocation(device.latitude,device.longitude)
                                showLabel(device.latitude,device.longitude)
                            }"
                >
                <!-- 显示设备名称和位置信息 -->
                    <p>设备:{{ device.name }}</p>
                    <img src="../assets/icon/history.svg" class="icon" title="显示历史位置"
                            @click="showHistory(device)"
                    >
                </div>
            </div>
        </template>
        
        <div class="map-container">
            <template v-if="historyDevice===null">
                <div class="title-wrapper">
                    <h1>我的设备</h1>
                    <img src="../assets/icon/return.svg" @click="()=>{$router.push('/main')}">
                </div>
            </template>
            <template v-else>
                <div class="title-wrapper">
                    <h1>{{historyDevice.name}}的历史位置</h1>
                    <img src="../assets/icon/return.svg" @click="()=>{returnFromHistory()}">
                </div>
            </template>
            
            <div class="map-wrapper">
                <div id="map" v-bind:class="mobileFlag===0?'PCrealmap':'MOrealmap'">
                    
                </div>
            </div>
        </div>
    </div>
    

</template>

<script>
import TopBar from "../components/TopBar.vue"
import Menu from "../components/map/Menu.vue"
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
export default{
    data(){
        return{
            mobileFlag:0,
            map:null,
            position_list:[
            ],
            history_list:null,
            historyDevice:null,
            historyDevicePolyline:null
        }
    },
    methods:{
        initMap(){
            let map = L.map("map", {
                center: [30.23086372926422, 120.21121938720704], // 中心位置
                zoom: 10, // 缩放等级
                // zoomAnimation:false,fadeAnimation:true,markerZoomAnimation:true,
                zoomControl: true //缩放控件
            });
            
            L.Icon.Default.imagePath = '/marker/'
            L.Popup.prototype._animateZoom = function (e) {//解决缩放时的变形问题
                if (!this._map) {
                    return
                }
                var pos = this._map._latLngToNewLayerPoint(this._latlng, e.zoom, e.center),
                    anchor = this._getAnchor()
                L.DomUtil.setPosition(this._container, pos.add(anchor))
            }

            this.map = map; // data上需要挂载
            L.tileLayer(
                "http://wprd04.is.autonavi.com/appmaptile?lang=zh_cn&size=1&style=7&x={x}&y={y}&z={z}"
            ).addTo(map) // 加载底图
        },
        moveToLocation(latitude, longitude) {
            this.map.setView([latitude, longitude], this.map.getZoom());
        },
        addMarkerAndPopup(latitude, longitude, label) {
            let marker = L.marker([latitude, longitude]).addTo(this.map);
            let popup = L.popup().setContent(label);
            marker.bindPopup(popup).openPopup();
        },
        showLabel(latitude,longitude){
            this.map.eachLayer((layer) => {
            if (layer instanceof L.Marker && layer.getLatLng().equals([latitude, longitude])) {
                    layer.openPopup();
                }
            });
        },
        async showHistory(device){
            // get history by id
            await this.getHistoryList(device)
            try{
                this.history_list.sort((a, b) => {
                    const timeA = new Date(a.timestamp);
                    const timeB = new Date(b.timestamp);
                    // 根据时间从早到晚排序
                    return timeA - timeB;
                });
                this.historyDevice = device
                this.map.eachLayer((layer) => {//去除标记和标签
                    if (layer instanceof L.Marker && !layer.getLatLng().equals([device.latitude, device.longitude])) {
                            layer.closePopup();
                            this.map.removeLayer(layer);
                    }
                });
                const historyLatLngs = this.history_list.map(({ latitude, longitude }) => [latitude, longitude]);
                if (this.historyDevicePolyline!=null) {
                    this.map.removeLayer(this.historyDevicePolyline);
                }
                this.historyDevicePolyline = L.polyline(historyLatLngs, { color: 'red' }).addTo(this.map);
                if (historyLatLngs.length > 0) {
                    const [firstLat, firstLng] = historyLatLngs[0];
                    this.moveToLocation(firstLat, firstLng);
                }
                for (const position of this.history_list) {
                    const options = { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit' };
                    const formattedTime = (new Date(position.timestamp)).toLocaleDateString('en-US', options);
                    const label = `<b>Time:</b> ${formattedTime}`;
                    this.addMarkerAndPopup(position.latitude, position.longitude, label);
                }
            }catch(e){
                console.log(e)
            }
            
        },
        returnFromHistory(){
            this.historyDevice = null
            if (this.historyDevicePolyline!=null) {
                this.map.removeLayer(this.historyDevicePolyline);
            }
            this.map.eachLayer((layer) => {//去除标记和标签
                if (layer instanceof L.Marker) {
                        layer.closePopup();
                        this.map.removeLayer(layer);
                }
            });
            for(const p of this.position_list){
                this.addMarkerAndPopup(p.latitude,p.longitude,p.name)
            }
            if(this.position_list.length!=0){
                this.moveToLocation(this.position_list[0].latitude,this.position_list[0].longitude)
            }
        },
        async getPositionList(){
            try{
                const response = await fetch(`http://127.0.0.1:8000/message/location_list?user_id=${this.$store.state.user_id}`,{
                    method: 'GET',
                });
                if (response.ok) {
                    const jsonResponse = await response.json();
                    if (jsonResponse.status === 'success') {
                        this.position_list = jsonResponse.position_list;
                        console.log('position_list',this.position_list)
                    } else {
                        alert(`获取位置列表错误: ${jsonResponse.message}`);
                    }
                } else {
                    alert(`网络错误: ${response.message}`);
                }
            } catch (error) {
                console.log(error)
                alert(`网络错误`);
            }
        },
        async getHistoryList(device){
            try{
                const response = await fetch(`http://127.0.0.1:8000/message/location_history?user_id=${this.$store.state.user_id}&device_id=${device.id}`,{
                    method: 'GET',
                });
                if (response.ok) {
                    const jsonResponse = await response.json();
                    if (jsonResponse.status === 'success') {
                        console.log('device',jsonResponse.history_list)
                        this.history_list = jsonResponse.history_list;
                    } else {
                        alert(`获取位置历史错误: ${jsonResponse.message}`);
                    }
                } else {
                    alert(`网络错误: ${response.message}`);
                }
            } catch (error) {
                console.log(error)
                alert(`网络错误`);
            }
        }
    },
    components:{
        TopBar,
        Menu,
    }
    ,
    created:function(){
        // 进行登陆状态检查
        if(this.$store.state.loginState===0){
            let loginInfo = JSON.parse(localStorage.getItem('loginInfo'))
            if(loginInfo===null){
                this.$router.push('/')
                return
            }else{
                this.$store.commit('changeLogin', loginInfo);
            }
        }
        
        // 进行设备类型检查
        var u = navigator.userAgent
        var isAndroid = u.indexOf('Android') > -1 || u.indexOf('Adr') > -1 //android
        var isiOS = !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/) //ios
        if (isiOS || isAndroid) {
            this.mobileFlag=1;
        } else {
            this.mobileFlag=0;
        } 
    },
    mounted:async function(){
        // 请求列表 position_list
        await this.getPositionList()
        // 因为需要dom元素来实现正确渲染，所以放在mounted
        this.initMap()
        for(const p of this.position_list){
            this.addMarkerAndPopup(p.latitude,p.longitude,p.name)
        }
        if(this.position_list.length!=0){
            this.moveToLocation(this.position_list[0].latitude,this.position_list[0].longitude)
        }
    }
}
</script>

<style scoped>
.container{
    display: flex;
}

.left-bar{
    flex: 0 0 350px;
    height: calc(100vh - 50px);
    backdrop-filter: blur(2px);
    background-color: rgba(217,217,217, 0.3);
}
.map-container{
    flex: 1;
    height: calc(100vh - 50px);

}
.item-wrapper{
    border-bottom: 1px #fff solid;
    color: #fff;
    font-size: 20px;
    display: flex;
    justify-content: space-between;
    height: 40px;
    align-items: center;
    padding: 0 20px;

    transition: 0.3s;
}
.item-wrapper:hover{
    background-color: rgba(217,217,217, 0.7);
    color: #144E2E;

}
.icon{
    height: 20px;
    transition: 0.3s;
    cursor: pointer;
}
.icon:hover{
    transform: scale(1.3);
}
.icon:active{
    transform: scale(0.9);
}

.title-wrapper{
    height: 80px;
    padding: 0 40px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.title-wrapper img{
    height: 32px;
    cursor: pointer;
    transition: transform 0.3s ease-in-out;
}
.title-wrapper img:hover{
    transform: scale(1.2);
}
.title-wrapper img:active{
    transform: scale(0.9);
}
.title-wrapper h1{
    color: #fff;
    font-size: 32px;
    font-weight: bold;
}
.map-wrapper{
    box-sizing: border-box;
    height: calc(100vh - 50px - 80px - 20px);
    padding: 0 20px;
}
.PCrealmap {
    box-sizing: border-box;
    width: calc(100vw - 350px - 40px);
    height: calc(100vh - 50px - 80px - 20px);
    border-radius: 15px;
}
.MOrealmap{
    box-sizing: border-box;
    width: calc(100vw - 40px);
    height: calc(100vh - 50px - 80px - 20px - 30px);
    border-radius: 15px;
}
</style>