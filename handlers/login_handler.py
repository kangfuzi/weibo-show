# coding:utf-8

import logging
from .base_handler import BaseHandler


class LoginHandler(BaseHandler):

    def get(self, action):
        if action == "":
            self.signin_page()
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

    def signout(self):
        self.set_secure_cookie('uid', "")

    def register_page(self):
        self.render('register.html')

    def signin(self):
        pass

    def register(self):
        pass
