# coding:utf-8

import logging
from .base_handler import BaseHandler


class LoginHandler(BaseHandler):

    def get(self, action):
        if action == "":
            self.signin_page()
        elif action == "weibo":
            self.weibo_signin()
        elif action == "signout":
            self.signout()
        elif action == "register":
            self.register_page()
        else:
            self.write("not found")

    def post(self, action):
        if action == "signin":
            self.signin()
        elif action == "register":
            self.register()
        else:
            self.write("not found")

    def signin_page(self):
        self.render('signin.html')

    def weibo_signin(self):
        url = 'https://api.weibo.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&response_type=code&redirect_uri=YOUR_REGISTERED_REDIRECT_URI'
        self.redirect(url)

        'https://api.weibo.com/oauth2/access_token?client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=authorization_code&redirect_uri=YOUR_REGISTERED_REDIRECT_URI&code=CODE'
    def signout(self):
        self.set_secure_cookie('uid', "")

    def register_page(self):
        self.render('register.html')

    def signin(self):
        pass

    def register(self):
        pass
