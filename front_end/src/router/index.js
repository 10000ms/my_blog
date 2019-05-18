import Vue from 'vue';
import Router from 'vue-router';
import store from '../store/index';

import Index from '../pages/front_page/Index';
import searchMode from '../pages/front_page/searchMode';
import Archive from '../pages/front_page/Archive';
import AboutMe from '../pages/front_page/AboutMe';
import Categories from '../pages/front_page/Categories';
import Blog from '../pages/front_page/Blog';
import Tabs from '../pages/front_page/Tabs';
import Front from '../pages/Front';
import End from '../pages/End';
import EndIndex from '../pages/end_page/EndIndex';
import BlogOperation from '../pages/end_page/BlogOperation';
import ManageBlog from '../pages/end_page/ManageBlog';
import TabOperation from '../pages/end_page/TabOperation';
import ManageTabs from '../pages/end_page/ManageTabs';
import CategoryOperation from '../pages/end_page/CategoryOperation';
import ManageCategories from '../pages/end_page/ManageCategories';
import EndAboutMe from '../pages/end_page/EndAboutMe';
import ManageWebsite from '../pages/end_page/ManageWebsite';

Vue.use(Router);


export const router = new Router({
    routes: [
        {
            path: '/',
            component: Front,
            children: [
                {
                    path: '',
                    name: 'index',
                    component: Index,
                },
                {
                    path: 'search/:mode/:query',
                    name: 'searchMode',
                    component: searchMode,
                },
                {
                    path: 'archive',
                    name: 'archive',
                    component: Archive,
                },
                {
                    path: 'about-me',
                    name: 'aboutMe',
                    component: AboutMe,
                },
                {
                    path: 'categories',
                    name: 'categories',
                    component: Categories,
                },
                {
                    path: 'tabs',
                    name: 'tabs',
                    component: Tabs,
                },
                {
                    path: 'blog/:id',
                    name: 'blog',
                    component: Blog,
                },
            ],
        },
        {
            path: '/admin',
            component: End,
            children: [
                {
                    path: '',
                    name: 'endIndex',
                    component: EndIndex,
                },
                {
                    path: 'create-blog',
                    name: 'create-blog',
                    component: BlogOperation,
                },
                {
                    path: 'change-blog/:mode',
                    name: 'change-blog',
                    component: BlogOperation,
                },
                {
                    path: 'manage-blog',
                    name: 'manage-blog',
                    component: ManageBlog,
                },
                {
                    path: 'create-tab',
                    name: 'create-tab',
                    component: TabOperation,
                },
                {
                    path: 'change-tab/:mode',
                    name: 'change-tab',
                    component: TabOperation,
                },
                {
                    path: 'manage-tabs',
                    name: 'manage-tabs',
                    component: ManageTabs,
                },
                {
                    path: 'create-category',
                    name: 'create-category',
                    component: CategoryOperation,
                },
                {
                    path: 'change-category/:mode',
                    name: 'change-category',
                    component: CategoryOperation,
                },
                {
                    path: 'manage-categories',
                    name: 'manage-categories',
                    component: ManageCategories,
                },
                {
                    path: 'end-about-me',
                    name: 'end-about-me',
                    component: EndAboutMe,
                },
                {
                    path: 'manage-website',
                    name: 'manage-website',
                    component: ManageWebsite,
                },
            ],
        },
    ],
});


/**
 * 未登录和不是管理员不允许进入后台管理界面
 */
router.beforeEach((to, from, next) => {
    let isLogin = store.state.auth.id;
    let isSuperuser = store.state.auth.isSuperuser;
    let isDemo = Boolean(store.state.website.demoModel && store.state.auth.isDemo);
    const regex = '^/admin.*$';
    if (! ((isLogin && isSuperuser) || isDemo)) {
        if (to.path.search(regex) !== -1) {
            next({path: '/'});
        }else {
            next();
        }
    }else {
        next();
    }
});
