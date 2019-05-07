import { get, post } from './api.js';

export default {
    index: p => get('api/init-index/', p),
    blog: p => get('api/blog/' + p + '/', null),
    blogs: p => get('api/blog/', p),
    login: p => post('api/users/login/', p),
    register: p => post('api/users/register/', p),
    logout: () => post('api/users/logout/', null),
    tab: () => get('api/tab/', null),
    tabQuery: p => get('api/tab/query/', p),
    category: () => get('api/category/', null),
    categoryQuery: p => get('api/category/query/', p),
    aboutMe: () => get('api/about-me/', null),
}
