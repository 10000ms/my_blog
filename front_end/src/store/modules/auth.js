const state = {
    id: 0,
    email: '',
    profile: '',
    firstName: '',
    lastName: '',
    phone: '',
    username: '',
    isAuthor: '',
    isSuperuser: '',
    isDemo: false,
};


const getters = {
    getFullName(state) {
        return state.lastName + state.firstName;
    },

};


const mutations = {
    commitInit(state, user) {
        state.id = user['id'];
        state.profile = user['profile'];
        state.email = user['email'];
        state.firstName = user['first_name'];
        state.lastName = user['last_name'];
        state.phone = user['phone'];
        state.username = user['username'];
        state.isAuthor = user['is_author'];
        state.isSuperuser = user['is_superuser'];
        state.isDemo = user['is_demo_user'];
    },
};


export default {
    namespaced: true,
    state,
    mutations,
    getters,
};
