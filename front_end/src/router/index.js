import Vue from 'vue';
import Router from 'vue-router';
import Index from '../pages/front-page/Index';
import Archive from '../pages/front-page/Archive';
import AboutMe from '../pages/front-page/AboutMe';
import Categories from '../pages/front-page/Categories';
import Blog from '../pages/front-page/Blog';
import Tabs from '../pages/front-page/Tabs';
import Front from '../pages/Front';
import End from '../pages/End';

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
                    name: 'adminIndex',
                    component: Index,
                },
            ],
        },
    ],
});
