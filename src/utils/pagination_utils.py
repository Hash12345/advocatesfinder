from rest_framework import pagination

class CustomPagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        result = {
            'previous': self.get_previous_link(),
            'next': self.get_next_link(),
            'count': self.count,
            'result': data
        }
        return result