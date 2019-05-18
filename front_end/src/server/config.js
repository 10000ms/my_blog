/**axios封装
 * 请求拦截、相应拦截、错误统一处理
 */
import axios from 'axios';
import { router } from '../router/index';

import {log} from '../utils/console';
import cookie from '../utils/cookie';

// 代码对应的默认信息
const codeMsg = {
    400: '错误请求',
    403: '没有对应请求权限',
    404: '未找到对应请求资源',
    500: '服务器内部错误',
};

// 需要使用到csrf token的方法
const needCsrfTokenMethod = [
    'post',
    'put',
    'patch',
    'delete',
];

const getMsg = function(response) {
    let m = '';
    if ('data' in response && 'code' in response.data && 'msg' in response.data) {
        if (response.data.msg) {
            m = response.data.msg;
        } else {
            m = codeMsg[response.data.code];
        }
    } else {
        log('请求返回缺乏关键信息', response);
    }
    return m;

};

export const axiosConfig = function(message) {
    // 请求超时时间
    axios.defaults.timeout = 10000;
    // 请求头
    axios.defaults.headers.post['Content-Type'] = 'application/json';
    axios.defaults.headers.put['Content-Type'] = 'application/json';

    // // 请求拦截器, 添加头部X-CSRFTOKEN
    axios.interceptors.request.use(
        config => {
            if (needCsrfTokenMethod.indexOf(config.method) !== -1) {
                config.headers['X-CSRFTOKEN'] = cookie.getCookie('csrftoken');
            }
            return config;
        },
        error => {
            return Promise.error(error);
        }
    );

    // 响应拦截器
    axios.interceptors.response.use(
        response => {
            // 开发环境行对返回进行debug输出
            if (process.env.NODE_ENV === 'development') {
                log('in development response', response);
            }
            if (response.status < 200 || response.status > 299) {
                let m = getMsg(response);
                switch (response.data.code) {
                    case 400:
                        message.error(m);
                        return Promise.reject(response);
                    case 403:
                        message.warning(m);
                        router.push({
                            path: '/',
                        });
                        return Promise.reject(response);
                    case 404:
                        message.warning(m);
                        router.push({
                            path: '/',
                        });
                        return Promise.reject(response);
                    case 500:
                        message.error(m);
                        return ;
                }
            }
            return Promise.resolve(response);
        },
        error => {
            // 开发环境行对返回进行debug输出
            if (process.env.NODE_ENV === 'development') {
                log('in development error response', error.response);
            }
            if (error.response.status < 200 || error.response.status > 299) {
                switch (error.response.data.code) {
                    case 403:
                        message.warning(codeMsg[error.response.data.code]);
                        return ;
                    case 404:
                        message.warning(codeMsg[error.response.data.code]);
                        return ;
                    case 500:
                        message.error(codeMsg[error.response.data.code]);
                        return ;
                }
            }
            return Promise.reject(error.response);
        },
    );
};
