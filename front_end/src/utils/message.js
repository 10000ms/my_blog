import { log } from './console';

export default {
    /**
     * 处理返回信息方法
     * 对象和数组都可以拆开来发出
     */
    dealReturnMessage(message, thisObject, sender) {
        if (message instanceof Object) {
            // 处理object对象的消息
            let messageKey = Object.keys(message);
            for (let i = 0; i < messageKey.length; i++) {
                this.dealReturnMessage(message[messageKey[i]], thisObject,sender);
            }
        } else if (message instanceof Array) {
            // 处理array对象的消息
            for (let i = 0; i < message.length; i++) {
                this.dealReturnMessage(message[i], thisObject, sender);
            }
        } else {
            // 其他对象直接发送
            log(`Message ${sender}: ${message}`);
            thisObject.$Message[sender](message)
        }
    }
}
