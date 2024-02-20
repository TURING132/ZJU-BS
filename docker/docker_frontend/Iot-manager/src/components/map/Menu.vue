<template>
  
    <template v-if="this.show===0">
        <div class="container-short">
            <img src="../../assets/down_arrow.svg" class="arrow" @click="()=>{this.show=1}">
        </div>
    </template>
    <template v-else>
        <div class="container-long">
            <img src="../../assets/up_arrow.svg" class="arrow" @click="()=>{this.show=0}">
            <div v-for="(device) in position_list" :key="device.id" class="item-wrapper" 
                            @click="()=>{
                                this.$emit('move_show',device)
                            }"
                >
                <!-- 显示设备名称和位置信息 -->
                    <p>设备:{{ device.name }}</p>
                    <img src="../../assets/icon/history.svg" class="icon" title="显示历史位置"
                            @click="()=>{
                                this.$emit('show_history',device)
                            }"
                    >
            </div>
        </div>

    </template>
    
   
</template>

<script>
export default {
    data(){
        return{
            show: 0
        }
    },
    props:{
        position_list:Array
    }
}
</script>

<style scoped>
.container-short{
    height: 30px;
    width: 100vw;
    backdrop-filter: blur(2px);
    background-color: rgba(217,217,217, 0.3);
    transition: 0.3s;
    display: flex;
    justify-content: center;
}
.container-long{
    height: 70vh;
    width: 100vw;
    backdrop-filter: blur(2px);
    background-color: rgba(217,217,217, 0.3);
    transition: 0.3s;
    justify-content: center;
}
.item-wrapper{
    height: 40px;
    border-bottom: 1px solid #fff;
    display: flex;
    justify-content: space-between;
    padding: 0 20px;
    align-items: center;
    color: #fff;
}
.arrow{
    box-sizing: border-box;
    height: 30px;
    width: 100vw;
    border-bottom: 1px solid #fff;
    display: flex;
    justify-content: center;
}
.icon{
    height: 20px;
}


</style>