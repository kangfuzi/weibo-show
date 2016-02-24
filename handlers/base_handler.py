# coding:utf-8

import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    def prepare(self):
        self.title = None

    @tornado.web.authenticated
    def get(self, action):
        self.get_index_page()

    def post(self, action):
        pass

    def get_current_user(self):
        """override the super class method"""
        app_user_id = self.get_secure_cookie('uid', '')
        if not app_user_id:
            return None
        return app_user_id

    def render(self, template_name, **kwargs):

        return super(BaseHandler, self).render(template_name, title=self.title, **kwargs)

    def get_current_ip(self):
        self.request.headers.get('X-Real-IP', self.request.remote_ip)

    def get_index_page(self):
        user_tags = None
        self.title = u'微博链接测试'
        self.render("index.html", user_tags=user_tags)
