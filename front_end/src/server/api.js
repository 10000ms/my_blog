/**axios封装
 * 请求拦截、相应拦截、错误统一处理
 */
import axios from 'axios';

import router from '../router/index';
import store from '../store/index';
import { createWebMessage } from '../utils/webMessage';

import { log } from '../utils/console'

// 请求超时时间
axios.defaults.timeout = 10000;
// post请求头
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8';

// // 请求拦截器
// axios.interceptors.request.use(
//     config => {
//         store.commit('auth/showLoad',true);
//         return config;
//     },
//     error => {
//         return Promise.error(error);
//     }
// );

// 响应拦截器
axios.interceptors.response.use(
    response => {
        log(response);
        switch (response.data.code) {
            // 测试返回信息会不会弹出提示
            case 200:
                store.commit('webMessages/commitMessage',createWebMessage('info', response.data.message));
                break;
            case 400:
                store.commit('webMessages/commitMessage',createWebMessage('error', response.data.message));
                break;
            case 403:
                store.commit('webMessages/commitMessage',createWebMessage('warning', response.data.message));
                router.push({
                    path: '/',
                });
                break;
            case 404:
                store.commit('webMessages/commitMessage',createWebMessage('warning', response.data.message));
                router.push({
                    path: '/',
                });
                break;
            case 500:
                store.commit('webMessages/commitMessage',createWebMessage('error', response.data.message));
                break;
        }
        return Promise.resolve(response);
    },
    error => {
        if (error.response.status) {
            store.commit('webMessages/commitMessage',createWebMessage('error', error.response.status));
            return Promise.reject(error.response);
        }
    }
);

/**
 * get方法，对应get请求
 * @param {String} url [请求的url地址]
 * @param {Object} params [请求时携带的参数]
 */
export function get(url, params){
    return new Promise((resolve, reject) =>{
        axios.get(url, {
            params: params
        })
            .then(res => {
                resolve(res.data);
            })
            .catch(error => {
                store.commit('webMessages/commitMessage',createWebMessage('error', error.response.status));
                reject(error.data)
            })
    });
}

/**
 * post方法，对应post请求
 * @param {String} url [请求的url地址]
 * @param {Object} params [请求时携带的参数]
 */
export function post(url, params) {
    return new Promise((resolve, reject) => {
        axios.post(url, JSON.stringify(params))
            .then(res => {
                resolve(res.data);
            })
            .catch(error => {
                store.commit('webMessages/commitMessage',createWebMessage('error', error.response.status));
                reject(error.data);
            })
    });
}
