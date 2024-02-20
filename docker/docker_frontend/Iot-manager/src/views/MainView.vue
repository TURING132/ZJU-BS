<template>
    <top-bar :mobileFlag="mobileFlag"></top-bar>
    <template v-if="mobileFlag===0">
        <div class="container">
            <div class="left-bar">
                <histo-chart :devices="devices" :deviceType="deviceType">

                </histo-chart>
                <line-chart :devices="devices" >

                </line-chart>
                <button class="map-button" @click="()=>{$router.push('/map')}">在地图上查看</button>
            </div>
            <div class="my-device">
                <template v-if="selectedDevice===null && addedDevice===null">
                    <div class="title-wrapper">
                    <h1 >我的设备 <span class="online">在线数量: {{this.onlineCount}} 离线数量: {{this.offlineCount}}</span></h1>
                    <img src="../assets/icon/plus-circle.svg" @click="addNewDevice">
                    </div>
                    <div class="card-wrapper">
                        <device-card 
                            v-for="device in devices"
                            :key="device.id"
                            :info="device"
                            @click="handleClick(device)"
                            class="device-card"
                        ></device-card>
                    </div>
                </template>
                <template v-else-if="addedDevice!=null">
                    <!-- TODO -->
                    <div class="title-wrapper">
                        <h1 >我的设备</h1>
                        <img src="../assets/icon/return.svg" @click="returnFromAdd">
                    </div>
                    <div class="set-wrapper">
                        <div class="set-title-wrapper">
                            <h2 >添加设备</h2>
                            <h3 @click="addConfirm" class="confirm">确定</h3>
                        </div>
                        <div class="device-type">
                            <label for="deviceType">设备类型</label>
                            <select id="deviceType" v-model="addedDevice.type">
                                <option v-for="(item, index) in deviceType" :key="index" :value="item.type">
                                    {{ item.cn }}
                                </option>
                            </select>
                        </div>
                        <div class="device-id">
                            <label for="deviceId">设备id</label>
                            <input type="text" id="deviceName" v-model="addedDevice.id">
                        </div>
                        <div class="device-name">
                            <label for="deviceName">设备名称</label>
                            <input type="text" id="deviceName" v-model="addedDevice.name">
                        </div>
                        <div class="device-location">
                            <label for="deviceLocation">设备位置</label>
                            <input type="text" id="deviceLocation" v-model="addedDevice.location">
                        </div>
                    </div>
                </template>
                <template v-else-if="selectedDevice!=null">
                    <div class="title-wrapper">
                        <h1>我的设备</h1>
                        <img src="../assets/icon/return.svg" @click="returnFromSet">
                    </div>
                    <div class="set-wrapper">
                        <div class="set-title-wrapper">
                            <h2 >设备信息</h2>
                            <h3 @click="setConfirm" class="confirm">确定</h3>
                        </div>
                        <div class="device-type">
                            <label for="deviceType">设备类型</label>
                            <select id="deviceType" v-model="selectedDevice.type">
                                <option v-for="(item, index) in deviceType" :key="index" :value="item.type">
                                    {{ item.cn }}
                                </option>
                            </select>
                        </div>
                        <div class="device-name">
                            <label for="deviceName">设备名称</label>
                            <input type="text" id="deviceName" v-model="selectedDevice.name">
                        </div>
                        <div class="device-location">
                            <label for="deviceLocation">设备位置</label>
                            <input type="text" id="deviceLocation" v-model="selectedDevice.location">
                        </div>
                        <div class="device-message">
                            <label >设备消息 正常信息:{{this.messageCount.normal}} 警告信息:{{this.messageCount.warning}} </label>
                            <div class="messag-box">
                                <div v-for="(message, index) in messageList" :key="index" :class="message.type">
                                    <p>{{ formatTimestamp(message.timestamp) }}</p>
                                    <p>{{ message.text }}</p>
                                    <br>
                                </div>
                            </div>
                        </div>
                    </div>
                </template>
            </div>
        </div>
    </template>
    
    <template v-else>
        <div class="container">
            <div class="my-device">
                <template v-if="selectedDevice===null && addedDevice===null">
                    <div class="MOtitle-wrapper">
                        <h1 >我的设备 <span class="online">在线数量: {{this.onlineCount}} 离线数量: {{this.offlineCount}}</span></h1>
                        <img src="../assets/icon/plus-circle.svg" @click="addNewDevice">
                        </div>
                        <div class="MOcard-wrapper">
                            <m-o-device-card
                                v-for="device in devices"
                                :key="device.id"
                                :info="device"
                                :mobileFlag="mobileFlag"
                                @click="handleClick(device)"
                                class="device-card"
                            ></m-o-device-card>
                        </div>
                        <button class="MOmap-button" @click="()=>{$router.push('/map')}">在地图上查看</button>
                </template>
                <template v-else-if="addedDevice!=null">
                    <!-- TODO -->
                    <div class="MOtitle-wrapper">
                        <h1 >我的设备</h1>
                        <img src="../assets/icon/return.svg" @click="returnFromAdd">
                    </div>
                    <div class="set-wrapper">
                        <div class="MOset-title-wrapper">
                            <h2 >添加设备</h2>
                            <h3 @click="addConfirm" class="confirm">确定</h3>
                        </div>
                        <div class="device-type">
                            <label for="deviceType">设备类型</label>
                            <select id="deviceType" v-model="addedDevice.type">
                                <option v-for="(item, index) in deviceType" :key="index" :value="item.type">
                                    {{ item.cn }}
                                </option>
                            </select>
                        </div>
                        <div class="device-id">
                            <label for="deviceId">设备id</label>
                            <input type="text" id="deviceName" v-model="addedDevice.id">
                        </div>
                        <div class="device-name">
                            <label for="deviceName">设备名称</label>
                            <input type="text" id="deviceName" v-model="addedDevice.name">
                        </div>
                        <div class="device-location">
                            <label for="deviceLocation">设备位置</label>
                            <input type="text" id="deviceLocation" v-model="addedDevice.location">
                        </div>
                    </div>
                </template>
                <template v-else-if="selectedDevice!=null">
                    <div class="MOtitle-wrapper">
                        <h1>我的设备</h1>
                        <img src="../assets/icon/return.svg" @click="returnFromSet">
                    </div>
                    <div class="set-wrapper">
                        <div class="MOset-title-wrapper">
                            <h2 >设备信息</h2>
                            <h3 @click="setConfirm" class="confirm">确定</h3>
                        </div>
                        <div class="device-type">
                            <label for="deviceType">设备类型</label>
                            <select id="deviceType" v-model="selectedDevice.type">
                                <option v-for="(item, index) in deviceType" :key="index" :value="item.type">
                                    {{ item.cn }}
                                </option>
                            </select>
                        </div>
                        <div class="device-name">
                            <label for="deviceName">设备名称</label>
                            <input type="text" id="deviceName" v-model="selectedDevice.name">
                        </div>
                        <div class="device-location">
                            <label for="deviceLocation">设备位置</label>
                            <input type="text" id="deviceLocation" v-model="selectedDevice.location">
                        </div>
                        <div class="device-message">
                            <label >设备消息 正常信息:{{this.messageCount.normal}} 警告信息:{{this.messageCount.warning}} </label>
                            <div class="messag-box">
                                <div v-for="(message, index) in messageList" :key="index" :class="message.type">
                                    <p>{{ formatTimestamp(message.timestamp) }}</p>
                                    <p>{{ message.text }}</p>
                                    <br>
                                </div>
                            </div>
                        </div>
                    </div>
                </template>
            </div>
        
        </div>
    </template>
    
    

</template>

<script>
import TopBar from "../components/TopBar.vue"
import HistoChart from "../components/main/HistoChart.vue"
import LineChart from "../components/main/LineChart.vue"
import DeviceCard from "../components/main/DeviceCard.vue"
import MODeviceCard from "../components/main/MODeviceCard.vue"
export default{
    data(){
        return{
            mobileFlag:0,
            devices:[
            ],
            deviceType:[
                {type:"light",cn:"照明"},
                {type:"music",cn:"音乐"},
                {type:"door_window",cn:"门窗"},
                {type:"curtain",cn:"窗帘"},
                {type:"tv",cn:"电视"},
                {type:"temperature",cn:"环境"},
                {type:"car",cn:"出行"},
                {type:"internet",cn:"网络"},
                {type:"aircondition",cn:"空调"},
                {type:"camera",cn:"摄像头"},
                {type:"sensor",cn:"传感器"},
                {type:"other",cn:"其他"},
            ],
            selectedDevice:null,
            addedDevice:null,
            messageList: [],
            messageCount:{'normal':0,'warning':0},
            onlineCount: 0,
            offlineCount: 0,
        }
    },
    methods:{
        async handleClick(device){
            // 操作DOM
            const clickedElement = event.target;
            if(clickedElement.classList.contains('device-card-wrapper-close')
                ||clickedElement.classList.contains('device-card-wrapper-open')
                ||clickedElement.classList.contains('logo')
                ||clickedElement.classList.contains('MOdevice-card-wrapper-close')
                ||clickedElement.classList.contains('MOdevice-card-wrapper-open')
                ||clickedElement.classList.contains('MOlogo')){
                if(device.is_online){
                    device.status = device.status === 'on'? 'off':'on'; 
                    // 将消息发送给mqtt
                    const request = {
                        device_id: device.id,
                        message: device.status == "on"?"打开设备":"关闭设备"
                    };
                    try{
                        const response = await fetch('http://127.0.0.1:8000/mqtt/post', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify(request),
                        });

                        if (response.ok) {
                            const jsonResponse = await response.json();
                            if (jsonResponse.status === 'success') {
                            } else {
                                alert(`发送mqtt消息失败: ${jsonResponse.message}`);
                            }
                        } else {
                            alert(`网络错误: ${response.message}`);
                        }
                    } catch (error) {
                        console.log(error)
                        alert(`网络错误`);
                    }
                    // 将改动发送回后端
                    const requestData = {
                        user_id: this.$store.state.user_id,
                        device_id: device.id,
                        device_status: device.status
                    };
                    try{
                        const response = await fetch('http://127.0.0.1:8000/device/modify', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify(requestData),
                        });

                        if (response.ok) {
                            const jsonResponse = await response.json();
                            // 根据服务器返回的status和message进行响应
                            if (jsonResponse.status === 'success') {
                                this.getDeviceList()
                            } else {
                                alert(`新建设备失败: ${jsonResponse.message}`);
                            }
                        } else {
                            alert(`网络错误: ${response.message}`);
                        }
                    } catch (error) {
                        alert(`网络错误`);
                    }
                }
            }else{
                this.selectedDevice = { ...device }
                // 同时请求信息列表
                try{
                    const response = await fetch(`http://127.0.0.1:8000/device/get_message?user_id=${this.$store.state.user_id}&device_id=${device.id}`,{
                        method: 'GET',
                    });
                    if (response.ok) {
                        const jsonResponse = await response.json();
                        if (jsonResponse.status === 'success') {
                            this.messageList = jsonResponse.message_list;
                            this.messageList.forEach(message => {
                                if(message.type === 'normal' || message.type === 'location'){
                                    this.messageCount.normal ++
                                }else{
                                    this.messageCount.warning ++
                                }
                            })
                        } else {
                            alert(`获取设备列表错误: ${jsonResponse.message}`);
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
        async addConfirm(){
            // 增加设备
            let addedDevice = this.addedDevice
            if (!addedDevice.name || typeof addedDevice.name !== 'string' || addedDevice.name.trim() === ''
                || !addedDevice.type || typeof addedDevice.type !== 'string' || addedDevice.type.trim() === ''
                || !addedDevice.location || typeof addedDevice.location !== 'string' || addedDevice.location.trim() === ''
                || !addedDevice.id || typeof addedDevice.id !== 'string' || addedDevice.id.trim() === '') {
                alert("添加失败，有未填写的信息")
            }
            const requestData = {
                user_id: this.$store.state.user_id,
                device_id: addedDevice.id,
                device_name: addedDevice.name,
                device_location: addedDevice.location,
                device_type: addedDevice.type 
            };
            try {
                const response = await fetch('http://127.0.0.1:8000/device/add', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(requestData),
                });

                if (response.ok) {
                    const jsonResponse = await response.json();
                    // 根据服务器返回的status和message进行响应
                    if (jsonResponse.status === 'success') {
                        this.getDeviceList()
                        alert('新建设备成功')
                    } else {
                        alert(`新建设备失败: ${jsonResponse.message}`);
                    }
                } else {
                    alert(`网络错误: ${response.message}`);
                }
            } catch (error) {
                console.log(error)
                // 处理网络请求失败的逻辑
                alert('网络错误');
            }
            
        },
        async setConfirm(){
            // 归0count
            this.messageCount.normal = 0
            this.messageCount.warning = 0
            // 更改设备属性
            let selectedDevice = this.selectedDevice
            if (!selectedDevice.name || typeof selectedDevice.name !== 'string' || selectedDevice.name.trim() === ''
                || !selectedDevice.type || typeof selectedDevice.type !== 'string' || selectedDevice.type.trim() === ''
                || !selectedDevice.location || typeof selectedDevice.location !== 'string' || selectedDevice.location.trim() === '') {
                alert("添加失败，有未填写的信息")
            }
            const requestData = {
                user_id: this.$store.state.user_id,
                device_id: selectedDevice.id,
                device_name: selectedDevice.name,
                device_location: selectedDevice.location,
                device_type: selectedDevice.type,
                device_status: selectedDevice.status
            };
            try {
                // TODO: test
                const response = await fetch('http://127.0.0.1:8000/device/modify', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(requestData),
                });

                if (response.ok) {
                    const jsonResponse = await response.json();
                    // 根据服务器返回的status和message进行响应
                    if (jsonResponse.status === 'success') {
                        alert("更改设备属性成功")
                        this.getDeviceList()
                    } else {
                        alert(`新建设备失败: ${jsonResponse.message}`);
                    }
                } else {
                    alert(`网络错误: ${response.message}`);
                }
            } catch (error) {
                // 处理网络请求失败的逻辑
                alert('网络错误');
            }
        },
        async getDeviceList(){
            const user_id = this.$store.state.user_id
            try{
                const response = await fetch(`http://127.0.0.1:8000/device/get?user_id=${user_id}`,{
                    method: 'GET',
                });
                if (response.ok) {
                    const jsonResponse = await response.json();
                    if (jsonResponse.status === 'success') {
                        this.devices = jsonResponse.devices;
                        this.onlineCount = this.devices.filter(device => device.is_online).length;
                        this.offlineCount = this.devices.length - this.onlineCount;
                        this.devices.sort((a, b) => {
                            // 将 is_online 为 true 的设备排在前面
                            return a.is_online === b.is_online ? 0 : a.is_online ? -1 : 1;
                        });
                        console.log(this.devices)
                    } else {
                        alert(`获取设备列表错误: ${jsonResponse.message}`);
                    }
                } else {
                    alert(`网络错误: ${response.message}`);
                }
            } catch (error) {
                console.log(error)
                alert(`网络错误`);
            }
        }
        ,
        returnFromSet(){
            this.messageCount.normal = 0
            this.messageCount.warning = 0
            this.selectedDevice = null;
        },
        addNewDevice(){
            this.addedDevice = {name:"",type:"",location:"",id:""};
        },
        returnFromAdd(){
            this.addedDevice = null; 
        },
        padZero(number) {
            return number.toString().padStart(2, '0');
        },
        formatTimestamp(timestamp){
            const date = new Date(timestamp);
            const formattedDate = `${date.getFullYear()}-${this.padZero(date.getMonth() + 1)}-${this.padZero(date.getDate())} ${this.padZero(date.getHours())}:${this.padZero(date.getMinutes())}:${this.padZero(date.getSeconds())}`;
            return formattedDate;
        }
    },
    components:{
    TopBar,
    HistoChart,
    LineChart,
    DeviceCard,
    MODeviceCard,
    MODeviceCard
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
        // 请求设备列表
        this.getDeviceList()
    },
    mounted(){
        
    }
}
</script>

<style scoped>

.container{
    display: flex;
}
.left-bar{
    flex: 0 0 550px;
    height: calc(100vh - 50px);
    backdrop-filter: blur(2px);
    background-color: rgba(217,217,217, 0.3);

    flex-direction: column;
    display: flex;
    align-items: center;
    justify-content:space-around;
    
}
.map-button{
    width: 350px;
    height: 50px;
    border: 1px solid #fff; 
    border-radius: 15px;
    padding: 5px; 
    margin: 10px 0; 
    box-sizing: border-box;
    background-color: transparent;
    font-size: 18px; 
    color: #fff;
    text-align: center; 
    transition: background-color 0.3s;
    
    cursor: pointer;
}
.map-button:hover{
    background-color: rgba(255,255,255,0.7); 
    color: #144E2E;
}
.my-device{
    flex: 1;
    height: calc(100vh - 50px);
}
.my-device .title-wrapper{
    height: 80px;
    padding: 0 40px;
    margin-bottom: -20px;
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
.title-wrapper .online{
    font-size: 14px;
    color: rgba(255,255,255,0.5);
}
.my-device h1{
    color: #fff;
    font-size: 32px;
    font-weight: bold;
}
.card-wrapper{
    height: calc(100vh - 80px - 50px + 20px);
    padding-left: 20px;
    overflow-y: auto;
}

.card-wrapper::-webkit-scrollbar {
  width: 12px;
}

.card-wrapper::-webkit-scrollbar-thumb {
  background-color: #525252;
  border-radius: 6px;
}

.card-wrapper::-webkit-scrollbar-track {
  background-color: rgba(255,255,255,0.5);
}

.device-card{
    float: left;
}

.set-wrapper{
    color: #fff;
    height: calc(100vh - 100px - 50px);
    background-color: rgba(155,155,155,0.3);
    backdrop-filter: blur(5px);
    padding: 0 40px;
    margin: 10px 40px;
    border-radius: 10px;
    display: flex;
    flex-direction: column;

}
.set-title-wrapper{
    height: 100px;
    

    display: flex;
    align-items: center;
    justify-content:space-between;
    
    color: #fff;
}
.set-title-wrapper h2{
    font-size: 32px;
}
.set-title-wrapper h3{
    font-size: 28px;
}
.set-title-wrapper .confirm{
    cursor: pointer;
}
.set-wrapper input,select{
    box-sizing: border-box;
    box-shadow: none;
    height: 45px;
    border-radius: 10px;
    width: 100%;
    background-color: #fff;
    border: 1px #fff solid;
    padding-left: 20px;
}

.set-wrapper input:placeholder{
    color: #144E2E;;
}
.set-wrapper .device-type{
    height: 100px;
}   

.set-wrapper .device-name{
    height: 100px;
}

.set-wrapper .device-location{
    height: 100px;
}

.set-wrapper .device-id{
    height: 100px;
}

.set-wrapper .device-message .messag-box{
    color: #000;
    box-sizing: border-box;
    padding: 10px;
    overflow-y: auto;

    border: 1px solid #fff;
    background-color: #fff;
    border-radius: 10px;
    height: 180px;
}

.messag-box .warning{
    color: red
}

.messag-box .normal{
    color: black
}

.set-wrapper .device-message p::-webkit-scrollbar-thumb {
  background-color: #525252;
  border-radius: 6px;
}

.set-wrapper .device-message p::-webkit-scrollbar-track {
  background-color: rgba(255,255,255,0.5);
}

.set-wrapper label{
    margin-bottom: 10px;
    display: block;
}
/* ---------------- */
.my-device .MOtitle-wrapper{
    height: 80px;
    padding: 0 20px;
    margin-bottom: -20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.MOtitle-wrapper img{
    height: 32px;
    cursor: pointer;
    transition: transform 0.3s ease-in-out;
}
.MOtitle-wrapper img:hover{
    transform: scale(1.2);
}
.MOtitle-wrapper img:active{
    transform: scale(0.9);
}
.MOtitle-wrapper .online{
    font-size: 14px;
    color: rgba(255,255,255,0.5);
}
.MOmap-button{
    width: 80vw;
    height: 40px;
    border: 1px solid #fff; 
    border-radius: 15px;
    padding: 5px; 
    margin-left: calc(50vw - 40vw);
    box-sizing: border-box;
    background-color: transparent;
    font-size: 18px; 
    color: #fff;
    text-align: center; 
    transition: background-color 0.3s;
    
    cursor: pointer;
}
.MOmap-button:hover{
    background-color: rgba(255,255,255,0.7); 
    color: #144E2E;
}

.MOcard-wrapper{
    height: calc(100vh - 80px - 50px + 20px - 50px);
    /* padding-left: 10px; */
    overflow-y: auto;
}

.MOcard-wrapper::-webkit-scrollbar {
  width: 12px;
}

.MOcard-wrapper::-webkit-scrollbar-thumb {
  background-color: #525252;
  border-radius: 6px;
}

.MOcard-wrapper::-webkit-scrollbar-track {
  background-color: rgba(255,255,255,0.5);
}

.MOset-title-wrapper{
    height: 80px;
    display: flex;
    align-items: center;
    justify-content:space-between;
    
    color: #fff;
}
.MOset-title-wrapper h2{
    font-size: 24px;
}
.MOset-title-wrapper h3{
    font-size: 20px;
}
.MOset-title-wrapper .confirm{
    cursor: pointer;
}
</style>