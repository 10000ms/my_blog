from rest_framework.renderers import JSONRenderer

from utils.api_common import create_response


class CustomJSONRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        # 已经有对应格式的返回不进行改写
        if data and 'code' in data and 'msg' in data:
            response_data = data
        else:
            response_data = create_response(data=data)
        response = super().render(response_data, accepted_media_type, renderer_context)
        return response
