import { scrollTop } from 'iview/src/utils/assist';

export default {
    toTop() {
        const sTop = document.documentElement.scrollTop || document.body.scrollTop;
        scrollTop(window, sTop, 0)
    }
}
