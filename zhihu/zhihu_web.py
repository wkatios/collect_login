#coding=utf-8
#author: katios
#date: 2017/07/05

import os
import re
import sys
import json
import time
import random
import requests
from bs4 import BeautifulSoup

headers = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

data = {
    'password': "",
    "remember_me": "true",
    'phone_num': "",
    'captcha': ''
}

def login_pre():
    s = requests.session()
    html = s.get(url='https://www.zhihu.com/',headers=headers)
    soup = BeautifulSoup(html.content,'lxml')
    xsrf = soup.input['value']
    return s,xsrf

def login():
    timesteamp = str(int(time.time())*1000)
    s = requests.session()
    html = s.get("https://www.zhihu.com/roundtable",headers=headers)
    print html.status_code
    html =s.get('https://www.zhihu.com/captcha.gif?r=%s&type=login'% timesteamp,headers=headers)
    print html.status_code
    with open('test.gif','wb+') as f:
        f.write(html.content)
        os.startfile('test.gif')
    captcha = raw_input()
    data['captcha']= captcha
    html = s.post('https://www.zhihu.com/login/phone_num',headers=headers,data=data)
    print html.content
    print html.json()['msg']
    return html.cookies

def login_with_cookies():
    headers = {
        'Host': 'www.zhihu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': 'z_c0="QUpBQ3NRdGxCQXdYQUFBQVlRSlZUWEtFaFZsZDdsVWsycVYtcEhPR3R2bHdMWGdsNFBSTVRBPT0=|1499330418|c5d5e4f63c649bd7a935ae223a5fde330c30b03c"',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0', }
    s = requests.session()
    html = s.get('https://www.zhihu.com/', headers=headers)
    print html.content

if __name__ == "__main__":
    # s,xsrf = login_pre()
    # login()
    login_with_cookies()



    #print s.cookies


    #html =s.get('https://www.zhihu.com/question/38001090',headers=headers)
    #print html.status_code
    # html =s.get('https://www.zhihu.com/api/v4/members/wkatios?include=locations%2Cemployments%2Cgender%2Ceducations%2Cbusiness%2Cvoteup_count%2Cthanked_Count%2Cfollower_count%2Cfollowing_count%2Ccover_url%2Cfollowing_topic_count%2Cfollowing_question_count%2Cfollowing_favlists_count%2Cfollowing_columns_count%2Cavatar_hue%2Canswer_count%2Carticles_count%2Cpins_count%2Cquestion_count%2Ccolumns_count%2Ccommercial_question_count%2Cfavorite_count%2Cfavorited_count%2Clogs_count%2Cmarked_answers_count%2Cmarked_answers_text%2Cmessage_thread_token%2Caccount_status%2Cis_active%2Cis_bind_phone%2Cis_force_renamed%2Cis_bind_sina%2Cis_privacy_protected%2Csina_weibo_url%2Csina_weibo_name%2Cshow_sina_weibo%2Cis_blocking%2Cis_blocked%2Cis_following%2Cis_followed%2Cmutual_followees_count%2Cvote_to_count%2Cvote_from_count%2Cthank_to_count%2Cthank_from_count%2Cthanked_count%2Cdescription%2Chosted_live_count%2Cparticipated_live_count%2Callow_message%2Cindustry_category%2Corg_name%2Corg_homepage%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics',headers=headers)
    # print html.json()['error']['message']
    # html =s.get('https://www.zhihu.com/people/wkatios/following/questions',headers=headers)
    # print html.content



