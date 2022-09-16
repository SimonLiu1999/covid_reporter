import os

from utils.navigator import Navigator
from utils.user import UserManager
import requests


print('***********************************************')
print('***                                         ***')
print('***      UCAS Cronavirus Report Script      ***')
print('***        Password Login - by ZZJ          ***')
print('***                                         ***')
print('***********************************************')
print()


api_key = "SCT171412TAtEIee0z9VTutsJtRg3WjpXk"  # server酱的api，填了可以微信通知打卡结果，不填没影响
def message(key, title, body):
    """
    微信通知打卡结果
    """
    msg_url = "https://sc.ftqq.com/{}.send?text={}&desp={}".format(key, title, body)
    requests.get(msg_url)

try:
    usermg = UserManager(False)
    user = usermg.get_user()
    nav = Navigator(user)
    print('登录中')
    nav.login()
    print('获取历史打卡记录中')
    old_data = nav.get_history_data()
    print('构造本次打卡记录中')
    new_data = nav.gen_report_data(old_data)
    print('提交打卡记录中')
    resp = nav.do_report(new_data)
    if resp.json()['e']==0:
        print('打卡成功！')
        message(api_key, '打卡成功！', resp)

except Exception as err:
    print(err)
    message(api_key, err, err)

#os.system('pause')
