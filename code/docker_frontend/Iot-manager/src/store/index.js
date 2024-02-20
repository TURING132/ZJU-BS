import {createStore} from "vuex"

export default createStore({
    state:{
        loginState: 0,
        username: "",
        email: "",
        user_id: null
    },
    mutations: {
        changeLogin(state, {loginState, username, email, user_id}){
            Object.assign(state,  {loginState, username, email, user_id})
        }
    }
})