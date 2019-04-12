import { get } from './api.js';

export default {
    index: p => get('api/init_index', p),
}
