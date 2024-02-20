<template>
    <template v-if="info.is_online==false||info.status==='off'">
        <div class="MOdevice-card-wrapper-close">
            <img v-if="info.type=='light'" src="../../assets/icon/light.svg" class="MOlogo">
            <img v-else-if="info.type=='music'" src="../../assets/icon/music.svg" class="MOlogo">
            <img v-else-if="info.type=='door_window'" src="../../assets/icon/door_window.svg" class="MOlogo">
            <img v-else-if="info.type=='curtain'" src="../../assets/icon/curtain.svg" class="MOlogo">
            <img v-else-if="info.type=='tv'" src="../../assets/icon/tv.svg" class="MOlogo">
            <img v-else-if="info.type=='temperature'" src="../../assets/icon/temperature.svg" class="MOlogo">
            <img v-else-if="info.type=='car'" src="../../assets/icon/car.svg" class="MOlogo">
            <img v-else-if="info.type=='internet'" src="../../assets/icon/internet.svg" class="MOlogo">
            <img v-else-if="info.type=='aircondition'" src="../../assets/icon/aircondition.svg" class="MOlogo">
            <img v-else-if="info.type=='camera'" src="../../assets/icon/camera.svg" class="MOlogo">
            <img v-else-if="info.type=='sensor'" src="../../assets/icon/sensor.svg" class="MOlogo">
            <img v-else src="../../assets/icon/other.svg" class="MOlogo">
            <div class="MOdev-name">{{info.name}}</div>
            <div v-if="info.is_online==false" class="MOoff-line">离线</div>
            <div v-else class="MOdev-status">关</div>
            <div class="MOdev-location">{{info.location}}</div>
        </div>
    </template>
    <template v-else-if="info.status==='on'">
        <div class="MOdevice-card-wrapper-open">
            <img v-if="info.type=='light'" src="../../assets/icon/light_g.svg" class="MOlogo">
            <img v-else-if="info.type=='music'" src="../../assets/icon/music_g.svg" class="MOlogo">
            <img v-else-if="info.type=='door_window'" src="../../assets/icon/door_window_g.svg" class="MOlogo">
            <img v-else-if="info.type=='curtain'" src="../../assets/icon/curtain_g.svg" class="MOlogo">
            <img v-else-if="info.type=='tv'" src="../../assets/icon/tv_g.svg" class="logo">
            <img v-else-if="info.type=='temperature'" src="../../assets/icon/temperature_g.svg" class="MOlogo">
            <img v-else-if="info.type=='car'" src="../../assets/icon/car_g.svg" class="MOlogo">
            <img v-else-if="info.type=='internet'" src="../../assets/icon/internet_g.svg" class="MOlogo">
            <img v-else-if="info.type=='aircondition'" src="../../assets/icon/aircondition_g.svg" class="MOlogo">
            <img v-else-if="info.type=='camera'" src="../../assets/icon/camera_g.svg" class="MOlogo">
            <img v-else-if="info.type=='sensor'" src="../../assets/icon/sensor_g.svg" class="MOlogo">
            <img v-else src="../../assets/icon/other_g.svg" class="MOlogo">

            <div class="MOdev-name">{{info.name}}</div>
            <div class="MOdev-status">开</div>
            <div class="MOdev-location">{{info.location}}</div>
        </div>
    </template>

    
    
</template>

<script>
export default {
    props:{
        info:{type: Object, required: true},
        mobileFlag:Number
    },
}
</script>

<style scoped>
.device-card-wrapper-close{
    width: 200px;
    height: 200px;
    border-radius: 10px;
    color: #fff;
    box-sizing: border-box;
    margin: 20px 20px;
    margin-right: 40px;
    padding-left: 20px;
    padding-right: 20px;

    background-color: rgba(155,155,155,0.3);
    backdrop-filter: blur(5px);
    display: flex;
    flex-direction: column;
    transition: transform 0.3s ease-in-out;
}

.device-card-wrapper-close:hover, .device-card-wrapper-open:hover{
    transform: scale(1.1);
    
}
.device-card-wrapper-close:active, .device-card-wrapper-open:active{
    transform: scale(0.9);   
}


.device-card-wrapper-open{
    width: 200px;
    height: 200px;
    border-radius: 10px;
    color: #144E2E;
    box-sizing: border-box;
    margin: 20px 20px;
    margin-right: 40px;
    padding-left: 20px;
    padding-right: 20px;

    background-color: rgba(255,255,255,0.5);
    backdrop-filter: blur(5px);
    display: flex;
    flex-direction: column;
    transition: transform 0.3s ease-in-out;
}



.logo{
    margin: 20px 0;
    width: 50px;
    height: 50px;
}
.dev-name{
    display: inline-block;
    margin-bottom: 15px;
    font-size: 20px;
    font-weight: bold;
    cursor: pointer;
}
.dev-status{
    display: inline-block;
    margin-bottom: 15px;
    font-size: 20px;
    cursor: pointer;
}
.dev-location{
    display: inline-block;
    font-size: 20px;
    cursor: pointer;
}
.off-line{
    display: inline-block;
    margin-bottom: 15px;
    font-size: 20px;
    color: rgba(255,255,255,0.5);
    cursor: pointer;
}

/* ------------------------- */
.MOdevice-card-wrapper-close{
    box-sizing: border-box;
    width: 170px;
    height: 170px;
    border-radius: 10px;
    color: #fff;
    box-sizing: border-box;
    margin: 10px 0;
    margin-left: 10px;
    padding-left: 20px;
    padding-right: 20px;

    background-color: rgba(155,155,155,0.3);
    backdrop-filter: blur(5px);
    display: flex;
    flex-direction: column;
    transition: transform 0.3s ease-in-out;
}


.MOdevice-card-wrapper-open{
    box-sizing: border-box;
    width: 170px;
    height: 170px;
    border-radius: 10px;
    color: #144E2E;
    box-sizing: border-box;
    margin: 10px 0;
    margin-left: 10px;
    
    padding-left: 20px;
    padding-right: 20px;

    background-color: rgba(255,255,255,0.5);
    backdrop-filter: blur(5px);
    display: flex;
    flex-direction: column;
    transition: transform 0.3s ease-in-out;
}


.MOlogo{
    margin-top: 10px;
    margin-bottom: 15px;
    width: 40px;
    height: 40px;
}
.MOdev-name{
    display: inline-block;
    margin-bottom: 15px;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
}
.MOdev-status{
    display: inline-block;
    margin-bottom: 15px;
    font-size: 18px;
    cursor: pointer;
}
.MOdev-location{
    display: inline-block;
    font-size: 18px;
    cursor: pointer;
}
.MOoff-line{
    display: inline-block;
    margin-bottom: 15px;
    font-size: 18px;
    color: rgba(255,255,255,0.5);
    cursor: pointer;
}


</style>