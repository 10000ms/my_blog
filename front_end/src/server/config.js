/**axios封装
 * 请求拦截、相应拦截、错误统一处理
 */
import axios from 'axios';
import router from '../router/index';

import { log } from '../utils/console';

// 代码对应的默认信息
const codeMsg = {
    400: '错误请求',
    403: '没有对应请求权限',
    404: '未找到对应请求资源',
    500: '服务器内部错误',
};

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
            // 开发环境行对返回进行debug输出
            if (process.env.NODE_ENV === "development") {
                log('in development response', response);
            }
            let m = getMsg(response);
            switch (response.data.code) {
                case 400:
                    message.error(m);
                    break;
                case 403:
                    message.warning(m);
                    router.push({
                        path: '/',
                    });
                    break;
                case 404:
                    message.warning(m);
                    router.push({
                        path: '/',
                    });
                    break;
                case 500:
                    message.error(m);
                    break;
            }
            return Promise.resolve(response);
        },
        error => {
            if (error.response.status) {
                // 开发环境行对返回进行debug输出
                if (process.env.NODE_ENV === "development") {
                    log('in development error response', error.response);
                }
                let s = error.response.status;
                if ('data' in error.response) {
                    // 清除错误信息，前端不显示
                    error.response.data = ''
                }
                if (s === 404) {
                    message.error('资源未找到');
                    return Promise.reject(error.response);
                } else if (s === 500) {
                    message.error('服务器内部错误');
                    return Promise.reject(error.response);
                } else {
                    message.error(error.response.status.toString());
                    return Promise.reject(error.response);
                }
            }
        }
    );
};
