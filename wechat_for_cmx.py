"""
__project_ = 'this_is_for_cmx'
__file_name__ = 'wechat_for_cmx'
__author__ = 'lufangfan'
__time__ = '2020/4/4 16:46'
__product_name = PyCharm
# code is far away from bugs with the god animal protecting,I love animals. They taste delicious.
                                            ┏┓      ┏┓
                                    ┏┛┻━━━┛┻┓
                                    ┃        ┃
                                    ┃  ┳┛  ┗┳  ┃
                                    ┃      ┻      ┃
                                    ┗━┓      ┏━┛
                                        ┃      ┗━━━┓
                                        ┃  神兽保佑    ┣┓
                                        ┃　永无BUG！   ┏┛
                                        ┗┓┓┏━┳┓┏┛
                                          ┃┫┫  ┃┫┫
                                          ┗┻┛  ┗┻┛
"""
import threading

import itchat
import requests
import time
import datetime
from itchat.content import *

lunar_calendar_birthday = '1998-07-17'
the_gregorian_calendar_birthday = '1998-09-07'
nick_name = 'FFD'  # 微信昵称
fall_in_love_time = '2020-2-7 02:00:00'
first_time_i_saw_you = '2020-3-21 10:30:00'
morning_time = '08:00:00'
ten_o_clock = '10:00:00'
lunch_time = '12:00:00'
fifteen_o_clock = '15:00:00'
dinner_time = '18:00:00'
night_time = '22:00:00'


def get_king_soft_power_word():
    # 获取金山词霸每日一句，英文和翻译
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    return r.json()['content'], r.json()['note']


def time_stamp_of_given(given_time):
    return time.time() - time.mktime(time.strptime(given_time, "%Y-%m-%d %H:%M:%S"))


def trans_str_time_to_datetime(str_time):
    return datetime.datetime.strptime(str(datetime.date.today()) + ' ' + str_time, '%Y-%m-%d %H:%M:%S')


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    if msg.user['NickName'] == nick_name:
        print('收到来自{}的消息'.format(nick_name))
    # msg.user.send('%s: %s' % (msg.type, msg.text))


def send_messages_regularly():
    print('定时发送微信开启')
    search_friends_res = itchat.search_friends(name=nick_name)
    if search_friends_res:
        user_name = search_friends_res[0]['UserName']
        tmp_time = '23:25:00'
        while True:
            if trans_str_time_to_datetime(morning_time) <= datetime.datetime.now() <= trans_str_time_to_datetime(
                    morning_time) + datetime.timedelta(minutes=10):
                content, note = get_king_soft_power_word()
                msg = '我的小可爱，现在是{}，从你做我女朋友到现在已经过了{}秒，每一秒我都在想着你！你要记得吃早饭，还要记得喝一杯水。希望你今天开开心心。送给你一句话，希望你喜欢。{}{}'.format(
                    datetime.datetime.now().strftime('%Y{y}%m{m}%d{d}%H{h}%M{f}%S{s}').format(y='年', m='月', d='日',
                                                                                              h='时', f='分',
                                                                                              s='秒'),
                    time_stamp_of_given(fall_in_love_time), content, note)
                itchat.send(msg, toUserName=user_name)
                time.sleep(10)
                itchat.send('记得早上起来一定要喝一杯水啊！！！我的小可爱，一定要听话哦', toUserName=user_name)
                time.sleep(10)
                itchat.send('宝贝，早餐一定要吃啊，一定要吃啊啊啊啊啊啊', toUserName=user_name)
                time.sleep(1800)
            if trans_str_time_to_datetime(ten_o_clock) <= datetime.datetime.now() <= trans_str_time_to_datetime(
                    ten_o_clock) + datetime.timedelta(minutes=10):
                msg = '现在是上午10点钟，你要记得喝杯水了啊。'
                itchat.send(msg, toUserName=user_name)
                time.sleep(10)
                itchat.send('小宝贝，喝水了没？', toUserName=user_name)
                time.sleep(40)
                itchat.send('嘿嘿，多喝水哦', toUserName=user_name)
                time.sleep(1800)
            if trans_str_time_to_datetime(lunch_time) <= datetime.datetime.now() <= trans_str_time_to_datetime(
                    lunch_time) + datetime.timedelta(minutes=10):
                msg = '现在是中午12点钟了，你要按时吃午饭，就算肚子不饿，也要吃一点点垫垫肚子。听话呀，我的小可爱'
                itchat.send(msg, toUserName=user_name)
                time.sleep(10)
                itchat.send('还要记得喝杯水...', toUserName=user_name)
                time.sleep(50)
                itchat.send('小可爱，你喝水了没有啊', toUserName=user_name)
                time.sleep(1800)
            if trans_str_time_to_datetime(fifteen_o_clock) <= datetime.datetime.now() <= trans_str_time_to_datetime(
                    fifteen_o_clock) + datetime.timedelta(minutes=10):
                msg = '现在是下午3点钟了，你又有好几个小时没有喝水了，记得要喝水啊'
                itchat.send(msg, toUserName=user_name)
                time.sleep(10)
                itchat.send('爱你，宝贝', toUserName=user_name)
                time.sleep(50)
                itchat.send('老婆，你喝水了没有啊', toUserName=user_name)
                time.sleep(1800)
            if trans_str_time_to_datetime(dinner_time) <= datetime.datetime.now() <= trans_str_time_to_datetime(
                    dinner_time) + datetime.timedelta(minutes=10):
                msg = '现在是下午6点钟了，到了吃晚饭的时间了，要按时吃晚饭，我的小可爱要按时吃饭呀，不饿也要吃，听话听话'
                itchat.send(msg, toUserName=user_name)
                time.sleep(20)
                itchat.send('也别忘记喝水呀，爱你，宝贝', toUserName=user_name)
                time.sleep(1800)
            if trans_str_time_to_datetime(night_time) <= datetime.datetime.now() <= trans_str_time_to_datetime(
                    night_time) + datetime.timedelta(minutes=10):
                msg = '又到了晚上10点钟了，我的小可爱，今天过的开心吗？你知道吗，从我们第一次见面，到此刻，已经过去了{}秒，我好想在你睡前抱抱你，在你耳边说声晚安啊！'.format(
                    time_stamp_of_given(first_time_i_saw_you))
                itchat.send(msg, toUserName=user_name)
                time.sleep(10)
                itchat.send('爱你，宝贝，晚安，早点睡哦...', toUserName=user_name)
                time.sleep(1800)

    else:
        print('未找到指定用户')


def auto_reply_message():
    print('开始自动回复消息')
    itchat.run(True)


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    print('登录成功！！！')
    # print(cur_time)

    t1 = threading.Thread(target=send_messages_regularly)
    t2 = threading.Thread(target=auto_reply_message)
    t1.start()
    t2.start()

    # print(trans_str_time_to_datetime(morning_time))
