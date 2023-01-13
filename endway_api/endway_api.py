# -*- coding: utf-8 -*-
import requests

from bs4 import BeautifulSoup


class EndWayApi:
    def __init__(self, xf_user: str) -> None:
        self.session = requests.session()
        self.cookies = {"xf_user": xf_user}
        self.xfToken = self.get_token()

    def get_token(self) -> str:
        """
        Getting a csrf token for later use in requests

        :return: csrf token
        :rtype: str
        """
        response = self.session.get("https://endway.su/", cookies=self.cookies)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        csrf = soup.find("html").get("data-csrf")
        return csrf

    def post_thread(self, section_id: int, title: str, message: str) -> object:
        """
        Creating a post

        :param section_id: The number of the partition in which the thread will be created
        :type section_id: int

        :param title: Topic title
        :type title: str

        :param message: Message
        :type message: str

        :return: Response from the server
        :rtype: object
        """
        data = {
            "_xfToken": self.xfToken,
            "title": title,
            "message_html": message,
            "_xfResponseType": "json"
        }
        response = self.session.post(f"https://endway.su/forums/{section_id}/post-thread", cookies=self.cookies,
                                     data=data)
        return response

    def add_reply(self, thread_id: int, message: str) -> object:
        """
        Sending a message to a thread

        :param thread_id: The thread number to which the message will be sent
        :type thread_id: int

        :param message: Message
        :type message: str

        :return: Response from the server
        :rtype: object
        """
        data = {
            "_xfToken": self.xfToken,
            "message_html": message,
            "_xfResponseType": "json"
        }
        response = self.session.post(f"https://endway.su/threads/{thread_id}/add-reply", cookies=self.cookies,
                                     data=data)
        return response

    def member_post(self, member_id: int or str, message: str) -> object:
        """
        Creating a post on a user's page

        :param member_id: Either a permanent user id or a short link. If permanent id, then type int, if short link,
        then type string
        :type member_id: int or str

        :param message: Message
        :type message: str

        :return: Response from the server
        :rtype: object
        """
        if type(member_id) is int:
            url = f"https://endway.su/members/{member_id}/post"
        else:
            url = f"https://endway.su/{member_id}/post"

        data = {
            "_xfToken": self.xfToken,
            "message_html": message,
            "_xfResponseType": "json"
        }
        response = self.session.post(url, cookies=self.cookies, data=data)
        return response

    def add_comment(self, post_id: int, message: str) -> object:
        """
        Creating a comment under a post on a user's page

        :param post_id: The number of the message on the user's page
        (I do not know how to get it without using DevTools)
        :type post_id: int

        :param message: Message
        :type message: str

        :return: Response from the server
        :rtype: object
        """
        data = {
            "_xfToken": self.xfToken,
            "message_html": message,
            "_xfResponseType": "json"
        }
        response = self.session.post(f"https://endway.su/profile-posts/{post_id}/add-comment", cookies=self.cookies,
                                     data=data)
        return response

    # Changing Account Information
    def account_details(self, short_link: str = None, location: str = None, website: str = None,
                        profilebackground: str = None, about_html: str = None, telegram: str = None, vk: str = None,
                        steam: str = None, discord: str = None, github: str = None) -> object:
        """
        Creating a comment under a post on a user's page

        :param short_link: Short link to the page
        :type short_link: str

        :param location: Place of residence
        :type location: str

        :param website: Link to your website
        :type website: str

        :param profilebackground: Link to the desired background of the page
        :type profilebackground: str

        :param about_html: A brief biography about yourself
        :type about_html: str

        :param telegram: Username without @
        :type telegram: str

        :param vk: Link to VK
        :type vk: str

        :param steam: Link to Steam
        :type steam: str

        :param discord: Link to Discord
        :type discord: str

        :param github: Link to GitHub
        :type github: str

        :return: Response from the server
        :rtype: object
        """
        data = {
            "_xfToken": self.xfToken,
            "_xfResponseType": "json"
        }
        if short_link is not None:
            data["short_link"] = short_link
        if location is not None:
            data["profile[location]"] = location
        if website is not None:
            data["profile[website]"] = website
        if profilebackground is not None:
            data["custom_fields[profilebackground]"] = profilebackground
        if about_html is not None:
            data["about_html"] = about_html
        if telegram is not None:
            data["custom_fields[telegram]"] = telegram
        if vk is not None:
            data["custom_fields[vk]"] = vk
        if steam is not None:
            data["custom_fields[Steam]"] = steam
        if discord is not None:
            data["custom_fields[discord]"] = discord
        if github is not None:
            data["custom_fields[github]"] = github
        response = self.session.post(f"https://endway.su/account/account-details", cookies=self.cookies,
                                     data=data)
        return response

    def security(self, old_password: str, new_password: str) -> object:
        """
        Changing the account password

        :param old_password: Old account password
        :type old_password: str

        :param new_password: New password for the account
        :type new_password: str

        :return: Response from the server
        :rtype: object
        """

        data = {
            "_xfToken": self.xfToken,
            "old_password": old_password,
            "password": new_password,
            "password_confirm": new_password,
            "_xfResponseType": "json"
        }
        response = self.session.post(f"https://endway.su/account/security", cookies=self.cookies,
                                     data=data)
        return response

    def signature(self, signature_html: str) -> object:
        """
        Changing the signature

        :param signature_html: New signature
        :type signature_html: str

        :return: Response from the server
        :rtype: object
        """
        data = {
            "_xfToken": self.xfToken,
            "signature_html": signature_html,
            "_xfResponseType": "json"
        }
        response = self.session.post(f"https://endway.su/account/security", cookies=self.cookies,
                                     data=data)
        return response
