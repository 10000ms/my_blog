import { get, post, put, deleteAjax } from './api.js';

export default {
    index: p => get('api/init-index/', p),
    changeUserData: (id, p) => put(`api/user/${id}/`, p),
    blog: id => get(`api/blog/${id}/`, null),
    blogs: (p=null) => get('api/blog/', p),
    heart: p => post('api/blog/heart/', p),
    blogComment: p => get('api/comment/blog/', p),
    createComment: p => post(`api/comment/`, p),
    changeComment: (id, p) => put(`api/comment/${id}/`, p),
    deleteComment: id => deleteAjax(`api/comment/${id}/`, null),
    login: p => post('api/user/login/', p),
    register: p => post('api/user/register/', p),
    logout: () => post('api/user/logout/', null),
    tab: (id=null) => {
        let url;
        if (id) {
            url = `api/tab/${id}/`
        } else {
            url = 'api/tab/'
        }
        return  get(url, null);
    },
    tabQuery: p => get('api/tab/query/', p),
    category: (id=null) => {
        let url;
        if (id) {
            url = `api/category/${id}/`
        } else {
            url = 'api/category/'
        }
        return  get(url, null);
    },
    categoryQuery: p => get('api/category/query/', p),
    aboutMe: () => get('api/about-me/', null),

    createBlog: p => post(`api/blog/`, p),
    changeBlog: (id, p) => put(`api/blog/${id}/`, p),
    deleteBlog: id => deleteAjax(`api/blog/${id}/`, null),
    addRecommend: p => post('api/blog/add-recommend/', p),
    cancelRecommend: p => post('api/blog/cancel-recommend/', p),
    createTab: p => post(`api/tab/`, p),
    changeTab: (id, p) => put(`api/tab/${id}/`, p),
    deleteTab: id => deleteAjax(`api/tab/${id}/`, null),
    createCategory: p => post(`api/category/`, p),
    changeCategory: (id, p) => put(`api/category/${id}/`, p),
    deleteCategory: id => deleteAjax(`api/category/${id}/`, null),
    changeAboutMe: (id, p) => put(`api/about-me/${id}/`, p),
    websiteManage: () => get('api/website-manage/', null),
    changeWebsiteManage: (id, p) => put(`api/website-manage/${id}/`, p),
}
