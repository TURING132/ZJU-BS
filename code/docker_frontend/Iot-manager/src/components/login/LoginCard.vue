<template>
  <template v-if="mobileFlag===0">
    <div class="login-card">
      <input type="email" id="email" v-model="email" placeholder = "邮箱" required>
      <input type="password" id="password" v-model="password" placeholder = "密码" required>
      <button class="login-botton" @click="login">登陆</button>
      <p @click="()=>{this.$router.push('/register');console.log(111);}">注册账号</p>
    </div>
  </template>
  <template v-else>
    <div class="MOlogin-card">
      <input type="email" id="email" v-model="email" placeholder = "邮箱" required>
      <input type="password" id="password" v-model="password" placeholder = "密码" required>
      <button class="login-botton" @click="login">登陆</button>
      <p @click="()=>{this.$router.push('/register');console.log(111);}">注册账号</p>
    </div>
  </template>
</template>
<script>
import md5 from 'js-md5';
export default {
    props:{
        mobileFlag:Number
    },
    data(){
        return{
            email: "",
            password: ""
        }
    },
    methods:{
        async login(){
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(this.email)) {
                alert("邮箱格式错误");
            }
            if(this.email===""||this.password===""){
                alert("请填写邮箱和密码")
                return
            }
            const requestData = {
                email: this.email,
                password: md5(this.password),
            };
            try {
                
                const response = await fetch('http://127.0.0.1:8000/user/check', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(requestData),
                });

                if (response.ok) {
                    const jsonResponse = await response.json();
                    // 根据服务器返回的status和message进行响应
                    // 更新user_id字段
                    if (jsonResponse.status === 'success') {
                        let loginInfo = {
                            loginState: 1,
                            username: jsonResponse.username,
                            email: jsonResponse.email,
                            user_id: jsonResponse.user_id    
                        }
                        this.$store.commit('changeLogin', loginInfo);
                        localStorage.setItem('loginInfo',JSON.stringify(loginInfo))
                        this.$router.push('/main');
                    } else {
                        alert(`登陆失败: ${jsonResponse.message}`);
                    }
                } else {
                    alert(`网络错误: ${response.status}`);
                }
            } catch (error) {
                console.log(error)
                // 处理网络请求失败的逻辑
                alert('网络错误');
            }
        }
    }
}
</script>

<style>
.login-card{
    width: 400px;
    height: 240px;
    padding: 15px,0;
    border-radius: 17px;

    background-color: rgba(217,217,217, 0.3);
    backdrop-filter: blur(5px);

    display: flex;
    flex-direction: column;
    align-items:center;
    justify-content: center;
}

.login-card input[type="email"],
.login-card input[type="password"],
.login-card button {
    width: 350px;
    height: 40px;
    border: 1px solid rgba(255,255,255,0.7); 
    border-radius: 15px;
    padding: 5px; 
    margin: 10px 0; 
    box-sizing: border-box;
    background-color: transparent;
    font-size: 18px; 
    font-weight: bold;
    text-align: center; 
    
    transition: background-color 0.3s;
}

.login-card input[type="email"],
.login-card input[type="password"]{
    color: #144E2E;
}
.login-card button{
    color: rgba(255,255,255,0.7);
}

.login-card input[type="email"]:hover,
.login-card input[type="password"]:hover{
    background-color: rgba(255,255,255,0.7); 
}
.login-card input[type="email"]:hover::placeholder,
.login-card input[type="password"]:hover::placeholder{
    color: #144E2E;
}
.login-card button:hover {
    background-color: rgba(255,255,255,0.7); 
    color: #144E2E;
}
.login-card input[type="email"]::placeholder,
.login-card input[type="password"]::placeholder {
    color: rgba(255,255,255,0.7); /* placeholder颜色 */
    font-size: 16px; /* placeholder字体大小 */
    font-weight: bold;
}
.login-card p{
    color: #fff;
    margin-top: 10px;
    font-size: 13px;
    cursor: pointer;
}

/* ----------------------------- */

.MOlogin-card{
    width: 90vw;
    height: 240px;
    padding: 15px,0;
    border-radius: 17px;

    background-color: rgba(217,217,217, 0.3);
    backdrop-filter: blur(5px);

    display: flex;
    flex-direction: column;
    align-items:center;
    justify-content: center;
}

.MOlogin-card input[type="email"],
.MOlogin-card input[type="password"],
.MOlogin-card button {
    width: 80vw;
    height: 40px;
    border: 1px solid rgba(255,255,255,0.7); 
    border-radius: 15px;
    padding: 5px; 
    margin: 10px 0; 
    box-sizing: border-box;
    background-color: transparent;
    font-size: 18px; 
    font-weight: bold;
    text-align: center; 
    
    transition: background-color 0.3s;
}

.MOlogin-card input[type="email"],
.MOlogin-card input[type="password"]{
    color: #144E2E;
}
.MOlogin-card button{
    color: rgba(255,255,255,0.7);
}

.MOlogin-card input[type="email"]:hover,
.MOlogin-card input[type="password"]:hover{
    background-color: rgba(255,255,255,0.7); 
}
.MOlogin-card input[type="email"]:hover::placeholder,
.MOlogin-card input[type="password"]:hover::placeholder{
    color: #144E2E;
}

.MOlogin-card button:hover {
    background-color: rgba(255,255,255,0.7); 
    color: #144E2E;
}

.MOlogin-card input[type="email"]::placeholder,
.MOlogin-card input[type="password"]::placeholder {
    color: rgba(255,255,255,0.7); /* placeholder颜色 */
    font-size: 16px; /* placeholder字体大小 */
    font-weight: bold;
}
.MOlogin-card p{
    color: #fff;
    margin-top: 10px;
    font-size: 13px;
    cursor: pointer;
}




</style>