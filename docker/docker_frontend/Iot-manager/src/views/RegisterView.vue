<template>
  <top-bar :mobileFlag="mobileFlag"></top-bar>
    <div class="container">
        <h1 class="title">IoT Manage</h1>
        <h2 class="title2">注册账号</h2>
        <register-card :mobileFlag="mobileFlag"></register-card>
    </div>
</template>

<script>
import RegisterCard from '../components/register/RegisterCard.vue'
import TopBar from "../components/TopBar.vue"
export default {
    data(){
        return{
            mobileFlag: 0,
        }
    },
    components:{
        TopBar,
        RegisterCard,
    },
    created:function(){
        // 进行设备类型检查
        var u = navigator.userAgent
        var isAndroid = u.indexOf('Android') > -1 || u.indexOf('Adr') > -1 //android
        var isiOS = !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/) //ios
        if (isiOS || isAndroid) {
            this.mobileFlag=1;
        } else {
            this.mobileFlag=0;
        }  //set mobile
    },
    mounted(){
        
    }
}
</script>

<style scoped>
.container{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: calc(100vh - 50px);
    
}
.title{
    margin-bottom: 20px;
    margin-top: -120px;
    color: #fff;
    font-size: 32px;
    font-weight: bold;
    letter-spacing: 0.1em;
}
.title2{
    margin-bottom: 20px;
    color: #fff;
    font-size: 24px;
    font-weight: bold;
    letter-spacing: 0.1em;
}
</style>