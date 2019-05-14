const state = {
    day: {
        seven_day: [
            {
                'date': '',
                'read_count': 0,
                'like_count': 0,
                'comment_count': 0,
            },
            {
                'date': '',
                'read_count': 0,
                'like_count': 0,
                'comment_count': 0,
            },
            {
                'date': '',
                'read_count': 0,
                'like_count': 0,
                'comment_count': 0,
            },
            {
                'date': '',
                'read_count': 0,
                'like_count': 0,
                'comment_count': 0,
            },
            {
                'date': '',
                'read_count': 0,
                'like_count': 0,
                'comment_count': 0,
            },
            {
                'date': '',
                'read_count': 0,
                'like_count': 0,
                'comment_count': 0,
            },
            {
                'date': '',
                'read_count': 0,
                'like_count': 0,
                'comment_count': 0,
            },
            ],
        total: {
            'read_count': 0,
            'like_count': 0,
            'comment_count': 0,
        },
    },
    region: [],
};


const getters = {

};


const mutations = {
    commitInit(state, count) {
        state.day = count['day'];
        state.region = count['region'];
    },
};


export default {
    namespaced: true,
    state,
    mutations,
    getters,
};
