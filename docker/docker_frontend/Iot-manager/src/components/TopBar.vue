<template>
    <div v-if = "mobileFlag===0" class = "PCbar-container">
        <img src="../assets/logo.svg" class = "PClogo" @click="()=>{$router.push('/main')}">
        <template  v-if = "this.$store.state.loginState==1">
            <span class="PCuser-name">{{this.$store.state.username}}</span>
            <span class="PClogout" @click="logout">退出登录</span>
        </template>
        <a href="https://github.com/TURING132"><img src="../assets/github.svg" class = "PCgithub"></a>
    </div>
    <div v-else class = "MObar-container">
        <img src="../assets/logo.svg" class = "MOlogo" @click="()=>{$router.push('/main')}">
        <template  v-if = "this.$store.state.loginState==1">
            <span class="MOuser-name">{{this.$store.state.username}}</span>
            <span class="MOlogout" @click="logout">退出登录</span>
        </template>
        <a href="https://github.com/TURING132"><img src="../assets/github.svg" class = "MOgithub"></a>
    </div>
</template>

<script>
export default {
    props:{
        mobileFlag:Number
    },
    methods:{
        logout(){
            // TODO: test
            localStorage.clear()
            this.$router.push('/')
            this.$store.commit('changeLogin', {
                loginState: 0,
                username: '',
                email: '',
                user_id:null
            });
        }
    }
}
</script>

<style>
    .PCbar-container{
        box-sizing: border-box;
        height:50px;
        padding-top: 10px;
        padding-left: 20px;
        padding-right: 20px;
        border-bottom: 1px solid white;

        display: flex;
        justify-content: space-between;
        align-items: center; 

        backdrop-filter: blur(2px);
        background-color: rgba(217,217,217, 0.3);

    }
    .PClogo{
        margin-left: 15px;
        height: 30px;
        align-self: flex-start;
        fill: #FFF;
        cursor: pointer;
    }
    .PCgithub{
        margin-right: 15px;
        height: 30px;
        align-self: flex-start;
        
    }
    .PCuser-name{
        margin-left: 60%;
        color: #FFF;
    }
    .PClogout{
        color: #FFF;
        cursor: pointer;
    }

    
    .MObar-container{
        box-sizing: border-box;
        width: 100vw;
        height:50px;
        padding: 10px;
        border-bottom: 1px solid white;

        display: flex;
        justify-content: space-between;
        align-items: center; 

        backdrop-filter: blur(2px);
        background-color: rgba(217,217,217, 0.3);
    }
    .MOlogo{
        height: 30px;
        align-self: flex-start;
        fill: #FFF;
        cursor: pointer;
    }
    .MOgithub{
        height: 30px;
        align-self: flex-start;
        
    }
    .MOuser-name{
        margin-left: 50px;
        color: #FFF;
        font-size: 14px;
    }
    .MOlogout{
        color: #FFF;
        cursor: pointer;
        font-size: 14px;
    }
    

</style>