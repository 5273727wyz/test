from rest_framework.response import  Response
from rest_framework.decorators  import  action,api_view
from rest_framework import  viewsets
from testapp.models import *
from testapp.serializers import *
# Create your views here.
class LoginViewSet(viewsets.ModelViewSet):
  serializer_class = userAuthSerializer
  def create(self, request, *args, **kwargs):
      print(request.data)
      userName  = request.data.get('userName','')
      print(userName)
      userPwd  = request.data.get('UserPassWord','123456')
      print(userPwd)
      if userName:

        userAuth.objects.create(userName = userName ,userPassWord =userPwd)
        print('123128378192hahahahha')
        return Response({"code":0,"msg":"创建成功"})
      else:
        count = userAuth.objects.count()
        """
        我的想法是使用redis存一个hash结构。。这台电脑上没有redis。。我就把下面的那个简化一下 返回一个正整数
        """
        userName = (count+1)**2 +10086
        userAuth.objects.create(userName=userName, userPassWord=userPwd)
        return Response({"code": 0, "msg": "创建成功您随机生成的账号是："+userName+"初始密码为:"+userPwd})
  def list(self, request, *args, **kwargs):
    userName  = self.request.query_params.get('userName','')
    userPwd = self.request.query_params.get('userPwd','')
    try:
      user  = userAuth.objects.get(userName= userName)
    except Exception as e :
      return Response('请输入正确的用户名')
    if user.userPassWord == userPwd:
      return Response('登录成功')
    else:
      return Response('请输入正确的密码')
"""
下面这个是第一题的答案
"""
# 1.现要求游戏玩家的初始用户名是无重复切无规律的正整数，请参考postgreSQL中pseudo_encrypt()的原理，实现一个高效的用户名生成方法

# 原理：可用作唯一值的伪随机生成数。它产生一个整数输出。该整数输出唯一地与其整数输入相关联（通过数学排列），但同时看起来随机，且碰撞为0
#思路：编写一个字典方法来生成一个伪随机生成数，并且无碰撞
dic = {}
"""pk为数据库主键自增字段"""
def hashMapRandom(pk,dic):
  if pk not in dic:
     return dic.update({pk:pk**2*2+10086})
  else:
    return hashMapRandom(pk+1)


"""4如果要求用户名分为三段组成，分别为形容词、身份、地点 如"fancy black from Mirtore""
"""
"""下面是我的思路"""


"""我的思路是首先 形容词、身份、地点分为 三个表
当用户默认姓名出现时从每个表拿出来各一个单词 并记录 他们的PK主键 生成一个set集合 ，可以用redis数据库维护起来 ，如 (1,1,1)
然后固定前面的集合的两个数字 就例如 [(1,1,1),(1,1,2),(1,1,3),(1,1,4),(1,2,1),(1,2,2)]每次只需要判断 集合中的数字是否超过数据库表中数据个数即可
如果没超过数据库中的数据个数，那么加1否则前一位加1 当第一位到达数据库数据个数时 证明所有名称都已使用过 需要添加新的词汇
时间复杂度为O(1)
"""
