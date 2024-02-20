<template>
    <top-bar :mobileFlag="mobileFlag"></top-bar>
    <div class="container">
        <h1 class="title">IoT Manager</h1>
        <login-card :mobileFlag="mobileFlag"></login-card>
    </div>
</template>

<script>
import TopBar from "../components/TopBar.vue"
import LoginCard from "../components/login/LoginCard.vue"

export default{
    data(){
        return{
            mobileFlag:0
        }
    },
    components:{
        TopBar,
        LoginCard
    }
    ,
    created:function(){
        // 进行登陆状态检查
        if(this.$store.state.loginState===0){
            // 如果vuex显示没有登陆，去localstorage找
            let loginInfo = JSON.parse(localStorage.getItem('loginInfo'))
            if(loginInfo===null){
                // do nothing
            }else{
                this.$store.commit('changeLogin', loginInfo);
                this.$router.push('/main')
                return
            }
        }else{
            this.$router.push('/main')
            return
        }
        // 进行设备类型检查
        var u = navigator.userAgent
        var isAndroid = u.indexOf('Android') > -1 || u.indexOf('Adr') > -1 //android
        var isiOS = !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/) //ios
        if (isiOS || isAndroid) {
            this.mobileFlag=1;
        } else {
            this.mobileFlag=0;
        }  //set mobile
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
    margin-bottom: 40px;
    margin-top: -120px;
    color: #fff;
    font-size: 32px;
    font-weight: bold;
    letter-spacing: 0.1em;
}
</style>