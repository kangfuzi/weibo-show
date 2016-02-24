# coding:utf-8

import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    @tornado.web.authenticated
    def get(self):
        self.get_index_page()

    def post(self):
        pass

    def get_current_user(self):
        """override the super class method"""
        app_user_id = self.get_secure_cookie('uId', '')
        if not app_user_id:
            return None
        return app_user_id

    def get_current_ip(self):
        self.request.headers.get('X-Real-IP', self.request.remote_ip)

    def get_index_page(self):
        pass
