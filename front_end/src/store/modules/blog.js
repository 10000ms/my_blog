const state = {
    blog: [],
    blogRecommend: [],
};


const getters = {

};


const mutations = {
    commitBlog(state, blog) {
        state.blog = blog;
    },
    commitBlogRecommend(state, blogRecommend) {
        state.blogRecommend = blogRecommend;
    },
};


export default {
    namespaced: true,
    state,
    mutations,
    getters,
};
