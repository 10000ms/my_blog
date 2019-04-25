import { get } from './api.js';

export default {
    index: p => get('api/init_index', p),
    blog: p => get('api/blog/' + p + '/', {}),
    blogs: p => get('api/blog/', p),
}
