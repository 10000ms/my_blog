const state = {
    blog: [],
    blogRecommend: [],
    indexPage: [],
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
    commitIndexPage(state, indexPage) {
        state.indexPage = indexPage;
    },
};


export default {
    namespaced: true,
    state,
    mutations,
    getters,
};
