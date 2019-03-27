import { get } from './api.js';

export const index = p => get('api/v1/index', p);
