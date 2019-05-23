# -*- coding: utf-8 -*-
from django.conf import settings

from elasticsearch import Elasticsearch, Transport


class ESControl(Elasticsearch):
    """
    针对es7.x的控制器封装
    """

    def __init__(self, hosts=settings.ELASTICSEARCH_HOST, transport_class=Transport, **kwargs):
        super().__init__(hosts, transport_class, **kwargs)

    def index(self, index, body, doc_type='_doc', doc_id=None, params=None):
        return super().index(index, body, id=doc_id, params=params)

    def create(self, index, doc_id, body, doc_type='_doc', params=None):
        return super().create(index, body, id=doc_id, params=params)

    def delete(self, index, doc_id, doc_type='_doc', params=None):
        super().delete(index, id=doc_id, params=None)

    def update(self, index, doc_id, doc_type='_doc', body=None, params=None):
        super().update(index, id=doc_id, body=None, params=None)

    def auto_id_search(self, index, content):
        body = {
            'query': {
                'multi_match': {
                    'query': content,
                    'fields': ['*'],
                },
            },
            'size': 1000,
            'stored_fields': ['_id'],
        }
        raw_res = super().search(index, body=body)
        return [hit['_id'] for hit in raw_res['hits']['hits']]

    @staticmethod
    def _add_analyzer_to_field_dict(field_dict, analyzer='ik_max_word', search_analyzer='ik_smart'):
        """
        默认使用ik 7.x的分词设置
        """
        r = {}
        for d in field_dict:
            temp_dict = {
                d: {
                    'type': field_dict[d],
                    'analyzer': analyzer,
                    'search_analyzer': search_analyzer,
                },
            }
            r.update(temp_dict)
        return r

    def create_index(self, index_name, field_dict):
        """
        创建一个index
        :param index_name:
        :param field_dict: 指明每个field对应类型的dict即可，例如：{'foo': 'keyword'}
        :type field_dict: dict
        :return:
        """
        body = {
            'mappings': self._add_analyzer_to_field_dict(field_dict),
        }
        self.index(index_name, body)


def start_task():
    """
    启动django时候的任务，自动检测

    现阶段只包含自动创建index
    """
    es = ESControl()
    check = {
        'blog': {
            'title': 'text',
            'author': 'text',
            'create_time': 'date',
            'last_change_time': 'date',
            'brief': 'text',
            'content': 'text',
        },
    }
    for c in check:
        if es.indices.exists(index=c):
            es.create_index(c, check[c])
