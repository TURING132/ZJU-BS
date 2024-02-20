<template>
    <template v-if="mobileFlag===0">
        <div class="register-card">
            <input type="text" id="username" v-model="username" placeholder="用户名" required>
            <input type="email" id="email" v-model="email" placeholder = "邮箱" required>
            <input type="password" id="password" v-model="password" placeholder = "密码" required>
            <input type="password" id="ensurePassword" v-model="ensurePassword" placeholder = "确认密码" required>
            <button class="login-botton" @click="register">注册</button>
        </div>
    </template>
    <template v-else>
        <div class="MOregister-card">
            <input type="text" id="username" v-model="username" placeholder="用户名" required>
            <input type="email" id="email" v-model="email" placeholder = "邮箱" required>
            <input type="password" id="password" v-model="password" placeholder = "密码" required>
            <input type="password" id="ensurePassword" v-model="ensurePassword" placeholder = "确认密码" required>
            <button class="login-botton" @click="register">注册</button>
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
            password: "",
            ensurePassword:"",
            username: "",
        }
    },
    methods:{
    async register(){
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(this.email)) {
            alert("邮箱格式错误");
        }
        // 密码和确认密码是否相同
        if (this.password !== this.ensurePassword) {
            alert("注册失败！密码和确认密码不匹配");
            return;
        }
        // 密码长度是否符合要求（至少8个字符），包含字母和数字
        const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
        if (!passwordRegex.test(this.password)) {
            alert("注册失败！密码长度至少为8位，且必须包含字母和数字");
            return;
        }
        
        const requestData = {
            username: this.username,
            password: md5(this.password),
            email: this.email,
        };
        try {
            const response = await fetch('http://127.0.0.1:8000/user/register', {
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
                    alert('注册成功')
                    this.$router.push('/');
                } else {
                    alert(`注册失败: ${jsonResponse.message}`);
                }
            } else {
                alert(`网络错误: ${response.message}`);
            }
        } catch (error) {
            // 处理网络请求失败的逻辑
            alert('网络错误');
        }
        }
    }
}
</script>
  
<style>
.register-card{
    width: 400px;
    height: 350px;
    padding: 15px,0;
    border-radius: 17px;

    background-color: rgba(217,217,217, 0.3);
    backdrop-filter: blur(5px);

    display: flex;
    flex-direction: column;
    align-items:center;
    justify-content: center;
}

.register-card input[type="email"],
.register-card input[type="password"],
.register-card input[type="text"],
button {
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

.register-card input[type="email"],
.register-card input[type="password"],
.register-card input[type="text"]{
    color: #144E2E;
}
.register-card button{
    color: rgba(255,255,255,0.7);
}

.register-card input[type="email"]:hover,
.register-card input[type="password"]:hover,
.register-card input[type="text"]:hover{
    background-color: rgba(255,255,255,0.7); 
}
.register-card input[type="email"]:hover::placeholder,
.register-card input[type="password"]:hover::placeholder{
    color: #144E2E;
}
.register-card button:hover {
    background-color: rgba(255,255,255,0.7); 
    color: #144E2E;
}
.register-card input[type="email"]::placeholder,
.register-card input[type="password"]::placeholder,
.register-card input[type="text"]::placeholder {
    color: rgba(255,255,255,0.7); /* placeholder颜色 */
    font-size: 16px; /* placeholder字体大小 */
    font-weight: bold;
}
.register-card p{
    color: #fff;
    margin-top: 10px;
    font-size: 13px;
    cursor: pointer;
}
/* ------------------------ */
.MOregister-card{
    width: 90vw;
    height: 350px;
    padding: 15px,0;
    border-radius: 17px;

    background-color: rgba(217,217,217, 0.3);
    backdrop-filter: blur(5px);

    display: flex;
    flex-direction: column;
    align-items:center;
    justify-content: center;
}

.MOregister-card input[type="email"],
.MOregister-card input[type="password"],
.MOregister-card input[type="text"],
.MOregister-card button {
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

.MOregister-card input[type="email"],
.MOregister-card input[type="password"],
.MOregister-card input[type="text"]{
    color: #144E2E;
}
.MOregister-card button{
    color: rgba(255,255,255,0.7);
}

.MOregister-card input[type="email"]:hover,
.MOregister-card input[type="password"]:hover,
.MOregister-card input[type="text"]:hover{
    background-color: rgba(255,255,255,0.7); 
}
.MOregister-card input[type="email"]:hover::placeholder,
.MOregister-card input[type="password"]:hover::placeholder{
    color: #144E2E;
}

.MOregister-card button:hover {
    background-color: rgba(255,255,255,0.7); 
    color: #144E2E;
}

.MOregister-card input[type="email"]::placeholder,
.MOregister-card input[type="password"]::placeholder,
.MOregister-card input[type="text"]::placeholder {
    color: rgba(255,255,255,0.7); /* placeholder颜色 */
    font-size: 16px; /* placeholder字体大小 */
    font-weight: bold;
}
.MOregister-card p{
    color: #fff;
    margin-top: 10px;
    font-size: 13px;
    cursor: pointer;
}
</style>