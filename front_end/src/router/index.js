import Vue from 'vue';
import Router from 'vue-router';
import Index from '../pages/front_page/Index';
import Archive from '../pages/front_page/Archive';
import AboutMe from '../pages/front_page/AboutMe';
import Categories from '../pages/front_page/Categories';
import Blog from '../pages/front_page/Blog';
import Tabs from '../pages/front_page/Tabs';
import Front from '../pages/Front';
import End from '../pages/End';
import EndIndex from '../pages/end_page/EndIndex'
import CreateBlog from '../pages/end_page/CreateBlog'
import ManageBlog from '../pages/end_page/ManageBlog'
import CreateTabs from '../pages/end_page/CreateTabs'
import ManageTabs from '../pages/end_page/ManageTabs'
import CreateCategories from '../pages/end_page/CreateCategories'
import ManageCategories from '../pages/end_page/ManageCategories'
import EndAboutMe from '../pages/end_page/EndAboutMe'
import ManageWebsite from '../pages/end_page/ManageWebsite'

Vue.use(Router);


export default new Router({
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
                    path: ':year/:month/:day/:id',
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
                    component: CreateBlog,
                },
                {
                    path: 'manage-blog',
                    name: 'manage-blog',
                    component: ManageBlog,
                },
                {
                    path: 'create-tabs',
                    name: 'create-tabs',
                    component: CreateTabs,
                },
                {
                    path: 'manage-tabs',
                    name: 'manage-tabs',
                    component: ManageTabs,
                },
                {
                    path: 'create-categories',
                    name: 'create-categories',
                    component: CreateCategories,
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
