const state = {
    message: []
};

const getters = {
    getMessages(state){
        return state.message;
    },
};

const mutations = {
    commitMessage(state, message) {
        state.message.push(message)
    },
    renewMessage(state) {
        // 发送后，移除第一条信息
        state.message.shift()
    }
};

export default {
    namespaced: true,
    state,
    mutations,
    getters,
};
