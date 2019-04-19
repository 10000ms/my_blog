const state = {
    aboutMe: '',
    websiteName: '',
    ICPNumber: '',
    websiteImage: '',
    ad1: '',
    ad1URL: '',
    ad2: '',
    ad2URL: '',
    github: '',
    email: '',
    friendshipLink: '',
    openRegister: false,
    demoModel: false,
};


const getters = {
    getFriendshipLink(state) {
        return state.friendshipLink.split(';');
    },
};


const mutations = {
    commitInit(state, website_manage) {
        state.aboutMe = website_manage['about_me'];
        state.websiteName = website_manage['website_name'];
        state.ICPNumber = website_manage['ICP_number'];
        state.websiteImage = website_manage['website_image'];
        state.ad1 = website_manage['ad_1'];
        state.ad1URL = website_manage['ad_1_url'];
        state.ad2 = website_manage['ad_2'];
        state.ad2URL = website_manage['ad_2_url'];
        state.github = website_manage['github'];
        state.email = website_manage['email'];
        state.friendshipLink = website_manage['friendship_link'];
        state.openRegister = website_manage['open_register'];
        state.demoModel = website_manage['demo_model'];
    },
};


export default {
    namespaced: true,
    state,
    mutations,
    getters,
};
