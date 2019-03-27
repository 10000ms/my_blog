export const createWebMessage = (messageType, message) => {
    return {
        state: messageType,
        message: message,
    };
};
