# coding=utf-8

"""
批量生成模拟数据
可在生成后删除.
"""
from datetime import datetime, timedelta
import os
import codecs
import time
import random

from faker import Faker
# from china_regions.data import provinces, get_cities_by_province, get_districts_by_city
import pandas
import numpy as np
import pandas as pd

def normal(size):
    arr = np.random.normal(size=size+1)
    arr = np.round(arr, decimals=2)
    return arr


def get(faker: Faker, mcfieldnamezh, mctablenamezh=''):
    """
    根据表字段的中文名修正为合适的生成方式
    扩展建议:
    根据字段名->实体名->枚举
    关联字段->同时生成多个字段
    """
    val = ''
    if 'ID' in mcfieldnamezh or '主键' in mcfieldnamezh or '唯一标识' in mcfieldnamezh:
        val = str(faker.uuid4())[:8]
        return val
    if '时间戳' == mcfieldnamezh:
        # val = str(int(time.mktime(faker.date_this_decade().timetuple())))
        # return val
        val = faker.date_between(
            start_date=datetime.now() - timedelta(days=3 * 4), end_date=datetime.now()
        )
        return val

    if '时间' in mcfieldnamezh:
        val = faker.date_between(start_date=datetime.now() - timedelta(days=3 * 4),
                                 end_date=datetime.now())
        return val
    if '日期' in mcfieldnamezh:
        val = faker.date_between(start_date=datetime.now() - timedelta(days=3 * 4),
                                 end_date=datetime.now())
        return val
    if '率' == mcfieldnamezh[-1]:
        val = int(normal(10)[faker.random.randint(0,10)])
        return val
    if '地点' in mcfieldnamezh:
        val = faker.address()
        return val
    # if '类型' in mcfieldnamezh or '类别' in mcfieldnamezh:
    #     val = faker.random.choice((
    #         # 根据文心一言/chatgpt/chatglm生产20个左右的类别即可.
    #     ))
    #     return val

        
    # 用户信息表
    
    # 用户信息表.用户ID唯一标识 <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID唯一标识':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 用户信息表.用户名用户登录名或昵称 <CharField>
    # 
    if mcfieldnamezh == '用户名用户登录名或昵称':
        
        # 给出一些用户信息表表中用户名用户登录名或昵称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 用户信息表.密码哈希存储加密后的密码 <CharField>
    # 
    if mcfieldnamezh == '密码哈希存储加密后的密码':
        
        # 给出一些用户信息表表中密码哈希存储加密后的密码的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 用户信息表.电子邮件用户邮箱地址 <TextField>
    # 
    if mcfieldnamezh == '电子邮件用户邮箱地址':
        
        # 给出一些用户信息表表中电子邮件用户邮箱地址的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 用户信息表.手机号码用户联系电话 <CharField>
    # 
    if mcfieldnamezh == '手机号码用户联系电话':
        
        # 给出一些用户信息表表中手机号码用户联系电话的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 用户信息表.注册时间用户注册时的日期和时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '注册时间用户注册时的日期和时间':
        
        # 给出一些用户信息表表中注册时间用户注册时的日期和时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 用户信息表.最后登录时间用户最后一次登录的日期和时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '最后登录时间用户最后一次登录的日期和时间':
        
        # 给出一些用户信息表表中最后登录时间用户最后一次登录的日期和时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 用户信息表.用户状态如活跃、禁用等 <CharField>
    # 
    if mcfieldnamezh == '用户状态如活跃、禁用等':
        
        # 载入配置成功
        # 给出一些用户信息表表中用户状态如活跃、禁用等的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '活跃', ' 禁用', ' 待审核', ' 已审核', ' 临时禁用', ' 已注销', ' 冻结', ' 锁定', ' 未激活', ' 已激活', ' 待支付', ' 已支付', ' 待发货', ' 已发货', ' 已完成', ' 已取消', ' 已退款', ' 已关闭', ' 警告中', ' 已恢复', '
    ))

        val = loadvalue
        
        return val
    
    # 用户信息表.头像URL用户头像图片的存储地址 <ImageField>
    # 
    if mcfieldnamezh == '头像URL用户头像图片的存储地址':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 用户信息表.角色ID关联到角色的ID示用户所属的角色 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '角色ID关联到角色的ID示用户所属的角色':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    
    # 平台账号表
    
    # 平台账号表.平台ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '平台ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 平台账号表.账号名称 <CharField>
    # 
    if mcfieldnamezh == '账号名称':
        
        # 给出一些平台账号表表中账号名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 平台账号表.账号类型 <CharField>
    # 
    if mcfieldnamezh == '账号类型':
        
        # 给出一些平台账号表表中账号类型的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 平台账号表.所属平台名称 <CharField>
    # 
    if mcfieldnamezh == '所属平台名称':
        
        # 给出一些平台账号表表中所属平台名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 平台账号表.用户名 <CharField>
    # 
    if mcfieldnamezh == '用户名':
        
        # 载入配置成功
        # 给出一些平台账号表表中用户名的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'Alice', ' Bob', ' Charlie', ' David', ' Eve', ' Frank', ' Grace', ' Henry', ' Ivy', ' John', ' Kate', ' Larry', ' Mary', ' Nick', ' Olivia', ' Peter', ' Quincy', ' Rachel', ' Sam', ' Tom', ', 'Alice', ' Bob', ' Charlie', ' David', ' Eve', ' Frank', ' Grace', ' Henry', ' Ivy', ' John', ' Kate', ' Larry', ' Mary', ' Nick', ' Olivia', ' Peter', ' Quincy', ' Rachel', ' Sam', ' Tom', '
    ))

        val = loadvalue
        
        return val
    
    # 平台账号表.密码加密存储 <CharField>
    # 
    if mcfieldnamezh == '密码加密存储':
        
        # 载入配置成功
        # 给出一些平台账号表表中密码加密存储的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'password_hash VARCHAR(255) NOT NULL', ' password_salt VARCHAR(255) NOT NULL', ' user_password_encrypted TEXT NOT NULL', ' account_pwd_secure VARCHAR(256) NOT NULL', ' secure_credential CHAR(60) NOT NULL', ' encrypted_pass BLOB NOT NULL', ' pwd_hash_value BINARY(64) NOT NULL', ' auth_token_encrypted TEXT NOT NULL', ' secure_pass_string VARCHAR(512) NOT NULL', ' pwd_encryption_key VARCHAR(128) NOT NULL', ' credential_secure_data TEXT NOT NULL', ' safe_password_storage TEXT NOT NULL', ' hash_of_password VARCHAR(255) NOT NULL', ' pwd_encryption_method VARCHAR(50) NOT NULL', ' password_protection TEXT NOT NULL', ' encrypted_credential_data BLOB NOT NULL', ' pwd_secure_string VARCHAR(512) NOT NULL', ' password_safe_hash VARCHAR(256) NOT NULL', ' secure_pwd_storage_field TEXT NOT NULL', ' encrypted_password_data TEXT NOT NULL', '
    ))

        val = loadvalue
        
        return val
    
    # 平台账号表.访问令牌 <CharField>
    # 
    if mcfieldnamezh == '访问令牌':
        
        # 给出一些平台账号表表中访问令牌的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 平台账号表.账号状态如启用、禁用 <CharField>
    # 
    if mcfieldnamezh == '账号状态如启用、禁用':
        
        # 给出一些平台账号表表中账号状态如启用、禁用的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 平台账号表.最后登录时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '最后登录时间':
        
        # 载入配置成功
        # 给出一些平台账号表表中最后登录时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 08:00:00', ' 2023-10-22 15:30:45', ' 2023-10-21 22:15:12', ' 2023-10-20 10:45:30', ', '2023-10-19 18:30:00', ' 2023-10-18 12:00:45', ' 2023-10-17 09:15:30', ' 2023-10-16 16:45:15', ', '2023-10-15 23:30:00', ' 2023-10-14 17:15:45', ' 2023-10-13 11:00:30', ' 2023-10-12 08:45:15', ', '2023-10-11 15:30:00', ' 2023-10-10 22:15:45', ' 2023-10-09 16:00:30', ' 2023-10-08 10:45:15', ', '2023-10-07 18:30:00', ' 2023-10-06 13:15:45', ' 2023-10-05 07:00:30', ' 2023-10-04 20:45:15', '
    ))

        val = loadvalue
        
        return val
    
    # 平台账号表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些平台账号表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 平台账号表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些平台账号表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 平台账号表.关联用户ID如果有用户与账号关联 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '关联用户ID如果有用户与账号关联':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    
    # 私信模板表
    
    # 私信模板表.模板ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '模板ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 私信模板表.模板名称 <CharField>
    # 
    if mcfieldnamezh == '模板名称':
        
        # 载入配置成功
        # 给出一些私信模板表表中模板名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '模板1', ' 模板2', ' 模板3', ' 模板4', ' 模板5', ' 模板6', ' 模板7', ' 模板8', ' 模板9', ' 模板10', ' 模板11', ' 模板12', ' 模板13', ' 模板14', ' 模板15', ' 模板16', ' 模板17', ' 模板18', ' 模板19', ' 模板20', '
    ))

        val = loadvalue
        
        return val
    
    # 私信模板表.模板内容 <TextField>
    # 
    if mcfieldnamezh == '模板内容':
        
        # 载入配置成功
        # 给出一些私信模板表表中模板内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '模板1：欢迎使用我们的服务', ' 模板2：您的订单已确认', ' 模板3：您的包裹已发货', ' 模板4：感谢您的反馈', ', '模板5：您的密码已重置', ' 模板6：欢迎加入我们的会员', ' 模板7：您的账户已激活', ' 模板8：您的订阅已更新', ', '模板9：您的支付已成功', ' 模板10：您的退款已处理', ' 模板11：产品库存告急', ' 模板12：新品上市通知', ', '模板13：促销活动即将开始', ' 模板14：您的优惠券已发送', ' 模板15：生日祝福', ' 模板16：会员专享优惠', ', '模板17：订单取消通知', ' 模板18：账户安全提醒', ' 模板19：服务更新通知', ' 模板20：联系我们获取帮助', '
    ))

        val = loadvalue
        
        return val
    
    # 私信模板表.创建者ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建者ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 私信模板表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些私信模板表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 私信模板表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些私信模板表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 私信模板表.是否激活 <BooleanField>
    # 
    if mcfieldnamezh == '是否激活':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    # 私信模板表.平台类型 <CharField>
    # 
    if mcfieldnamezh == '平台类型':
        
        # 给出一些私信模板表表中平台类型的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 私信模板表.目标用户ID可选用于指定特定用户 <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '目标用户ID可选用于指定特定用户':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    
    # 任务管理表
    
    # 任务管理表.任务ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '任务ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 任务管理表.任务名称 <CharField>
    # 
    if mcfieldnamezh == '任务名称':
        
        # 载入配置成功
        # 给出一些任务管理表表中任务名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '任务1', ' 任务2', ' 任务3', ' 任务4', ' 任务5', ' 任务6', ' 任务7', ' 任务8', ' 任务9', ' 任务10', ' 任务11', ' 任务12', ' 任务13', ' 任务14', ' 任务15', ' 任务16', ' 任务17', ' 任务18', ' 任务19', ' 任务20', '
    ))

        val = loadvalue
        
        return val
    
    # 任务管理表.平台 <CharField>
    # 
    if mcfieldnamezh == '平台':
        
        # 给出一些任务管理表表中平台的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 任务管理表.目标用户ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '目标用户ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 任务管理表.私信内容 <TextField>
    # 
    if mcfieldnamezh == '私信内容':
        
        # 给出一些任务管理表表中私信内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 任务管理表.计划执行时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '计划执行时间':
        
        # 给出一些任务管理表表中计划执行时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 任务管理表.任务状态 <CharField>
    # 
    if mcfieldnamezh == '任务状态':
        
        # 载入配置成功
        # 给出一些任务管理表表中任务状态的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '待分配', ' 已分配', ' 进行中', ' 待审核', ' 审核通过', ' 审核拒绝', ' 待修改', ' 已修改', ' 待确认', ' 已确认', ' 待执行', ' 执行中', ' 执行完成', ' 待关闭', ' 已关闭', ' 已取消', ' 暂停中', ' 已恢复', ' 延期中', ' 已完成', '
    ))

        val = loadvalue
        
        return val
    
    # 任务管理表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些任务管理表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 任务管理表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些任务管理表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 任务管理表.关联用户ID如任务创建者 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '关联用户ID如任务创建者':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    
    # 任务执行记录表
    
    # 任务执行记录表.任务ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '任务ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 任务执行记录表.执行时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '执行时间':
        
        # 载入配置成功
        # 给出一些任务执行记录表表中执行时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 09:30:15', ' 2023-10-23 10:15:45', ' 2023-10-23 11:00:00', ', '2023-10-23 12:15:30', ' 2023-10-23 13:30:00', ' 2023-10-23 14:45:15', ' 2023-10-23 15:45:30', ', '2023-10-23 16:30:00', ' 2023-10-23 17:15:45', ' 2023-10-23 18:00:00', ' 2023-10-23 19:30:15', ', '2023-10-23 20:45:30', ' 2023-10-23 21:30:00', ' 2023-10-23 22:15:45', ' 2023-10-23 23:00:00', ', '2023-10-24 00:30:15', ' 2023-10-24 01:45:30', ' 2023-10-24 02:30:00', ' 2023-10-24 03:15:45', '
    ))

        val = loadvalue
        
        return val
    
    # 任务执行记录表.执行状态 <CharField>
    # 
    if mcfieldnamezh == '执行状态':
        
        # 载入配置成功
        # 给出一些任务执行记录表表中执行状态的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '待执行', ' 执行中', ' 执行成功', ' 执行失败', ' 已取消', ' 已暂停', ' 待审核', ' 审核通过', ' 审核拒绝', ' 已提交', ' 已退回', ' 已重试', ' 部分成功', ' 部分失败', ' 正在排队', ' 已超时', ' 已忽略', ' 已跳过', ' 已合并', ' 已完成', '
    ))

        val = loadvalue
        
        return val
    
    # 任务执行记录表.用户ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 任务执行记录表.平台 <CharField>
    # 
    if mcfieldnamezh == '平台':
        
        # 给出一些任务执行记录表表中平台的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 任务执行记录表.私信内容 <TextField>
    # 
    if mcfieldnamezh == '私信内容':
        
        # 给出一些任务执行记录表表中私信内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 任务执行记录表.接收者ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '接收者ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 任务执行记录表.发送者ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '发送者ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 任务执行记录表.任务模板ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '任务模板ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 任务执行记录表.错误信息 <CharField>
    # 
    if mcfieldnamezh == '错误信息':
        
        # 载入配置成功
        # 给出一些任务执行记录表表中错误信息的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '无效的输入值', ', '系统内部错误', ', '数据库连接失败', ', '文件上传失败', ', '用户认证失败', ', '请求超时', ', '权限不足', ', '参数缺失', ', '数据格式不正确', ', '资源不存在', ', '操作被禁止', ', '服务器繁忙', ', '网络错误', ', '会话已过期', ', '验证码错误', ', '重复的操作', ', '无效的API调用', ', '数据校验失败', ', '超出最大限制', ', '系统维护中'
    ))

        val = loadvalue
        
        return val
    
    
    # 任务状态表
    
    # 任务状态表.任务ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '任务ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 任务状态表.状态码 <CharField>
    # 
    if mcfieldnamezh == '状态码':
        
        # 载入配置成功
        # 给出一些任务状态表表中状态码的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'SUCCESS', ' FAILURE', ' PENDING', ' CANCELLED', ' RUNNING', ' COMPLETED', ' EXPIRED', ' INVALID', ' DUPLICATE', ' APPROVED', ' DENIED', ' CREATED', ' UPDATED', ' DELETED', ' VERIFIED', ' UNVERIFIED', ' PAUSED', ' RESUMED', ' UNKNOWN', ' TEMPORARY', '
    ))

        val = loadvalue
        
        return val
    
    # 任务状态表.状态名称 <CharField>
    # 
    if mcfieldnamezh == '状态名称':
        
        # 载入配置成功
        # 给出一些任务状态表表中状态名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '状态1', ' 状态2', ' 状态3', ' 状态4', ' 状态5', ' 状态6', ' 状态7', ' 状态8', ' 状态9', ' 状态10', ' 状态11', ' 状态12', ' 状态13', ' 状态14', ' 状态15', ' 状态16', ' 状态17', ' 状态18', ' 状态19', ' 状态20', ', 'SELECT * FROM orders WHERE 状态名称 IN (状态1', ' 状态2', ' 状态3', ' 状态4', ' 状态5', ' 状态6', ' 状态7', ' 状态8', ' 状态9', ' 状态10', ' 状态11', ' 状态12', ' 状态13', ' 状态14', ' 状态15', ' 状态16', ' 状态17', ' 状态18', ' 状态19', ' 状态20);'
    ))

        val = loadvalue
        
        return val
    
    # 任务状态表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些任务状态表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 任务状态表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些任务状态表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 任务状态表.完成时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '完成时间':
        
        # 载入配置成功
        # 给出一些任务状态表表中完成时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 10:00:00', ' 2023-10-23 11:30:00', ' 2023-10-23 13:15:00', ' 2023-10-23 14:45:00', ' 2023-10-23 16:15:00', ' 2023-10-23 17:45:00', ' 2023-10-24 09:00:00', ' 2023-10-24 10:30:00', ' 2023-10-24 12:00:00', ' 2023-10-24 13:30:00', ' 2023-10-24 15:00:00', ' 2023-10-24 16:30:00', ' 2023-10-25 08:45:00', ' 2023-10-25 10:15:00', ' 2023-10-25 11:45:00', ' 2023-10-25 13:15:00', ' 2023-10-25 14:45:00', ' 2023-10-25 16:15:00', ' 2023-10-26 09:30:00', ' 2023-10-26 11:00:00', '
    ))

        val = loadvalue
        
        return val
    
    # 任务状态表.用户ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 任务状态表.平台ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '平台ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 任务状态表.私信内容 <TextField>
    # 
    if mcfieldnamezh == '私信内容':
        
        # 给出一些任务状态表表中私信内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 任务状态表.是否激活 <BooleanField>
    # 
    if mcfieldnamezh == '是否激活':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    
    # 定时任务表
    
    # 定时任务表.任务ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '任务ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 定时任务表.任务名称 <CharField>
    # 
    if mcfieldnamezh == '任务名称':
        
        # 载入配置成功
        # 给出一些定时任务表表中任务名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '任务1', ' 任务2', ' 任务3', ' 任务4', ' 任务5', ' 任务6', ' 任务7', ' 任务8', ' 任务9', ' 任务10', ' 任务11', ' 任务12', ' 任务13', ' 任务14', ' 任务15', ' 任务16', ' 任务17', ' 任务18', ' 任务19', ' 任务20', '
    ))

        val = loadvalue
        
        return val
    
    # 定时任务表.目标平台 <CharField>
    # 
    if mcfieldnamezh == '目标平台':
        
        # 给出一些定时任务表表中目标平台的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 定时任务表.计划执行时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '计划执行时间':
        
        # 给出一些定时任务表表中计划执行时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 定时任务表.执行状态 <CharField>
    # 
    if mcfieldnamezh == '执行状态':
        
        # 载入配置成功
        # 给出一些定时任务表表中执行状态的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '待执行', ' 执行中', ' 执行成功', ' 执行失败', ' 已取消', ' 已暂停', ' 待审核', ' 审核通过', ' 审核拒绝', ' 已提交', ' 已退回', ' 已重试', ' 部分成功', ' 部分失败', ' 正在排队', ' 已超时', ' 已忽略', ' 已跳过', ' 已合并', ' 已完成', '
    ))

        val = loadvalue
        
        return val
    
    # 定时任务表.最近一次错误信息 <CharField>
    # 
    if mcfieldnamezh == '最近一次错误信息':
        
        # 给出一些定时任务表表中最近一次错误信息的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 定时任务表.创建者 <CharField>
    # 
    if mcfieldnamezh == '创建者':
        
        # 载入配置成功
        # 给出一些定时任务表表中创建者的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'Alice', ' Bob', ' Charlie', ' David', ' Eva', ' Frank', ' Grace', ' Henry', ' Isabella', ' Jack', ', 'Kevin', ' Laura', ' Michael', ' Nina', ' Oliver', ' Patricia', ' Quentin', ' Rachel', ' Samuel', ' Tina', '
    ))

        val = loadvalue
        
        return val
    
    # 定时任务表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些定时任务表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 定时任务表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些定时任务表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 定时任务表.关联用户ID <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '关联用户ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    
    # 消息发送记录表
    
    # 消息发送记录表.唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送记录表.平台ID关联字段指向不同社交媒体或消息平台的ID <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '平台ID关联字段指向不同社交媒体或消息平台的ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送记录表.用户ID关联字段指向系统中用户的ID <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID关联字段指向系统中用户的ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送记录表.目标用户ID如果是私信则为目标接收者的ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '目标用户ID如果是私信则为目标接收者的ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送记录表.消息内容 <TextField>
    # 
    if mcfieldnamezh == '消息内容':
        
        # 载入配置成功
        # 给出一些消息发送记录表表中消息内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'Hello', ' how are you?', ' Good morning', ' everyone!', ' Have a nice day!', ' Whats up?', ' Meeting at 3pm?', ' Dont forget the deadline.', ' Can you help me with this?', ' Im feeling tired today.', ' Lets grab lunch!', ' Hows the project going?', ' Can you send me that file?', ' Ill be late today.', ' Reminder: team meeting at 10am.', ' I need to take a break.', ' Happy birthday!', ' Thank you for the help.', ' See you tomorrow.', ' Im on my way.', ' Please confirm receipt.', ' Everything is fine here.'
    ))

        val = loadvalue
        
        return val
    
    # 消息发送记录表.发送时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '发送时间':
        
        # 载入配置成功
        # 给出一些消息发送记录表表中发送时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 08:00:00', ' 2023-10-23 08:15:30', ' 2023-10-23 08:30:45', ' 2023-10-23 08:45:15', ', '2023-10-23 09:00:00', ' 2023-10-23 09:15:30', ' 2023-10-23 09:30:45', ' 2023-10-23 09:45:15', ', '2023-10-23 10:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 10:30:45', ' 2023-10-23 10:45:15', ', '2023-10-23 11:00:00', ' 2023-10-23 11:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 11:45:15', ', '2023-10-23 12:00:00', ' 2023-10-23 12:15:30', ' 2023-10-23 12:30:45', ' 2023-10-23 12:45:15', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送记录表.发送状态如待发送、发送中、已发送、发送失败 <CharField>
    # 
    if mcfieldnamezh == '发送状态如待发送、发送中、已发送、发送失败':
        
        # 给出一些消息发送记录表表中发送状态如待发送、发送中、已发送、发送失败的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送记录表.重试次数记录消息发送失败后的重试次数 <CharField>
    # 
    if mcfieldnamezh == '重试次数记录消息发送失败后的重试次数':
        
        # 给出一些消息发送记录表表中重试次数记录消息发送失败后的重试次数的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送记录表.上次重试时间记录最后一次尝试发送的时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '上次重试时间记录最后一次尝试发送的时间':
        
        # 给出一些消息发送记录表表中上次重试时间记录最后一次尝试发送的时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送记录表.错误信息如果发送失败记录失败的具体原因 <CharField>
    # 
    if mcfieldnamezh == '错误信息如果发送失败记录失败的具体原因':
        
        # 给出一些消息发送记录表表中错误信息如果发送失败记录失败的具体原因的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    
    # 消息接收记录表
    
    # 消息接收记录表.唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息接收记录表.用户ID关联用户 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID关联用户':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息接收记录表.平台ID关联平台 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '平台ID关联平台':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息接收记录表.消息内容 <TextField>
    # 
    if mcfieldnamezh == '消息内容':
        
        # 载入配置成功
        # 给出一些消息接收记录表表中消息内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'Hello', ' how are you?', ' Good morning', ' everyone!', ' Have a nice day!', ' Whats up?', ' Meeting at 3pm?', ' Dont forget the deadline.', ' Can you help me with this?', ' Im feeling tired today.', ' Lets grab lunch!', ' Hows the project going?', ' Can you send me that file?', ' Ill be late today.', ' Reminder: team meeting at 10am.', ' I need to take a break.', ' Happy birthday!', ' Thank you for the help.', ' See you tomorrow.', ' Im on my way.', ' Please confirm receipt.', ' Everything is fine here.'
    ))

        val = loadvalue
        
        return val
    
    # 消息接收记录表.接收时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '接收时间':
        
        # 给出一些消息接收记录表表中接收时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息接收记录表.接收状态如已接收、未处理、已处理等 <CharField>
    # 
    if mcfieldnamezh == '接收状态如已接收、未处理、已处理等':
        
        # 给出一些消息接收记录表表中接收状态如已接收、未处理、已处理等的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息接收记录表.回复内容 <TextField>
    # 
    if mcfieldnamezh == '回复内容':
        
        # 载入配置成功
        # 给出一些消息接收记录表表中回复内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '这是一个很好的问题', ' 谢谢你的帮助', ' 不客气，随时欢迎', ' 我很高兴能帮助你', ' 你的建议很有用', ' 我会考虑的', ' 期待你的回复', ' 请提供更多信息', ' 好的，我明白了', ' 我会尽快处理', ' 谢谢你的耐心等待', ' 这个问题有点复杂', ' 我会进一步调查', ' 请保持联系', ' 我会给你更新的', ' 再次感谢你的支持', ' 希望这能满足你的需求', ' 如果有其他问题，请告诉我', ' 祝你有愉快的一天', ' 再见！'
    ))

        val = loadvalue
        
        return val
    
    # 消息接收记录表.回复时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '回复时间':
        
        # 载入配置成功
        # 给出一些消息接收记录表表中回复时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-07-18 10:00:00', ' 2023-07-18 10:15:30', ' 2023-07-18 10:30:15', ' 2023-07-18 10:45:45', ' 2023-07-18 11:00:00', ' 2023-07-18 11:15:30', ' 2023-07-18 11:30:15', ' 2023-07-18 11:45:45', ' 2023-07-18 12:00:00', ' 2023-07-18 12:15:30', ' 2023-07-18 12:30:15', ' 2023-07-18 12:45:45', ' 2023-07-18 13:00:00', ' 2023-07-18 13:15:30', ' 2023-07-18 13:30:15', ' 2023-07-18 13:45:45', ' 2023-07-18 14:00:00', ' 2023-07-18 14:15:30', ' 2023-07-18 14:30:15', ' 2023-07-18 14:45:45', '
    ))

        val = loadvalue
        
        return val
    
    # 消息接收记录表.是否已读示用户是否已读该消息 <BooleanField>
    # 
    if mcfieldnamezh == '是否已读示用户是否已读该消息':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    
    # 用户偏好设置表
    
    # 用户偏好设置表.用户ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 用户偏好设置表.偏好名称 <CharField>
    # 
    if mcfieldnamezh == '偏好名称':
        
        # 载入配置成功
        # 给出一些用户偏好设置表表中偏好名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '阅读', '旅行', '音乐', '电影', '美食', '运动', '摄影', '艺术', '科技', '游戏', '购物', '健身', '编程', '写作', '绘画', '手工艺', '跳舞', '瑜伽', '茶道', '围棋', '
    ))

        val = loadvalue
        
        return val
    
    # 用户偏好设置表.偏好值 <CharField>
    # 
    if mcfieldnamezh == '偏好值':
        
        # 载入配置成功
        # 给出一些用户偏好设置表表中偏好值的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '阅读', ' 旅行', ' 音乐', ' 电影', ' 运动', ' 美食', ' 摄影', ' 游戏', ' 编程', ' 绘画', ' 瑜伽', ' 健身', ' 购物', ' 学习', ' 科技', ' 艺术', ' 历史', ' 自然', ' 宠物', ' 动漫', '
    ))

        val = loadvalue
        
        return val
    
    # 用户偏好设置表.偏好类型 <CharField>
    # 
    if mcfieldnamezh == '偏好类型':
        
        # 载入配置成功
        # 给出一些用户偏好设置表表中偏好类型的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '阅读', ' 旅行', ' 音乐', ' 电影', ' 运动', ' 美食', ' 购物', ' 科技', ' 艺术', ' 摄影', ' 游戏', ' 健身', ' 户外', ' 学习', ' 社交', ' 宠物', ' 自驾', ' 手工艺', ' 烹饪', ' 园艺', '
    ))

        val = loadvalue
        
        return val
    
    # 用户偏好设置表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些用户偏好设置表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 用户偏好设置表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些用户偏好设置表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 用户偏好设置表.是否激活 <BooleanField>
    # 
    if mcfieldnamezh == '是否激活':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    # 用户偏好设置表.偏好描述 <TextField>
    # 
    if mcfieldnamezh == '偏好描述':
        
        # 载入配置成功
        # 给出一些用户偏好设置表表中偏好描述的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '喜欢阅读科幻小说', ' 热爱户外运动，如徒步和骑行', ' 偏好观看悬疑电影', ' 对古典音乐有浓厚兴趣', ' 喜欢烹饪各种美食', ' 偏好旅行，探索新地方', ' 对摄影有浓厚兴趣', ' 喜欢收集邮票和硬币', ' 热爱篮球和足球', ' 偏好安静的环境，喜欢冥想', ' 喜欢阅读历史书籍', ' 热爱学习新技能', ' 偏好观看纪录片', ' 对艺术展览感兴趣', ' 喜欢种植花草', ' 热爱写作和创作', ' 偏好听摇滚音乐', ' 喜欢购物，特别是时尚服饰', ' 热爱电子游戏', ' 偏好观看动漫和卡通', '
    ))

        val = loadvalue
        
        return val
    
    # 用户偏好设置表.关联平台ID <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '关联平台ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    
    # 账号绑定关系表
    
    # 账号绑定关系表.唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 账号绑定关系表.账号ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '账号ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 账号绑定关系表.平台ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '平台ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 账号绑定关系表.绑定类型 <CharField>
    # 
    if mcfieldnamezh == '绑定类型':
        
        # 给出一些账号绑定关系表表中绑定类型的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 账号绑定关系表.绑定状态 <CharField>
    # 
    if mcfieldnamezh == '绑定状态':
        
        # 给出一些账号绑定关系表表中绑定状态的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 账号绑定关系表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些账号绑定关系表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 账号绑定关系表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些账号绑定关系表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 账号绑定关系表.用户ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    
    # 消息内容审核表
    
    # 消息内容审核表.消息内容审核ID <TextField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '消息内容审核ID':
        
        # 给出一些消息内容审核表表中消息内容审核ID的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息内容审核表.消息内容 <TextField>
    # 
    if mcfieldnamezh == '消息内容':
        
        # 载入配置成功
        # 给出一些消息内容审核表表中消息内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'Hello', ' how are you?', ' Good morning', ' everyone!', ' Have a nice day!', ' Whats up?', ' Meeting at 3pm?', ' Dont forget the deadline.', ' Can you help me with this?', ' Im feeling tired today.', ' Lets grab lunch!', ' Hows the project going?', ' Can you send me that file?', ' Ill be late today.', ' Reminder: team meeting at 10am.', ' I need to take a break.', ' Happy birthday!', ' Thank you for the help.', ' See you tomorrow.', ' Im on my way.', ' Please confirm receipt.', ' Everything is fine here.'
    ))

        val = loadvalue
        
        return val
    
    # 消息内容审核表.用户ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息内容审核表.平台名称 <CharField>
    # 
    if mcfieldnamezh == '平台名称':
        
        # 载入配置成功
        # 给出一些消息内容审核表表中平台名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '平台1', '平台2', '平台3', '平台4', '平台5', '平台6', '平台7', '平台8', '平台9', '平台10', '平台11', '平台12', '平台13', '平台14', '平台15', '平台16', '平台17', '平台18', '平台19', '平台20', '
    ))

        val = loadvalue
        
        return val
    
    # 消息内容审核表.审核状态 <CharField>
    # 
    if mcfieldnamezh == '审核状态':
        
        # 载入配置成功
        # 给出一些消息内容审核表表中审核状态的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '待审核', ' 审核中', ' 审核通过', ' 审核拒绝', ' 已重新提交', ' 需补充材料', ' 已退回', ' 已锁定', ' 已解锁', ' 已暂停', ' 已恢复', ' 待复审', ' 复审通过', ' 复审拒绝', ' 自动审核通过', ' 自动审核拒绝', ' 人工复审中', ' 已自动处理', ' 部分通过', ' 部分拒绝', '
    ))

        val = loadvalue
        
        return val
    
    # 消息内容审核表.审核时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '审核时间':
        
        # 载入配置成功
        # 给出一些消息内容审核表表中审核时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:30:00', ' 2023-10-24 12:45:15', ' 2023-10-25 14:15:30', ' 2023-10-26 08:00:00', ' 2023-10-27 10:30:45', ' 2023-10-28 13:15:10', ' 2023-10-29 16:00:00', ' 2023-10-30 18:30:15', ' 2023-10-31 21:00:30', ' 2023-11-01 00:15:00', ' 2023-11-02 03:30:00', ' 2023-11-03 06:45:15', ' 2023-11-04 09:00:00', ' 2023-11-05 11:30:45', ' 2023-11-06 14:15:10', ' 2023-11-07 16:45:00', ' 2023-11-08 19:15:15', ' 2023-11-09 21:45:30', ' 2023-11-10 00:30:00', ' 2023-11-11 03:00:00', '
    ))

        val = loadvalue
        
        return val
    
    # 消息内容审核表.审核员ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '审核员ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息内容审核表.拒绝原因 <CharField>
    # 
    if mcfieldnamezh == '拒绝原因':
        
        # 载入配置成功
        # 给出一些消息内容审核表表中拒绝原因的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '资料不全', ' 信息错误', ' 不符合要求', ' 重复申请', ' 信用评分不足', ' 年龄不符合', ' 地区限制', ' 职业不符', ' 收入不达标', ' 无法验证身份', ' 历史不良记录', ' 申请时间已过', ' 系统错误', ' 政策变动', ' 服务暂停', ' 资料过期', ' 联系方式无效', ' 未通过审核', ' 违反规定', ' 其他', '
    ))

        val = loadvalue
        
        return val
    
    # 消息内容审核表.是否敏感内容 <TextField>
    # 
    if mcfieldnamezh == '是否敏感内容':
        
        # 给出一些消息内容审核表表中是否敏感内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息内容审核表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些消息内容审核表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    
    # 消息发送失败日志表
    
    # 消息发送失败日志表.唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送失败日志表.消息ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '消息ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送失败日志表.平台名称 <CharField>
    # 
    if mcfieldnamezh == '平台名称':
        
        # 载入配置成功
        # 给出一些消息发送失败日志表表中平台名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '平台1', '平台2', '平台3', '平台4', '平台5', '平台6', '平台7', '平台8', '平台9', '平台10', '平台11', '平台12', '平台13', '平台14', '平台15', '平台16', '平台17', '平台18', '平台19', '平台20', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送失败日志表.用户ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送失败日志表.目标用户ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '目标用户ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送失败日志表.发送时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '发送时间':
        
        # 载入配置成功
        # 给出一些消息发送失败日志表表中发送时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 08:00:00', ' 2023-10-23 08:15:30', ' 2023-10-23 08:30:45', ' 2023-10-23 08:45:15', ', '2023-10-23 09:00:00', ' 2023-10-23 09:15:30', ' 2023-10-23 09:30:45', ' 2023-10-23 09:45:15', ', '2023-10-23 10:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 10:30:45', ' 2023-10-23 10:45:15', ', '2023-10-23 11:00:00', ' 2023-10-23 11:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 11:45:15', ', '2023-10-23 12:00:00', ' 2023-10-23 12:15:30', ' 2023-10-23 12:30:45', ' 2023-10-23 12:45:15', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送失败日志表.失败原因 <CharField>
    # 
    if mcfieldnamezh == '失败原因':
        
        # 载入配置成功
        # 给出一些消息发送失败日志表表中失败原因的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '网络连接错误', ' 服务器超时', ' 数据库连接失败', ' 文件读取错误', ' 权限不足', ' 参数错误', ' 无效的输入', ' 系统崩溃', ' 内存不足', ' 磁盘空间不足', ' 依赖服务未启动', ' 第三方API调用失败', ' 认证失败', ' 配置错误', ' 代码逻辑错误', ' 资源不存在', ' 请求超时', ' 加密错误', ' 数据格式错误', ' 未知错误', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送失败日志表.重试次数 <CharField>
    # 
    if mcfieldnamezh == '重试次数':
        
        # 载入配置成功
        # 给出一些消息发送失败日志表表中重试次数的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10', ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送失败日志表.上次重试时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '上次重试时间':
        
        # 给出一些消息发送失败日志表表中上次重试时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送失败日志表.是否已解决 <BooleanField>
    # 
    if mcfieldnamezh == '是否已解决':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    
    # 消息发送成功日志表
    
    # 消息发送成功日志表.消息ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '消息ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送成功日志表.平台名称 <CharField>
    # 
    if mcfieldnamezh == '平台名称':
        
        # 载入配置成功
        # 给出一些消息发送成功日志表表中平台名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '平台1', '平台2', '平台3', '平台4', '平台5', '平台6', '平台7', '平台8', '平台9', '平台10', '平台11', '平台12', '平台13', '平台14', '平台15', '平台16', '平台17', '平台18', '平台19', '平台20', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送成功日志表.用户ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送成功日志表.接收者ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '接收者ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送成功日志表.发送时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '发送时间':
        
        # 载入配置成功
        # 给出一些消息发送成功日志表表中发送时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 08:00:00', ' 2023-10-23 08:15:30', ' 2023-10-23 08:30:45', ' 2023-10-23 08:45:15', ', '2023-10-23 09:00:00', ' 2023-10-23 09:15:30', ' 2023-10-23 09:30:45', ' 2023-10-23 09:45:15', ', '2023-10-23 10:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 10:30:45', ' 2023-10-23 10:45:15', ', '2023-10-23 11:00:00', ' 2023-10-23 11:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 11:45:15', ', '2023-10-23 12:00:00', ' 2023-10-23 12:15:30', ' 2023-10-23 12:30:45', ' 2023-10-23 12:45:15', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送成功日志表.发送内容 <TextField>
    # 
    if mcfieldnamezh == '发送内容':
        
        # 给出一些消息发送成功日志表表中发送内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送成功日志表.发送状态 <CharField>
    # 
    if mcfieldnamezh == '发送状态':
        
        # 载入配置成功
        # 给出一些消息发送成功日志表表中发送状态的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '待发送', '已发送', '发送中', '发送失败', '发送成功', '部分发送', '排队中', '已取消', '已暂停', '正在重试', '已重试', '超时', '等待确认', '已确认', '已拒绝', '已退回', '已删除', '已过期', '已标记', '未知状态', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送成功日志表.错误信息 <CharField>
    # 
    if mcfieldnamezh == '错误信息':
        
        # 载入配置成功
        # 给出一些消息发送成功日志表表中错误信息的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '无效的输入值', ', '系统内部错误', ', '数据库连接失败', ', '文件上传失败', ', '用户认证失败', ', '请求超时', ', '权限不足', ', '参数缺失', ', '数据格式不正确', ', '资源不存在', ', '操作被禁止', ', '服务器繁忙', ', '网络错误', ', '会话已过期', ', '验证码错误', ', '重复的操作', ', '无效的API调用', ', '数据校验失败', ', '超出最大限制', ', '系统维护中'
    ))

        val = loadvalue
        
        return val
    
    # 消息发送成功日志表.关联任务ID <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '关联任务ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    
    # 消息模板分类表
    
    # 消息模板分类表.唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息模板分类表.分类名称 <CharField>
    # 
    if mcfieldnamezh == '分类名称':
        
        # 载入配置成功
        # 给出一些消息模板分类表表中分类名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '电子产品', ' 家用电器', ' 服装鞋帽', ' 食品饮料', ' 图书音像', ' 美妆护肤', ' 母婴用品', ' 家居家装', ' 运动户外', ' 汽车用品', ' 数码配件', ' 玩具乐器', ' 箱包配饰', ' 钟表眼镜', ' 珠宝首饰', ' 宠物用品', ' 文化娱乐', ' 办公用品', ' 厨具餐具', ' 礼品鲜花', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板分类表.分类描述 <TextField>
    # 
    if mcfieldnamezh == '分类描述':
        
        # 载入配置成功
        # 给出一些消息模板分类表表中分类描述的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '电子产品', '书籍与杂志', '家居用品', '服装与配饰', '美妆护肤', '食品饮料', '运动健身', '母婴用品', '汽车配件', '办公用品', '玩具与游戏', '珠宝首饰', '宠物用品', '旅行箱包', '数码配件', '园艺工具', '乐器与音响', '图书音像', '钟表眼镜', '厨具餐具', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板分类表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些消息模板分类表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板分类表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些消息模板分类表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板分类表.是否激活用于控制分类是否可用 <BooleanField>
    # 
    if mcfieldnamezh == '是否激活用于控制分类是否可用':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    # 消息模板分类表.父级分类ID用于构建分类层级结构 <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '父级分类ID用于构建分类层级结构':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息模板分类表.排序顺序用于控制分类在列中的显示顺序 <CharField>
    # 
    if mcfieldnamezh == '排序顺序用于控制分类在列中的显示顺序':
        
        # 给出一些消息模板分类表表中排序顺序用于控制分类在列中的显示顺序的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息模板分类表.模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护 <IntegerField>
    # 
    if mcfieldnamezh == '模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护':
        
        # 给出一些消息模板分类表表中模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    
    # 消息模板标签表
    
    # 消息模板标签表.唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息模板标签表.消息模板ID关联字段指向消息模板的ID <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '消息模板ID关联字段指向消息模板的ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息模板标签表.标签名称 <CharField>
    # 
    if mcfieldnamezh == '标签名称':
        
        # 载入配置成功
        # 给出一些消息模板标签表表中标签名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '标签1', ' 标签2', ' 标签3', ' 标签4', ' 标签5', ' 标签6', ' 标签7', ' 标签8', ' 标签9', ' 标签10', ' 标签11', ' 标签12', ' 标签13', ' 标签14', ' 标签15', ' 标签16', ' 标签17', ' 标签18', ' 标签19', ' 标签20', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板标签表.标签描述 <TextField>
    # 
    if mcfieldnamezh == '标签描述':
        
        # 载入配置成功
        # 给出一些消息模板标签表表中标签描述的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '用户姓名', ' 用户邮箱', ' 用户密码', ' 手机号码', ' 注册时间', ' 最后登录时间', ' 用户状态', ' 性别', ' 生日', ' 地址', ' 邮编', ' 国家', ' 省份', ' 城市', ' 职业', ' 兴趣爱好', ' 个人简介', ' 头像链接', ' 邮箱验证状态', ' 手机号码验证状态', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板标签表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些消息模板标签表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板标签表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些消息模板标签表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板标签表.是否激活用于控制标签是否可用 <BooleanField>
    # 
    if mcfieldnamezh == '是否激活用于控制标签是否可用':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    # 消息模板标签表.使用次数记录该标签被用于消息模板的次数 <CharField>
    # 
    if mcfieldnamezh == '使用次数记录该标签被用于消息模板的次数':
        
        # 给出一些消息模板标签表表中使用次数记录该标签被用于消息模板的次数的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息模板标签表.创建者ID关联字段指向用户的ID <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建者ID关联字段指向用户的ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    
    # 用户权限表
    
    # 用户权限表.用户ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 用户权限表.权限ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '权限ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 用户权限表.权限名称 <CharField>
    # 
    if mcfieldnamezh == '权限名称':
        
        # 载入配置成功
        # 给出一些用户权限表表中权限名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '读取权限', ' 写入权限', ' 编辑权限', ' 删除权限', ' 查看报告', ' 导出数据', ' 导入数据', ' 管理用户', ' 配置设置', ' 发送通知', ' 审核内容', ' 发布内容', ' 禁用账户', ' 启用账户', ' 重置密码', ' 访问后台', ' 查看日志', ' 下载文件', ' 上传文件', ' 执行命令', '
    ))

        val = loadvalue
        
        return val
    
    # 用户权限表.权限描述 <TextField>
    # 
    if mcfieldnamezh == '权限描述':
        
        # 载入配置成功
        # 给出一些用户权限表表中权限描述的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '读取数据', ' 写入数据', ' 修改数据', ' 删除数据', ' 导出数据', ' 导入数据', ' 查看报告', ' 生成报告', ' 管理用户', ' 分配权限', ' 设置角色', ' 审核数据', ' 发布内容', ' 撤销内容', ' 备份数据库', ' 恢复数据库', ' 访问日志', ' 修改密码', ' 禁用账户', ' 启用账户', ', 'INSERT INTO permissions (description) VALUES', '(读取数据)', ', '(写入数据)', ', '(修改数据)', ', '-- ... 以此类推，为其他权限描述添加更多的INSERT语句', ';'
    ))

        val = loadvalue
        
        return val
    
    # 用户权限表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些用户权限表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 用户权限表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些用户权限表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 用户权限表.是否激活 <BooleanField>
    # 
    if mcfieldnamezh == '是否激活':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    # 用户权限表.是否删除 <BooleanField>
    # 
    if mcfieldnamezh == '是否删除':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    # 用户权限表.角色名称关联字段 <SelectField>
    # 
    if mcfieldnamezh == '角色名称关联字段':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    
    # 系统配置表
    
    # 系统配置表.系统配置ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '系统配置ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 系统配置表.配置名称 <CharField>
    # 
    if mcfieldnamezh == '配置名称':
        
        # 载入配置成功
        # 给出一些系统配置表表中配置名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '配置1', ' 配置2', ' 配置3', ' 配置4', ' 配置5', ' 配置6', ' 配置7', ' 配置8', ' 配置9', ' 配置10', ' 配置11', ' 配置12', ' 配置13', ' 配置14', ' 配置15', ' 配置16', ' 配置17', ' 配置18', ' 配置19', ' 配置20', '
    ))

        val = loadvalue
        
        return val
    
    # 系统配置表.配置值 <CharField>
    # 
    if mcfieldnamezh == '配置值':
        
        # 载入配置成功
        # 给出一些系统配置表表中配置值的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'value1', ' value2', ' value3', ' value4', ' value5', ' value6', ' value7', ' value8', ' value9', ' value10', ' value11', ' value12', ' value13', ' value14', ' value15', ' value16', ' value17', ' value18', ' value19', ' value20', '
    ))

        val = loadvalue
        
        return val
    
    # 系统配置表.配置描述 <TextField>
    # 
    if mcfieldnamezh == '配置描述':
        
        # 载入配置成功
        # 给出一些系统配置表表中配置描述的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '配置项1描述', ' 配置项2描述', ' 配置项3详情', ' 设置项4说明', ' 参数5的用途', ' 选项6的设定', ' 功能7的配置', ' 属性8的注释', ' 值9的意义', ' 设置10的指南', ' 配置11的详情', ' 参数12的用途', ' 字段13的解释', ' 值14的设定', ' 描述15的内容', ' 配置项16的说明', ' 设置项17的用途', ' 参数18的详情', ' 功能19的注释', ' 属性20的指南', '
    ))

        val = loadvalue
        
        return val
    
    # 系统配置表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些系统配置表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 系统配置表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些系统配置表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 系统配置表.是否激活1为激活0为未激活 <BooleanField>
    # 
    if mcfieldnamezh == '是否激活1为激活0为未激活':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    # 系统配置表.创建者ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建者ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 系统配置表.关联系统ID <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '关联系统ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    
    # 通知推送表
    
    # 通知推送表.唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 通知推送表.平台ID关联字段指向平台的ID <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '平台ID关联字段指向平台的ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 通知推送表.用户ID关联字段指向用户的ID <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID关联字段指向用户的ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 通知推送表.消息内容 <TextField>
    # 
    if mcfieldnamezh == '消息内容':
        
        # 载入配置成功
        # 给出一些通知推送表表中消息内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'Hello', ' how are you?', ' Good morning', ' everyone!', ' Have a nice day!', ' Whats up?', ' Meeting at 3pm?', ' Dont forget the deadline.', ' Can you help me with this?', ' Im feeling tired today.', ' Lets grab lunch!', ' Hows the project going?', ' Can you send me that file?', ' Ill be late today.', ' Reminder: team meeting at 10am.', ' I need to take a break.', ' Happy birthday!', ' Thank you for the help.', ' See you tomorrow.', ' Im on my way.', ' Please confirm receipt.', ' Everything is fine here.'
    ))

        val = loadvalue
        
        return val
    
    # 通知推送表.推送状态例如待推送、已推送、推送失败 <CharField>
    # 
    if mcfieldnamezh == '推送状态例如待推送、已推送、推送失败':
        
        # 给出一些通知推送表表中推送状态例如待推送、已推送、推送失败的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 通知推送表.推送时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '推送时间':
        
        # 载入配置成功
        # 给出一些通知推送表表中推送时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 09:15:00', ' 2023-10-23 09:30:00', ' 2023-10-23 09:45:00', ', '2023-10-23 10:00:00', ' 2023-10-23 10:15:00', ' 2023-10-23 10:30:00', ' 2023-10-23 10:45:00', ', '2023-10-23 11:00:00', ' 2023-10-23 11:15:00', ' 2023-10-23 11:30:00', ' 2023-10-23 11:45:00', ', '2023-10-23 12:00:00', ' 2023-10-23 12:15:00', ' 2023-10-23 12:30:00', ' 2023-10-23 12:45:00', ', '2023-10-23 13:00:00', ' 2023-10-23 13:15:00', ' 2023-10-23 13:30:00', ' 2023-10-23 13:45:00', '
    ))

        val = loadvalue
        
        return val
    
    # 通知推送表.重试次数 <CharField>
    # 
    if mcfieldnamezh == '重试次数':
        
        # 载入配置成功
        # 给出一些通知推送表表中重试次数的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10', ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20', '
    ))

        val = loadvalue
        
        return val
    
    # 通知推送表.失败原因 <CharField>
    # 
    if mcfieldnamezh == '失败原因':
        
        # 载入配置成功
        # 给出一些通知推送表表中失败原因的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '网络连接错误', ' 服务器超时', ' 数据库连接失败', ' 文件读取错误', ' 权限不足', ' 参数错误', ' 无效的输入', ' 系统崩溃', ' 内存不足', ' 磁盘空间不足', ' 依赖服务未启动', ' 第三方API调用失败', ' 认证失败', ' 配置错误', ' 代码逻辑错误', ' 资源不存在', ' 请求超时', ' 加密错误', ' 数据格式错误', ' 未知错误', '
    ))

        val = loadvalue
        
        return val
    
    # 通知推送表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些通知推送表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 通知推送表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些通知推送表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    
    # 消息队列表
    
    # 消息队列表.消息ID唯一标识 <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '消息ID唯一标识':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息队列表.平台名称记录消息需要发送的平台如微信、微博等 <CharField>
    # 
    if mcfieldnamezh == '平台名称记录消息需要发送的平台如微信、微博等':
        
        # 给出一些消息队列表表中平台名称记录消息需要发送的平台如微信、微博等的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息队列表.用户ID接收消息的用户ID用于标识消息接收者 <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID接收消息的用户ID用于标识消息接收者':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息队列表.消息内容需要发送的具体消息内容 <TextField>
    # 
    if mcfieldnamezh == '消息内容需要发送的具体消息内容':
        
        # 给出一些消息队列表表中消息内容需要发送的具体消息内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息队列表.消息状态如待发送、发送中、已发送、发送失败等 <CharField>
    # 
    if mcfieldnamezh == '消息状态如待发送、发送中、已发送、发送失败等':
        
        # 给出一些消息队列表表中消息状态如待发送、发送中、已发送、发送失败等的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息队列表.创建时间消息加入队列的时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间消息加入队列的时间':
        
        # 给出一些消息队列表表中创建时间消息加入队列的时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息队列表.更新时间消息状态最后一次更新的时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间消息状态最后一次更新的时间':
        
        # 给出一些消息队列表表中更新时间消息状态最后一次更新的时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息队列表.重试次数如果消息发送失败记录重试的次数 <CharField>
    # 
    if mcfieldnamezh == '重试次数如果消息发送失败记录重试的次数':
        
        # 给出一些消息队列表表中重试次数如果消息发送失败记录重试的次数的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息队列表.下一次重试时间如果消息发送失败记录下一次尝试发送的时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '下一次重试时间如果消息发送失败记录下一次尝试发送的时间':
        
        # 给出一些消息队列表表中下一次重试时间如果消息发送失败记录下一次尝试发送的时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    
    # 消息队列状态表
    
    # 消息队列状态表.唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息队列状态表.平台ID关联字段指向不同平台的唯一标识 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '平台ID关联字段指向不同平台的唯一标识':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息队列状态表.消息ID关联字段指向具体消息的唯一标识 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '消息ID关联字段指向具体消息的唯一标识':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息队列状态表.状态如待发送、发送中、发送成功、发送失败 <CharField>
    # 
    if mcfieldnamezh == '状态如待发送、发送中、发送成功、发送失败':
        
        # 给出一些消息队列状态表表中状态如待发送、发送中、发送成功、发送失败的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息队列状态表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些消息队列状态表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 消息队列状态表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些消息队列状态表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 消息队列状态表.重试次数 <CharField>
    # 
    if mcfieldnamezh == '重试次数':
        
        # 载入配置成功
        # 给出一些消息队列状态表表中重试次数的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10', ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20', '
    ))

        val = loadvalue
        
        return val
    
    # 消息队列状态表.下一次重试时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '下一次重试时间':
        
        # 给出一些消息队列状态表表中下一次重试时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息队列状态表.错误信息如果发送失败记录失败原因 <CharField>
    # 
    if mcfieldnamezh == '错误信息如果发送失败记录失败原因':
        
        # 给出一些消息队列状态表表中错误信息如果发送失败记录失败原因的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    
    # 消息重试记录表
    
    # 消息重试记录表.消息ID关联消息的ID <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '消息ID关联消息的ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息重试记录表.平台名称 <CharField>
    # 
    if mcfieldnamezh == '平台名称':
        
        # 载入配置成功
        # 给出一些消息重试记录表表中平台名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '平台1', '平台2', '平台3', '平台4', '平台5', '平台6', '平台7', '平台8', '平台9', '平台10', '平台11', '平台12', '平台13', '平台14', '平台15', '平台16', '平台17', '平台18', '平台19', '平台20', '
    ))

        val = loadvalue
        
        return val
    
    # 消息重试记录表.目标用户ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '目标用户ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息重试记录表.消息内容 <TextField>
    # 
    if mcfieldnamezh == '消息内容':
        
        # 载入配置成功
        # 给出一些消息重试记录表表中消息内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    'Hello', ' how are you?', ' Good morning', ' everyone!', ' Have a nice day!', ' Whats up?', ' Meeting at 3pm?', ' Dont forget the deadline.', ' Can you help me with this?', ' Im feeling tired today.', ' Lets grab lunch!', ' Hows the project going?', ' Can you send me that file?', ' Ill be late today.', ' Reminder: team meeting at 10am.', ' I need to take a break.', ' Happy birthday!', ' Thank you for the help.', ' See you tomorrow.', ' Im on my way.', ' Please confirm receipt.', ' Everything is fine here.'
    ))

        val = loadvalue
        
        return val
    
    # 消息重试记录表.重试次数 <CharField>
    # 
    if mcfieldnamezh == '重试次数':
        
        # 载入配置成功
        # 给出一些消息重试记录表表中重试次数的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10', ' 11', ' 12', ' 13', ' 14', ' 15', ' 16', ' 17', ' 18', ' 19', ' 20', '
    ))

        val = loadvalue
        
        return val
    
    # 消息重试记录表.上次重试时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '上次重试时间':
        
        # 给出一些消息重试记录表表中上次重试时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息重试记录表.下一次重试时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '下一次重试时间':
        
        # 给出一些消息重试记录表表中下一次重试时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息重试记录表.消息状态如待发送、发送中、发送成功、发送失败 <CharField>
    # 
    if mcfieldnamezh == '消息状态如待发送、发送中、发送成功、发送失败':
        
        # 给出一些消息重试记录表表中消息状态如待发送、发送中、发送成功、发送失败的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息重试记录表.错误信息如果发送失败记录错误信息 <CharField>
    # 
    if mcfieldnamezh == '错误信息如果发送失败记录错误信息':
        
        # 给出一些消息重试记录表表中错误信息如果发送失败记录错误信息的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    
    # 账号黑名单表
    
    # 账号黑名单表.唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 账号黑名单表.账号ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '账号ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 账号黑名单表.黑名单类型 <CharField>
    # 
    if mcfieldnamezh == '黑名单类型':
        
        # 给出一些账号黑名单表表中黑名单类型的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 账号黑名单表.加入黑名单原因 <CharField>
    # 
    if mcfieldnamezh == '加入黑名单原因':
        
        # 给出一些账号黑名单表表中加入黑名单原因的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 账号黑名单表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些账号黑名单表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 账号黑名单表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些账号黑名单表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 账号黑名单表.是否有效用于标记黑名单记录是否仍然有效 <BooleanField>
    # 
    if mcfieldnamezh == '是否有效用于标记黑名单记录是否仍然有效':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    # 账号黑名单表.创建者ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建者ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 账号黑名单表.相关账号ID如果黑名单与特定操作或另一账号相关 <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '相关账号ID如果黑名单与特定操作或另一账号相关':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    
    # 用户反馈表
    
    # 用户反馈表.唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 用户反馈表.用户ID关联用户 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID关联用户':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 用户反馈表.反馈内容 <TextField>
    # 
    if mcfieldnamezh == '反馈内容':
        
        # 载入配置成功
        # 给出一些用户反馈表表中反馈内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '这是一个很好的产品，我非常满意。', ', '服务很周到，下次还会再来。', ', '产品有些小瑕疵，但整体来说还不错。', ', '希望下次能提供更多优惠活动。', ', '发货速度很快，包装也很安全。', ', '产品功能齐全，操作简单易懂。', ', '对客服的响应速度表示满意。', ', '产品质量有待提高，希望厂家能重视。', ', '购买体验很愉快，会继续支持。', ', '希望产品能更新更多功能。', ', '非常满意这次的购物体验，强烈推荐。', ', '物流信息更新及时，很方便查询。', ', '产品外观精美，性能稳定。', ', '希望售后服务能更加完善。', ', '价格合理，性价比高。', ', '产品使用效果很好，符合预期。', ', '希望下次能有更多选择。', ', '对产品的细节处理表示赞赏。', ', '购物流程很顺畅，没有遇到任何问题。', ', '期待下次能有更多新品上市。'
    ))

        val = loadvalue
        
        return val
    
    # 用户反馈表.反馈类型如建议、投诉、咨询等 <TextField>
    # 
    if mcfieldnamezh == '反馈类型如建议、投诉、咨询等':
        
        # 给出一些用户反馈表表中反馈类型如建议、投诉、咨询等的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 用户反馈表.反馈创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '反馈创建时间':
        
        # 载入配置成功
        # 给出一些用户反馈表表中反馈创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '反馈创建时间', '反馈创建时间', '反馈创建时间', '反馈创建时间', '反馈创建时间', ', '2023-10-23 10:00:00', '2023-10-23 11:30:15', '2023-10-23 13:45:30', '2023-10-23 15:15:45', '2023-10-23 17:00:00', '
    ))

        val = loadvalue
        
        return val
    
    # 用户反馈表.反馈状态如待处理、已处理、已忽略等 <CharField>
    # 
    if mcfieldnamezh == '反馈状态如待处理、已处理、已忽略等':
        
        # 给出一些用户反馈表表中反馈状态如待处理、已处理、已忽略等的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 用户反馈表.回复内容 <TextField>
    # 
    if mcfieldnamezh == '回复内容':
        
        # 载入配置成功
        # 给出一些用户反馈表表中回复内容的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '这是一个很好的问题', ' 谢谢你的帮助', ' 不客气，随时欢迎', ' 我很高兴能帮助你', ' 你的建议很有用', ' 我会考虑的', ' 期待你的回复', ' 请提供更多信息', ' 好的，我明白了', ' 我会尽快处理', ' 谢谢你的耐心等待', ' 这个问题有点复杂', ' 我会进一步调查', ' 请保持联系', ' 我会给你更新的', ' 再次感谢你的支持', ' 希望这能满足你的需求', ' 如果有其他问题，请告诉我', ' 祝你有愉快的一天', ' 再见！'
    ))

        val = loadvalue
        
        return val
    
    # 用户反馈表.回复时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '回复时间':
        
        # 载入配置成功
        # 给出一些用户反馈表表中回复时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-07-18 10:00:00', ' 2023-07-18 10:15:30', ' 2023-07-18 10:30:15', ' 2023-07-18 10:45:45', ' 2023-07-18 11:00:00', ' 2023-07-18 11:15:30', ' 2023-07-18 11:30:15', ' 2023-07-18 11:45:45', ' 2023-07-18 12:00:00', ' 2023-07-18 12:15:30', ' 2023-07-18 12:30:15', ' 2023-07-18 12:45:45', ' 2023-07-18 13:00:00', ' 2023-07-18 13:15:30', ' 2023-07-18 13:30:15', ' 2023-07-18 13:45:45', ' 2023-07-18 14:00:00', ' 2023-07-18 14:15:30', ' 2023-07-18 14:30:15', ' 2023-07-18 14:45:45', '
    ))

        val = loadvalue
        
        return val
    
    # 用户反馈表.是否已解决是否 <BooleanField>
    # 
    if mcfieldnamezh == '是否已解决是否':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    
    # 账号安全日志表
    
    # 账号安全日志表.日志ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '日志ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 账号安全日志表.账号ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '账号ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 账号安全日志表.日志类型 <CharField>
    # 
    if mcfieldnamezh == '日志类型':
        
        # 载入配置成功
        # 给出一些账号安全日志表表中日志类型的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '系统登录', ' 用户注册', ' 密码修改', ' 订单创建', ' 订单支付', ' 商品浏览', ' 购物车添加', ' 购物车删除', ' 优惠券领取', ' 评论发布', ' 订单取消', ' 退款申请', ' 退款成功', ' 系统错误', ' 用户反馈', ' 营销活动参与', ' 会员等级变更', ' 密码找回', ' 邮件发送', ' 短信发送', ', '系统登录', ' 用户注册', ' 密码修改', ' 订单创建', ' 订单支付', ' 商品浏览', ' 购物车添加', ' 购物车删除', ' 优惠券领取', ' 评论发布', ' 订单取消', ' 退款申请', ' 退款成功', ' 系统错误', ' 用户反馈', ' 营销活动参与', ' 会员等级变更', ' 密码找回', ' 邮件发送', ' 短信发送', '
    ))

        val = loadvalue
        
        return val
    
    # 账号安全日志表.动作描述 <TextField>
    # 
    if mcfieldnamezh == '动作描述':
        
        # 载入配置成功
        # 给出一些账号安全日志表表中动作描述的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '登录系统', ' 退出系统', ' 创建订单', ' 修改订单信息', ' 删除订单', ' 查看订单详情', ' 添加商品到购物车', ' 从购物车移除商品', ' 结算购物车', ' 修改密码', ' 发送邮件', ' 接收通知', ' 上传文件', ' 下载文件', ' 分享链接', ' 评论商品', ' 点赞商品', ' 取消点赞', ' 修改个人资料', ' 重置个人资料', '
    ))

        val = loadvalue
        
        return val
    
    # 账号安全日志表.地址 <TextField>
    # 
    if mcfieldnamezh == '地址':
        
        # 载入配置成功
        # 给出一些账号安全日志表表中地址的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '北京市朝阳区三里屯路1号', ' 上海市浦东新区世纪大道100号', ' 广州市天河区珠江新城华夏路8号', ' 深圳市福田区福华三路88号', ' 杭州市西湖区文三路478号', ' 成都市锦江区红星路二段99号', ' 重庆市渝中区解放碑步行街1号', ' 天津市和平区南京路123号', ' 北京市西城区金融大街1号', ' 上海市黄浦区南京东路200号', ' 广州市越秀区中山五路33号', ' 深圳市罗湖区深南东路5002号', ' 杭州市拱墅区莫干山路111号', ' 南京市秦淮区中山南路89号', ' 武汉市江汉区解放大道688号', ' 西安市碑林区南大街1号', ' 沈阳市和平区中山路123号', ' 长沙市天心区黄兴南路步行街88号', ' 青岛市市南区香港中路10号', ' 厦门市思明区中山路步行街1号', '
    ))

        val = loadvalue
        
        return val
    
    # 账号安全日志表.时间戳 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '时间戳':
        
        # 载入配置成功
        # 给出一些账号安全日志表表中时间戳的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 08:00:00', ' 2023-10-23 09:15:30', ' 2023-10-23 10:30:45', ' 2023-10-23 12:00:15', ' 2023-10-23 13:45:20', ' 2023-10-23 15:15:00', ' 2023-10-23 16:30:15', ' 2023-10-23 18:00:30', ' 2023-10-23 19:15:45', ' 2023-10-23 20:30:00', ' 2023-10-23 21:45:15', ' 2023-10-23 23:00:00', ' 2023-10-24 00:15:30', ' 2023-10-24 01:30:45', ' 2023-10-24 03:00:15', ' 2023-10-24 04:45:20', ' 2023-10-24 06:15:00', ' 2023-10-24 07:30:15', ' 2023-10-24 08:45:30', ' 2023-10-24 10:00:00', '
    ))

        val = loadvalue
        
        return val
    
    # 账号安全日志表.结果状态 <CharField>
    # 
    if mcfieldnamezh == '结果状态':
        
        # 载入配置成功
        # 给出一些账号安全日志表表中结果状态的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '成功', '失败', '待处理', '已取消', '已拒绝', '已提交', '审核中', '已完成', '部分成功', '超时', '未知状态', '已暂停', '已恢复', '已重新提交', '已退回', '已确认', '已忽略', '已删除', '已锁定', '已解锁', '
    ))

        val = loadvalue
        
        return val
    
    # 账号安全日志表.描述信息 <TextField>
    # 
    if mcfieldnamezh == '描述信息':
        
        # 载入配置成功
        # 给出一些账号安全日志表表中描述信息的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '姓名', '年龄', '性别', '生日', '地址', '邮编', '电话', '电子邮件', '职业', '学历', '公司名', '部门', '职位', '入职日期', '离职日期', '薪资', '工作内容', '技能', '兴趣爱好', '备注', ', 'CREATE TABLE employees (', '姓名 VARCHAR(50)', ', '年龄 INT', ', '性别 VARCHAR(10)', ', '-- ... 其他字段定义 ...', '备注 TEXT', ');'
    ))

        val = loadvalue
        
        return val
    
    # 账号安全日志表.关联账号ID <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '关联账号ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    
    # 消息模板编辑历史表
    
    # 消息模板编辑历史表.唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息模板编辑历史表.消息模板ID关联字段指向消息模板的ID <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '消息模板ID关联字段指向消息模板的ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息模板编辑历史表.编辑者ID关联字段指向用户的ID <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '编辑者ID关联字段指向用户的ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息模板编辑历史表.编辑时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '编辑时间':
        
        # 载入配置成功
        # 给出一些消息模板编辑历史表表中编辑时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:30', ' 2023-10-23 15:15:45', ' 2023-10-23 16:30:00', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:30', ' 2023-10-24 14:15:45', ' 2023-10-24 15:30:00', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', ' 2023-10-25 10:45:15', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板编辑历史表.编辑内容本次编辑的具体内容或变更 <TextField>
    # 
    if mcfieldnamezh == '编辑内容本次编辑的具体内容或变更':
        
        # 给出一些消息模板编辑历史表表中编辑内容本次编辑的具体内容或变更的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息模板编辑历史表.版本号每次编辑递增 <CharField>
    # 
    if mcfieldnamezh == '版本号每次编辑递增':
        
        # 给出一些消息模板编辑历史表表中版本号每次编辑递增的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息模板编辑历史表.状态如有效、已删除等 <CharField>
    # 
    if mcfieldnamezh == '状态如有效、已删除等':
        
        # 给出一些消息模板编辑历史表表中状态如有效、已删除等的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息模板编辑历史表.备注编辑时的额外说明或备注信息 <CharField>
    # 
    if mcfieldnamezh == '备注编辑时的额外说明或备注信息':
        
        # 给出一些消息模板编辑历史表表中备注编辑时的额外说明或备注信息的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息模板编辑历史表.是否为最新版本标识当前记录是否为该模板的最新编辑版本 <BooleanField>
    # 
    if mcfieldnamezh == '是否为最新版本标识当前记录是否为该模板的最新编辑版本':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    
    # 消息模板审核记录表
    
    # 消息模板审核记录表.唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息模板审核记录表.消息模板ID关联消息模板 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '消息模板ID关联消息模板':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息模板审核记录表.审核者ID关联用户 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '审核者ID关联用户':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息模板审核记录表.审核时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '审核时间':
        
        # 载入配置成功
        # 给出一些消息模板审核记录表表中审核时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:30:00', ' 2023-10-24 12:45:15', ' 2023-10-25 14:15:30', ' 2023-10-26 08:00:00', ' 2023-10-27 10:30:45', ' 2023-10-28 13:15:10', ' 2023-10-29 16:00:00', ' 2023-10-30 18:30:15', ' 2023-10-31 21:00:30', ' 2023-11-01 00:15:00', ' 2023-11-02 03:30:00', ' 2023-11-03 06:45:15', ' 2023-11-04 09:00:00', ' 2023-11-05 11:30:45', ' 2023-11-06 14:15:10', ' 2023-11-07 16:45:00', ' 2023-11-08 19:15:15', ' 2023-11-09 21:45:30', ' 2023-11-10 00:30:00', ' 2023-11-11 03:00:00', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板审核记录表.审核状态如待审核、审核通过、审核拒绝 <CharField>
    # 
    if mcfieldnamezh == '审核状态如待审核、审核通过、审核拒绝':
        
        # 给出一些消息模板审核记录表表中审核状态如待审核、审核通过、审核拒绝的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息模板审核记录表.审核意见 <CharField>
    # 
    if mcfieldnamezh == '审核意见':
        
        # 载入配置成功
        # 给出一些消息模板审核记录表表中审核意见的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '意见1', ' 意见2', ' 需要进一步核实', ' 内容基本准确', ' 格式不符合要求', ' 请补充详细信息', ' 已审核通过', ' 存在逻辑错误', ' 请修改后再提交', ' 图片不清晰', ' 建议增加相关内容', ' 内容过长，请精简', ' 与主题不符', ' 数据不准确', ' 审核中...', ' 请确保信息真实有效', ' 请检查错别字', ' 已拒绝', ' 请重新提交', ' 其他意见', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板审核记录表.记录创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '记录创建时间':
        
        # 载入配置成功
        # 给出一些消息模板审核记录表表中记录创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 15:30:00', ', '2023-10-23 15:30:00', ' 2023-10-24 09:15:45', ' 2023-10-25 21:00:12', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板审核记录表.记录更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '记录更新时间':
        
        # 载入配置成功
        # 给出一些消息模板审核记录表表中记录更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 10:01:02', ' 2023-10-23 10:02:15', ' 2023-10-23 10:03:30', ' 2023-10-23 10:04:45', ', '2023-10-23 10:06:00', ' 2023-10-23 10:07:15', ' 2023-10-23 10:08:30', ' 2023-10-23 10:09:45', ', '2023-10-23 10:11:00', ' 2023-10-23 10:12:15', ' 2023-10-23 10:13:30', ' 2023-10-23 10:14:45', ', '2023-10-23 10:16:00', ' 2023-10-23 10:17:15', ' 2023-10-23 10:18:30', ' 2023-10-23 10:19:45', ', '2023-10-23 10:21:00', ' 2023-10-23 10:22:15', ' 2023-10-23 10:23:30', ' 2023-10-23 10:24:45', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板审核记录表.是否删除逻辑删除标记 <BooleanField>
    # 
    if mcfieldnamezh == '是否删除逻辑删除标记':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    
    # 消息发送策略表
    
    # 消息发送策略表.策略ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '策略ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送策略表.策略名称 <CharField>
    # 
    if mcfieldnamezh == '策略名称':
        
        # 载入配置成功
        # 给出一些消息发送策略表表中策略名称的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '策略1', ' 策略2', ' 策略3', ' 策略4', ' 策略5', ' 策略6', ' 策略7', ' 策略8', ' 策略9', ' 策略10', ' 策略11', ' 策略12', ' 策略13', ' 策略14', ' 策略15', ' 策略16', ' 策略17', ' 策略18', ' 策略19', ' 策略20', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送策略表.策略描述 <TextField>
    # 
    if mcfieldnamezh == '策略描述':
        
        # 载入配置成功
        # 给出一些消息发送策略表表中策略描述的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '这是一个简单的测试策略描述', ' 用于演示字段内容的示例', ' 针对特定场景的策略描述', ' 详细描述策略的目标和效果', ' 包含多个关键字的策略描述', ' 详细列出策略实施步骤的描述', ' 针对用户行为的个性化策略描述', ' 基于数据分析的精准策略描述', ' 针对市场趋势的策略描述', ' 长期有效的稳定策略描述', ' 短期快速响应的策略描述', ' 考虑多种因素的综合性策略描述', ' 强调用户体验的策略描述', ' 突出产品优势的策略描述', ' 针对特定用户群体的策略描述', ' 包含风险评估的策略描述', ' 强调数据安全的策略描述', ' 基于历史数据的策略描述', ' 实时调整的动态策略描述', ' 用于提升转化率的策略描述', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送策略表.平台类型 <CharField>
    # 
    if mcfieldnamezh == '平台类型':
        
        # 给出一些消息发送策略表表中平台类型的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送策略表.目标类型 <CharField>
    # 
    if mcfieldnamezh == '目标类型':
        
        # 给出一些消息发送策略表表中目标类型的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送策略表.内容模板 <TextField>
    # 
    if mcfieldnamezh == '内容模板':
        
        # 给出一些消息发送策略表表中内容模板的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送策略表.计划类型如一次性、周期性 <CharField>
    # 
    if mcfieldnamezh == '计划类型如一次性、周期性':
        
        # 给出一些消息发送策略表表中计划类型如一次性、周期性的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送策略表.开始时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '开始时间':
        
        # 载入配置成功
        # 给出一些消息发送策略表表中开始时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-01-01 00:00:00', ' 2023-01-02 12:34:56', ' 2023-01-03 23:59:59', ', '2023-01-04 08:00:00', ' 2023-01-05 14:15:16', ' 2023-01-06 09:30:00', ', '2023-01-07 11:00:00', ' 2023-01-08 17:45:00', ' 2023-01-09 10:20:30', ', '2023-01-10 19:00:00', ' 2023-01-11 13:15:45', ' 2023-01-12 22:45:00', ', '2023-01-13 01:30:00', ' 2023-01-14 16:00:00', ' 2023-01-15 04:45:00', ', '2023-01-16 18:30:00', ' 2023-01-17 07:15:00', ' 2023-01-18 20:45:00', ', '2023-01-19 06:00:00', ' 2023-01-20 15:00:00', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送策略表.结束时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '结束时间':
        
        # 载入配置成功
        # 给出一些消息发送策略表表中结束时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 10:00:00', ' 2023-10-23 12:30:15', ' 2023-10-23 15:45:30', ' 2023-10-24 08:15:00', ', '2023-10-24 11:00:45', ' 2023-10-24 13:30:15', ' 2023-10-25 09:45:30', ' 2023-10-25 12:15:00', ', '2023-10-25 14:45:15', ' 2023-10-26 10:30:00', ' 2023-10-26 13:00:45', ' 2023-10-26 15:30:15', ', '2023-10-27 08:45:30', ' 2023-10-27 11:15:00', ' 2023-10-27 13:45:45', ' 2023-10-28 09:30:15', ', '2023-10-28 12:00:30', ' 2023-10-28 14:30:00', ' 2023-10-29 10:15:45', ' 2023-10-29 12:45:15'
    ))

        val = loadvalue
        
        return val
    
    # 消息发送策略表.用户ID关联用户 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID关联用户':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送策略表.状态如启用、禁用 <CharField>
    # 
    if mcfieldnamezh == '状态如启用、禁用':
        
        # 载入配置成功
        # 给出一些消息发送策略表表中状态如启用、禁用的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '启用', '禁用', '启用', '禁用', '启用', '禁用', '启用', '禁用', '启用', '禁用', '启用', '禁用', '启用', '禁用', '启用', '禁用', '启用', '禁用', '启用', '禁用', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送策略表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些消息发送策略表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送策略表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些消息发送策略表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    
    # 消息发送频率限制表
    
    # 消息发送频率限制表.唯一标识符 <UUIDField>
    # 
    if mcfieldnamezh == '唯一标识符':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送频率限制表.平台ID关联到不同平台的用于区分不同平台的发送频率限制 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '平台ID关联到不同平台的用于区分不同平台的发送频率限制':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送频率限制表.用户ID关联到用户示该限制是针对哪个用户的 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID关联到用户示该限制是针对哪个用户的':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送频率限制表.消息类型如文本、图片、视频等用于区分不同类型的消息发送频率 <ImageField>
    # 
    if mcfieldnamezh == '消息类型如文本、图片、视频等用于区分不同类型的消息发送频率':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送频率限制表.最大发送次数在指定时间周期内允许的最大发送次数 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '最大发送次数在指定时间周期内允许的最大发送次数':
        
        # 给出一些消息发送频率限制表表中最大发送次数在指定时间周期内允许的最大发送次数的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送频率限制表.时间周期如每天、每小时等示上述最大发送次数的时间范围 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '时间周期如每天、每小时等示上述最大发送次数的时间范围':
        
        # 给出一些消息发送频率限制表表中时间周期如每天、每小时等示上述最大发送次数的时间范围的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送频率限制表.上次发送时间记录最后一次发送消息的时间用于计算下一次发送的时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '上次发送时间记录最后一次发送消息的时间用于计算下一次发送的时间':
        
        # 给出一些消息发送频率限制表表中上次发送时间记录最后一次发送消息的时间用于计算下一次发送的时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送频率限制表.重置时间时间周期的开始时间用于重置发送次数计数器 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '重置时间时间周期的开始时间用于重置发送次数计数器':
        
        # 给出一些消息发送频率限制表表中重置时间时间周期的开始时间用于重置发送次数计数器的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送频率限制表.状态如启用、禁用示该频率限制是否生效 <BooleanField>
    # 
    if mcfieldnamezh == '状态如启用、禁用示该频率限制是否生效':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    # 消息发送频率限制表.备注用于记录该频率限制的其他相关信息或说明 <CharField>
    # 
    if mcfieldnamezh == '备注用于记录该频率限制的其他相关信息或说明':
        
        # 给出一些消息发送频率限制表表中备注用于记录该频率限制的其他相关信息或说明的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    
    # 消息发送优先级表
    
    # 消息发送优先级表.自增ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '自增ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送优先级表.优先级等级 <CharField>
    # 
    if mcfieldnamezh == '优先级等级':
        
        # 给出一些消息发送优先级表表中优先级等级的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送优先级表.优先级描述 <TextField>
    # 
    if mcfieldnamezh == '优先级描述':
        
        # 载入配置成功
        # 给出一些消息发送优先级表表中优先级描述的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '最高', ' 非常高', ' 高', ' 较高', ' 中上', ' 中等', ' 中下', ' 稍低', ' 低', ' 较低', ' 很低', ' 非常低', ' 紧急', ' 重要', ' 一般', ' 次要', ' 可选', ' 不推荐', ' 低优先级', ' 最低', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送优先级表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些消息发送优先级表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送优先级表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些消息发送优先级表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 消息发送优先级表.是否激活 <BooleanField>
    # 
    if mcfieldnamezh == '是否激活':
        
        val = faker.random.choice(('1', '0'))
        
        return val
    
    # 消息发送优先级表.平台ID关联字段指向平台 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '平台ID关联字段指向平台':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送优先级表.消息类型ID关联字段指向消息类型 <SelectField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '消息类型ID关联字段指向消息类型':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息发送优先级表.默认延迟时间秒 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '默认延迟时间秒':
        
        # 给出一些消息发送优先级表表中默认延迟时间秒的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息发送优先级表.最大重试次数 <CharField>
    # 
    if mcfieldnamezh == '最大重试次数':
        
        # 给出一些消息发送优先级表表中最大重试次数的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    
    # 消息模板使用统计表
    
    # 消息模板使用统计表.消息模板ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '消息模板ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息模板使用统计表.使用次数 <CharField>
    # 
    if mcfieldnamezh == '使用次数':
        
        # 载入配置成功
        # 给出一些消息模板使用统计表表中使用次数的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '123', '456', '789', '101', '122', '143', '164', '185', '206', '227', '248', '269', '290', '311', '332', '353', '374', '395', '416', '437', ', 'INSERT INTO usage_table (usage_count) VALUES', '(123)', '(456)', '(789)', '(101)', '(122)', '(143)', '(164)', '(185)', '(206)', '(227)', ', '(248)', '(269)', '(290)', '(311)', '(332)', '(353)', '(374)', '(395)', '(416)', '(437);'
    ))

        val = loadvalue
        
        return val
    
    # 消息模板使用统计表.最后使用时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '最后使用时间':
        
        # 载入配置成功
        # 给出一些消息模板使用统计表表中最后使用时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 10:00:00', ' 2023-10-22 15:30:45', ' 2023-10-21 22:15:12', ' 2023-10-20 09:45:30', ' 2023-10-19 14:20:00', ' 2023-10-18 18:30:15', ' 2023-10-17 12:45:00', ' 2023-10-16 21:00:30', ' 2023-10-15 16:15:45', ' 2023-10-14 11:30:00', ' 2023-10-13 19:45:15', ' 2023-10-12 13:00:30', ' 2023-10-11 08:15:45', ' 2023-10-10 20:30:00', ' 2023-10-09 15:45:15', ' 2023-10-08 22:00:30', ' 2023-10-07 17:15:45', ' 2023-10-06 11:30:00', ' 2023-10-05 09:45:15', ' 2023-10-04 14:00:30', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板使用统计表.创建时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '创建时间':
        
        # 载入配置成功
        # 给出一些消息模板使用统计表表中创建时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23T09:15:30Z', ' 2023-10-22T14:45:12Z', ' 2023-10-21T21:30:00Z', ' 2023-10-20T12:15:45Z', ', '2023-10-19T08:30:15Z', ' 2023-10-18T17:00:00Z', ' 2023-10-17T10:45:30Z', ' 2023-10-16T15:15:15Z', ', '2023-10-15T22:00:00Z', ' 2023-10-14T11:30:45Z', ' 2023-10-13T06:45:15Z', ' 2023-10-12T19:00:00Z', ', '2023-10-11T13:15:30Z', ' 2023-10-10T07:45:12Z', ' 2023-10-09T20:30:00Z', ' 2023-10-08T11:15:45Z', ', '2023-10-07T05:00:15Z', ' 2023-10-06T18:30:00Z', ' 2023-10-05T12:45:30Z', ' 2023-10-04T09:15:15Z', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板使用统计表.更新时间 <DateTimeField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '更新时间':
        
        # 载入配置成功
        # 给出一些消息模板使用统计表表中更新时间的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '2023-10-23 09:00:00', ' 2023-10-23 10:15:30', ' 2023-10-23 11:30:45', ' 2023-10-23 12:45:15', ', '2023-10-23 14:00:00', ' 2023-10-23 15:15:30', ' 2023-10-23 16:30:45', ' 2023-10-23 17:45:15', ', '2023-10-24 08:00:00', ' 2023-10-24 09:15:30', ' 2023-10-24 10:30:45', ' 2023-10-24 11:45:15', ', '2023-10-24 13:00:00', ' 2023-10-24 14:15:30', ' 2023-10-24 15:30:45', ' 2023-10-24 16:45:15', ', '2023-10-25 07:00:00', ' 2023-10-25 08:15:30', ' 2023-10-25 09:30:45', '
    ))

        val = loadvalue
        
        return val
    
    # 消息模板使用统计表.使用平台 <CharField>
    # 
    if mcfieldnamezh == '使用平台':
        
        # 给出一些消息模板使用统计表表中使用平台的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = ''
        val = loadvalue
        
        return val
    
    # 消息模板使用统计表.用户ID <UUIDField>
    # -----------------------------SKIP---------------------------
    if mcfieldnamezh == '用户ID':
        
        # 如果是图片，文件，UUID，URL，不需要生成
        val = faker.url()
        
        return val
    
    # 消息模板使用统计表.状态 <CharField>
    # 
    if mcfieldnamezh == '状态':
        
        # 载入配置成功
        # 给出一些消息模板使用统计表表中状态的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '待处理', '已处理', '处理中', '已完成', '已取消', '待审核', '审核通过', '审核失败', '待发货', '已发货', '运输中', '已签收', '退货中', '已退货', '退款中', '已退款', '待支付', '已支付', '支付失败', '未知状态', '
    ))

        val = loadvalue
        
        return val
    
    
    # 系统管理员
    
    # 系统管理员.管理员姓名 <CharField>
    # 
    if mcfieldnamezh == '管理员姓名':
        
        # 载入配置成功
        # 给出一些系统管理员表中管理员姓名的示例,要求用单引号包起来用逗号结尾放在一行,不少于20个
        loadvalue = faker.random.choice((
    '管理员姓名1', ' 管理员姓名2', ', '管理员姓名示例1', ' 管理员姓名2', '
    ))

        val = loadvalue
        
        return val
    
    
    return val




# 用户信息表
def generate_userinfo(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='userinfo'
    fields_en = ['`userid`', '`username`', '`pkwkwasswkwkwordhkwkwash`', '`email`', '`phonenumber`', '`regkwkwistertime`', '`lkwkwastlogkwkwintime`', '`status`', '`avatarurl`', '`roleid`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 用户ID唯一标识 根据名称选择合适的函数来生成数据
        userid = get(faker,'用户ID唯一标识')
        values.append('\''+str(userid)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户名用户登录名或昵称 根据名称选择合适的函数来生成数据
        username = get(faker,'用户名用户登录名或昵称')
        values.append('\''+str(username)+'\'')
        
        # 用于外键补充
        
        
        
        # 密码哈希存储加密后的密码 根据名称选择合适的函数来生成数据
        pkwkwasswkwkwordhkwkwash = get(faker,'密码哈希存储加密后的密码')
        values.append('\''+str(pkwkwasswkwkwordhkwkwash)+'\'')
        
        # 用于外键补充
        
        
        
        # 电子邮件用户邮箱地址 根据名称选择合适的函数来生成数据
        email = get(faker,'电子邮件用户邮箱地址')
        values.append('\''+str(email)+'\'')
        
        # 用于外键补充
        
        
        
        # 手机号码用户联系电话 根据名称选择合适的函数来生成数据
        phonenumber = get(faker,'手机号码用户联系电话')
        values.append('\''+str(phonenumber)+'\'')
        
        # 用于外键补充
        
        
        
        # 注册时间用户注册时的日期和时间 根据名称选择合适的函数来生成数据
        regkwkwistertime = get(faker,'注册时间用户注册时的日期和时间')
        values.append('\''+str(regkwkwistertime)+'\'')
        
        # 用于外键补充
        
        
        
        # 最后登录时间用户最后一次登录的日期和时间 根据名称选择合适的函数来生成数据
        lkwkwastlogkwkwintime = get(faker,'最后登录时间用户最后一次登录的日期和时间')
        values.append('\''+str(lkwkwastlogkwkwintime)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户状态如活跃、禁用等 根据名称选择合适的函数来生成数据
        status = get(faker,'用户状态如活跃、禁用等')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        
        # 头像URL用户头像图片的存储地址 根据名称选择合适的函数来生成数据
        avatarurl = get(faker,'头像URL用户头像图片的存储地址')
        values.append('\''+str(avatarurl)+'\'')
        
        # 用于外键补充
        
        
        
        if '角色ID关联到角色的ID示用户所属的角色' not in cache:
            roleid = get(faker,'角色ID关联到角色的ID示用户所属的角色')
        else:
            roleid = faker.random.choice(list(cache.get('角色ID关联到角色的ID示用户所属的角色', )))
        
        # 用于外键补充
        
        if '角色ID关联到角色的ID示用户所属的角色' not in cache:
            cache['角色ID关联到角色的ID示用户所属的角色'] = set()
        cache['角色ID关联到角色的ID示用户所属的角色'].add(roleid)
        values.append('\''+str(roleid)+'\'')
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 平台账号表
def generate_platkwkwfkwkwormaccount(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='platkwkwfkwkwormaccount'
    fields_en = ['`platkwkwfkwkwormid`', '`accountname`', '`accounttype`', '`platkwkwfkwkwormname`', '`username`', '`pkwkwasswkwkword`', '`accesstoken`', '`status`', '`lkwkwastlogkwkwintime`', '`createdat`', '`updatedat`', '`kwkwassociateduserid`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 平台ID 根据名称选择合适的函数来生成数据
        platkwkwfkwkwormid = get(faker,'平台ID')
        values.append('\''+str(platkwkwfkwkwormid)+'\'')
        
        # 用于外键补充
        
        
        
        # 账号名称 根据名称选择合适的函数来生成数据
        accountname = get(faker,'账号名称')
        values.append('\''+str(accountname)+'\'')
        
        # 用于外键补充
        
        
        
        # 账号类型 根据名称选择合适的函数来生成数据
        accounttype = get(faker,'账号类型')
        values.append('\''+str(accounttype)+'\'')
        
        # 用于外键补充
        
        
        
        # 所属平台名称 根据名称选择合适的函数来生成数据
        platkwkwfkwkwormname = get(faker,'所属平台名称')
        values.append('\''+str(platkwkwfkwkwormname)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户名 根据名称选择合适的函数来生成数据
        username = get(faker,'用户名')
        values.append('\''+str(username)+'\'')
        
        # 用于外键补充
        
        
        
        # 密码加密存储 根据名称选择合适的函数来生成数据
        pkwkwasswkwkword = get(faker,'密码加密存储')
        values.append('\''+str(pkwkwasswkwkword)+'\'')
        
        # 用于外键补充
        
        
        
        # 访问令牌 根据名称选择合适的函数来生成数据
        accesstoken = get(faker,'访问令牌')
        values.append('\''+str(accesstoken)+'\'')
        
        # 用于外键补充
        
        
        
        # 账号状态如启用、禁用 根据名称选择合适的函数来生成数据
        status = get(faker,'账号状态如启用、禁用')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        
        # 最后登录时间 根据名称选择合适的函数来生成数据
        lkwkwastlogkwkwintime = get(faker,'最后登录时间')
        values.append('\''+str(lkwkwastlogkwkwintime)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatedat = get(faker,'更新时间')
        values.append('\''+str(updatedat)+'\'')
        
        # 用于外键补充
        
        
        
        if '关联用户ID如果有用户与账号关联' not in cache:
            kwkwassociateduserid = get(faker,'关联用户ID如果有用户与账号关联')
        else:
            kwkwassociateduserid = faker.random.choice(list(cache.get('关联用户ID如果有用户与账号关联', )))
        
        # 用于外键补充
        
        if '关联用户ID如果有用户与账号关联' not in cache:
            cache['关联用户ID如果有用户与账号关联'] = set()
        cache['关联用户ID如果有用户与账号关联'].add(kwkwassociateduserid)
        values.append('\''+str(kwkwassociateduserid)+'\'')
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 私信模板表
def generate_messagetemplate(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagetemplate'
    fields_en = ['`templateid`', '`templatename`', '`templatecontent`', '`creatkwkworid`', '`createtime`', '`updatetime`', '`kwkwisactive`', '`platkwkwfkwkwormtype`', '`targetuserid`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 模板ID 根据名称选择合适的函数来生成数据
        templateid = get(faker,'模板ID')
        values.append('\''+str(templateid)+'\'')
        
        # 用于外键补充
        
        
        
        # 模板名称 根据名称选择合适的函数来生成数据
        templatename = get(faker,'模板名称')
        values.append('\''+str(templatename)+'\'')
        
        # 用于外键补充
        
        
        
        # 模板内容 根据名称选择合适的函数来生成数据
        templatecontent = get(faker,'模板内容')
        values.append('\''+str(templatecontent)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建者ID 根据名称选择合适的函数来生成数据
        creatkwkworid = get(faker,'创建者ID')
        values.append('\''+str(creatkwkworid)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createtime = get(faker,'创建时间')
        values.append('\''+str(createtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatetime = get(faker,'更新时间')
        values.append('\''+str(updatetime)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否激活 根据名称选择合适的函数来生成数据
        kwkwisactive = get(faker,'是否激活')
        values.append('\''+str(kwkwisactive)+'\'')
        
        # 用于外键补充
        
        
        
        # 平台类型 根据名称选择合适的函数来生成数据
        platkwkwfkwkwormtype = get(faker,'平台类型')
        values.append('\''+str(platkwkwfkwkwormtype)+'\'')
        
        # 用于外键补充
        
        
        
        # 目标用户ID可选用于指定特定用户 根据名称选择合适的函数来生成数据
        targetuserid = get(faker,'目标用户ID可选用于指定特定用户')
        values.append('\''+str(targetuserid)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 任务管理表
def generate_tkwkwaskmanagement(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='tkwkwaskmanagement'
    fields_en = ['`tkwkwaskid`', '`tkwkwaskname`', '`platkwkwfkwkworm`', '`targetuserid`', '`messagecontent`', '`scheduledtime`', '`status`', '`createdtime`', '`updatedtime`', '`kwkwassociateduserid`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 任务ID 根据名称选择合适的函数来生成数据
        tkwkwaskid = get(faker,'任务ID')
        values.append('\''+str(tkwkwaskid)+'\'')
        
        # 用于外键补充
        
        
        
        # 任务名称 根据名称选择合适的函数来生成数据
        tkwkwaskname = get(faker,'任务名称')
        values.append('\''+str(tkwkwaskname)+'\'')
        
        # 用于外键补充
        
        
        
        # 平台 根据名称选择合适的函数来生成数据
        platkwkwfkwkworm = get(faker,'平台')
        values.append('\''+str(platkwkwfkwkworm)+'\'')
        
        # 用于外键补充
        
        
        
        # 目标用户ID 根据名称选择合适的函数来生成数据
        targetuserid = get(faker,'目标用户ID')
        values.append('\''+str(targetuserid)+'\'')
        
        # 用于外键补充
        
        
        
        # 私信内容 根据名称选择合适的函数来生成数据
        messagecontent = get(faker,'私信内容')
        values.append('\''+str(messagecontent)+'\'')
        
        # 用于外键补充
        
        
        
        # 计划执行时间 根据名称选择合适的函数来生成数据
        scheduledtime = get(faker,'计划执行时间')
        values.append('\''+str(scheduledtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 任务状态 根据名称选择合适的函数来生成数据
        status = get(faker,'任务状态')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createdtime = get(faker,'创建时间')
        values.append('\''+str(createdtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatedtime = get(faker,'更新时间')
        values.append('\''+str(updatedtime)+'\'')
        
        # 用于外键补充
        
        
        
        if '关联用户ID如任务创建者' not in cache:
            kwkwassociateduserid = get(faker,'关联用户ID如任务创建者')
        else:
            kwkwassociateduserid = faker.random.choice(list(cache.get('关联用户ID如任务创建者', )))
        
        # 用于外键补充
        
        if '关联用户ID如任务创建者' not in cache:
            cache['关联用户ID如任务创建者'] = set()
        cache['关联用户ID如任务创建者'].add(kwkwassociateduserid)
        values.append('\''+str(kwkwassociateduserid)+'\'')
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 任务执行记录表
def generate_tkwkwaskexecutionreckwkword(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='tkwkwaskexecutionreckwkword'
    fields_en = ['`tkwkwaskid`', '`executiontime`', '`status`', '`userid`', '`platkwkwfkwkworm`', '`messagecontent`', '`recipientid`', '`senderid`', '`tkwkwasktemplateid`', '`errkwkwormessage`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 任务ID 根据名称选择合适的函数来生成数据
        tkwkwaskid = get(faker,'任务ID')
        values.append('\''+str(tkwkwaskid)+'\'')
        
        # 用于外键补充
        
        
        
        # 执行时间 根据名称选择合适的函数来生成数据
        executiontime = get(faker,'执行时间')
        values.append('\''+str(executiontime)+'\'')
        
        # 用于外键补充
        
        
        
        # 执行状态 根据名称选择合适的函数来生成数据
        status = get(faker,'执行状态')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户ID 根据名称选择合适的函数来生成数据
        userid = get(faker,'用户ID')
        values.append('\''+str(userid)+'\'')
        
        # 用于外键补充
        
        
        
        # 平台 根据名称选择合适的函数来生成数据
        platkwkwfkwkworm = get(faker,'平台')
        values.append('\''+str(platkwkwfkwkworm)+'\'')
        
        # 用于外键补充
        
        
        
        # 私信内容 根据名称选择合适的函数来生成数据
        messagecontent = get(faker,'私信内容')
        values.append('\''+str(messagecontent)+'\'')
        
        # 用于外键补充
        
        
        
        # 接收者ID 根据名称选择合适的函数来生成数据
        recipientid = get(faker,'接收者ID')
        values.append('\''+str(recipientid)+'\'')
        
        # 用于外键补充
        
        
        
        # 发送者ID 根据名称选择合适的函数来生成数据
        senderid = get(faker,'发送者ID')
        values.append('\''+str(senderid)+'\'')
        
        # 用于外键补充
        
        
        
        # 任务模板ID 根据名称选择合适的函数来生成数据
        tkwkwasktemplateid = get(faker,'任务模板ID')
        values.append('\''+str(tkwkwasktemplateid)+'\'')
        
        # 用于外键补充
        
        
        
        # 错误信息 根据名称选择合适的函数来生成数据
        errkwkwormessage = get(faker,'错误信息')
        values.append('\''+str(errkwkwormessage)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 任务状态表
def generate_tkwkwaskstatus(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='tkwkwaskstatus'
    fields_en = ['`tkwkwaskid`', '`statuscode`', '`statusname`', '`createdat`', '`updatedat`', '`completedat`', '`userid`', '`platkwkwfkwkwormid`', '`messagecontent`', '`kwkwisactive`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 任务ID 根据名称选择合适的函数来生成数据
        tkwkwaskid = get(faker,'任务ID')
        values.append('\''+str(tkwkwaskid)+'\'')
        
        # 用于外键补充
        
        
        
        # 状态码 根据名称选择合适的函数来生成数据
        statuscode = get(faker,'状态码')
        values.append('\''+str(statuscode)+'\'')
        
        # 用于外键补充
        
        
        
        # 状态名称 根据名称选择合适的函数来生成数据
        statusname = get(faker,'状态名称')
        values.append('\''+str(statusname)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatedat = get(faker,'更新时间')
        values.append('\''+str(updatedat)+'\'')
        
        # 用于外键补充
        
        
        
        # 完成时间 根据名称选择合适的函数来生成数据
        completedat = get(faker,'完成时间')
        values.append('\''+str(completedat)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户ID 根据名称选择合适的函数来生成数据
        userid = get(faker,'用户ID')
        values.append('\''+str(userid)+'\'')
        
        # 用于外键补充
        
        
        
        # 平台ID 根据名称选择合适的函数来生成数据
        platkwkwfkwkwormid = get(faker,'平台ID')
        values.append('\''+str(platkwkwfkwkwormid)+'\'')
        
        # 用于外键补充
        
        
        
        # 私信内容 根据名称选择合适的函数来生成数据
        messagecontent = get(faker,'私信内容')
        values.append('\''+str(messagecontent)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否激活 根据名称选择合适的函数来生成数据
        kwkwisactive = get(faker,'是否激活')
        values.append('\''+str(kwkwisactive)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 定时任务表
def generate_scheduledtkwkwask(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='scheduledtkwkwask'
    fields_en = ['`tkwkwaskid`', '`tkwkwaskname`', '`targetplatkwkwfkwkworm`', '`scheduletime`', '`executestatus`', '`lkwkwasterrkwkwor`', '`creatkwkwor`', '`createtime`', '`updatetime`', '`relateduserid`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 任务ID 根据名称选择合适的函数来生成数据
        tkwkwaskid = get(faker,'任务ID')
        values.append('\''+str(tkwkwaskid)+'\'')
        
        # 用于外键补充
        
        
        
        # 任务名称 根据名称选择合适的函数来生成数据
        tkwkwaskname = get(faker,'任务名称')
        values.append('\''+str(tkwkwaskname)+'\'')
        
        # 用于外键补充
        
        
        
        # 目标平台 根据名称选择合适的函数来生成数据
        targetplatkwkwfkwkworm = get(faker,'目标平台')
        values.append('\''+str(targetplatkwkwfkwkworm)+'\'')
        
        # 用于外键补充
        
        
        
        # 计划执行时间 根据名称选择合适的函数来生成数据
        scheduletime = get(faker,'计划执行时间')
        values.append('\''+str(scheduletime)+'\'')
        
        # 用于外键补充
        
        
        
        # 执行状态 根据名称选择合适的函数来生成数据
        executestatus = get(faker,'执行状态')
        values.append('\''+str(executestatus)+'\'')
        
        # 用于外键补充
        
        
        
        # 最近一次错误信息 根据名称选择合适的函数来生成数据
        lkwkwasterrkwkwor = get(faker,'最近一次错误信息')
        values.append('\''+str(lkwkwasterrkwkwor)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建者 根据名称选择合适的函数来生成数据
        creatkwkwor = get(faker,'创建者')
        values.append('\''+str(creatkwkwor)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createtime = get(faker,'创建时间')
        values.append('\''+str(createtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatetime = get(faker,'更新时间')
        values.append('\''+str(updatetime)+'\'')
        
        # 用于外键补充
        
        
        
        if '关联用户ID' not in cache:
            relateduserid = get(faker,'关联用户ID')
        else:
            relateduserid = faker.random.choice(list(cache.get('关联用户ID', )))
        
        # 用于外键补充
        
        if '关联用户ID' not in cache:
            cache['关联用户ID'] = set()
        cache['关联用户ID'].add(relateduserid)
        values.append('\''+str(relateduserid)+'\'')
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息发送记录表
def generate_messagesendreckwkword(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagesendreckwkword'
    fields_en = ['`id`', '`platkwkwfkwkwormid`', '`userid`', '`targetuserid`', '`messagecontent`', '`sendtime`', '`status`', '`rekwkwtrycount`', '`lkwkwastrekwkwtrytime`', '`errkwkwormessage`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        if '平台ID关联字段指向不同社交媒体或消息平台的ID' not in cache:
            platkwkwfkwkwormid = get(faker,'平台ID关联字段指向不同社交媒体或消息平台的ID')
        else:
            platkwkwfkwkwormid = faker.random.choice(list(cache.get('平台ID关联字段指向不同社交媒体或消息平台的ID', )))
        
        # 用于外键补充
        
        if '平台ID关联字段指向不同社交媒体或消息平台的ID' not in cache:
            cache['平台ID关联字段指向不同社交媒体或消息平台的ID'] = set()
        cache['平台ID关联字段指向不同社交媒体或消息平台的ID'].add(platkwkwfkwkwormid)
        values.append('\''+str(platkwkwfkwkwormid)+'\'')
        
        
        
        if '用户ID关联字段指向系统中用户的ID' not in cache:
            userid = get(faker,'用户ID关联字段指向系统中用户的ID')
        else:
            userid = faker.random.choice(list(cache.get('用户ID关联字段指向系统中用户的ID', )))
        
        # 用于外键补充
        
        if '用户ID关联字段指向系统中用户的ID' not in cache:
            cache['用户ID关联字段指向系统中用户的ID'] = set()
        cache['用户ID关联字段指向系统中用户的ID'].add(userid)
        values.append('\''+str(userid)+'\'')
        
        
        
        # 目标用户ID如果是私信则为目标接收者的ID 根据名称选择合适的函数来生成数据
        targetuserid = get(faker,'目标用户ID如果是私信则为目标接收者的ID')
        values.append('\''+str(targetuserid)+'\'')
        
        # 用于外键补充
        
        
        
        # 消息内容 根据名称选择合适的函数来生成数据
        messagecontent = get(faker,'消息内容')
        values.append('\''+str(messagecontent)+'\'')
        
        # 用于外键补充
        
        
        
        # 发送时间 根据名称选择合适的函数来生成数据
        sendtime = get(faker,'发送时间')
        values.append('\''+str(sendtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 发送状态如待发送、发送中、已发送、发送失败 根据名称选择合适的函数来生成数据
        status = get(faker,'发送状态如待发送、发送中、已发送、发送失败')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        
        # 重试次数记录消息发送失败后的重试次数 根据名称选择合适的函数来生成数据
        rekwkwtrycount = get(faker,'重试次数记录消息发送失败后的重试次数')
        values.append('\''+str(rekwkwtrycount)+'\'')
        
        # 用于外键补充
        
        
        
        # 上次重试时间记录最后一次尝试发送的时间 根据名称选择合适的函数来生成数据
        lkwkwastrekwkwtrytime = get(faker,'上次重试时间记录最后一次尝试发送的时间')
        values.append('\''+str(lkwkwastrekwkwtrytime)+'\'')
        
        # 用于外键补充
        
        
        
        # 错误信息如果发送失败记录失败的具体原因 根据名称选择合适的函数来生成数据
        errkwkwormessage = get(faker,'错误信息如果发送失败记录失败的具体原因')
        values.append('\''+str(errkwkwormessage)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息接收记录表
def generate_messagereceivereckwkword(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagereceivereckwkword'
    fields_en = ['`id`', '`userid`', '`platkwkwfkwkwormid`', '`messagecontent`', '`receivetime`', '`status`', '`responsecontent`', '`responsetime`', '`kwkwisread`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        if '用户ID关联用户' not in cache:
            userid = get(faker,'用户ID关联用户')
        else:
            userid = faker.random.choice(list(cache.get('用户ID关联用户', )))
        
        # 用于外键补充
        
        if '用户ID关联用户' not in cache:
            cache['用户ID关联用户'] = set()
        cache['用户ID关联用户'].add(userid)
        values.append('\''+str(userid)+'\'')
        
        
        
        if '平台ID关联平台' not in cache:
            platkwkwfkwkwormid = get(faker,'平台ID关联平台')
        else:
            platkwkwfkwkwormid = faker.random.choice(list(cache.get('平台ID关联平台', )))
        
        # 用于外键补充
        
        if '平台ID关联平台' not in cache:
            cache['平台ID关联平台'] = set()
        cache['平台ID关联平台'].add(platkwkwfkwkwormid)
        values.append('\''+str(platkwkwfkwkwormid)+'\'')
        
        
        
        # 消息内容 根据名称选择合适的函数来生成数据
        messagecontent = get(faker,'消息内容')
        values.append('\''+str(messagecontent)+'\'')
        
        # 用于外键补充
        
        
        
        # 接收时间 根据名称选择合适的函数来生成数据
        receivetime = get(faker,'接收时间')
        values.append('\''+str(receivetime)+'\'')
        
        # 用于外键补充
        
        
        
        # 接收状态如已接收、未处理、已处理等 根据名称选择合适的函数来生成数据
        status = get(faker,'接收状态如已接收、未处理、已处理等')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        
        # 回复内容 根据名称选择合适的函数来生成数据
        responsecontent = get(faker,'回复内容')
        values.append('\''+str(responsecontent)+'\'')
        
        # 用于外键补充
        
        
        
        # 回复时间 根据名称选择合适的函数来生成数据
        responsetime = get(faker,'回复时间')
        values.append('\''+str(responsetime)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否已读示用户是否已读该消息 根据名称选择合适的函数来生成数据
        kwkwisread = get(faker,'是否已读示用户是否已读该消息')
        values.append('\''+str(kwkwisread)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 用户偏好设置表
def generate_userpreference(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='userpreference'
    fields_en = ['`userid`', '`preferencename`', '`preferencevalue`', '`preferencetype`', '`createtime`', '`updatetime`', '`kwkwisactive`', '`description`', '`platkwkwfkwkwormid`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 用户ID 根据名称选择合适的函数来生成数据
        userid = get(faker,'用户ID')
        values.append('\''+str(userid)+'\'')
        
        # 用于外键补充
        
        
        
        # 偏好名称 根据名称选择合适的函数来生成数据
        preferencename = get(faker,'偏好名称')
        values.append('\''+str(preferencename)+'\'')
        
        # 用于外键补充
        
        
        
        # 偏好值 根据名称选择合适的函数来生成数据
        preferencevalue = get(faker,'偏好值')
        values.append('\''+str(preferencevalue)+'\'')
        
        # 用于外键补充
        
        
        
        # 偏好类型 根据名称选择合适的函数来生成数据
        preferencetype = get(faker,'偏好类型')
        values.append('\''+str(preferencetype)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createtime = get(faker,'创建时间')
        values.append('\''+str(createtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatetime = get(faker,'更新时间')
        values.append('\''+str(updatetime)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否激活 根据名称选择合适的函数来生成数据
        kwkwisactive = get(faker,'是否激活')
        values.append('\''+str(kwkwisactive)+'\'')
        
        # 用于外键补充
        
        
        
        # 偏好描述 根据名称选择合适的函数来生成数据
        description = get(faker,'偏好描述')
        values.append('\''+str(description)+'\'')
        
        # 用于外键补充
        
        
        
        if '关联平台ID' not in cache:
            platkwkwfkwkwormid = get(faker,'关联平台ID')
        else:
            platkwkwfkwkwormid = faker.random.choice(list(cache.get('关联平台ID', )))
        
        # 用于外键补充
        
        if '关联平台ID' not in cache:
            cache['关联平台ID'] = set()
        cache['关联平台ID'].add(platkwkwfkwkwormid)
        values.append('\''+str(platkwkwfkwkwormid)+'\'')
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 账号绑定关系表
def generate_accountbkwkwindkwkwing(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='accountbkwkwindkwkwing'
    fields_en = ['`id`', '`accountid`', '`platkwkwfkwkwormid`', '`bkwkwindkwkwingtype`', '`bkwkwindkwkwingstatus`', '`createdat`', '`updatedat`', '`userid`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        # 账号ID 根据名称选择合适的函数来生成数据
        accountid = get(faker,'账号ID')
        values.append('\''+str(accountid)+'\'')
        
        # 用于外键补充
        
        
        
        # 平台ID 根据名称选择合适的函数来生成数据
        platkwkwfkwkwormid = get(faker,'平台ID')
        values.append('\''+str(platkwkwfkwkwormid)+'\'')
        
        # 用于外键补充
        
        
        
        # 绑定类型 根据名称选择合适的函数来生成数据
        bkwkwindkwkwingtype = get(faker,'绑定类型')
        values.append('\''+str(bkwkwindkwkwingtype)+'\'')
        
        # 用于外键补充
        
        
        
        # 绑定状态 根据名称选择合适的函数来生成数据
        bkwkwindkwkwingstatus = get(faker,'绑定状态')
        values.append('\''+str(bkwkwindkwkwingstatus)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatedat = get(faker,'更新时间')
        values.append('\''+str(updatedat)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户ID 根据名称选择合适的函数来生成数据
        userid = get(faker,'用户ID')
        values.append('\''+str(userid)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息内容审核表
def generate_messagecontentreview(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagecontentreview'
    fields_en = ['`id`', '`content`', '`userid`', '`platkwkwfkwkworm`', '`reviewstatus`', '`reviewtime`', '`reviewerid`', '`rejectionrekwkwason`', '`kwkwissensitive`', '`createdat`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        # 消息内容 根据名称选择合适的函数来生成数据
        content = get(faker,'消息内容')
        values.append('\''+str(content)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户ID 根据名称选择合适的函数来生成数据
        userid = get(faker,'用户ID')
        values.append('\''+str(userid)+'\'')
        
        # 用于外键补充
        
        
        
        # 平台名称 根据名称选择合适的函数来生成数据
        platkwkwfkwkworm = get(faker,'平台名称')
        values.append('\''+str(platkwkwfkwkworm)+'\'')
        
        # 用于外键补充
        
        
        
        # 审核状态 根据名称选择合适的函数来生成数据
        reviewstatus = get(faker,'审核状态')
        values.append('\''+str(reviewstatus)+'\'')
        
        # 用于外键补充
        
        
        
        # 审核时间 根据名称选择合适的函数来生成数据
        reviewtime = get(faker,'审核时间')
        values.append('\''+str(reviewtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 审核员ID 根据名称选择合适的函数来生成数据
        reviewerid = get(faker,'审核员ID')
        values.append('\''+str(reviewerid)+'\'')
        
        # 用于外键补充
        
        
        
        # 拒绝原因 根据名称选择合适的函数来生成数据
        rejectionrekwkwason = get(faker,'拒绝原因')
        values.append('\''+str(rejectionrekwkwason)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否敏感内容 根据名称选择合适的函数来生成数据
        kwkwissensitive = get(faker,'是否敏感内容')
        values.append('\''+str(kwkwissensitive)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息发送失败日志表
def generate_messagesendfailurelog(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagesendfailurelog'
    fields_en = ['`id`', '`messageid`', '`platkwkwfkwkworm`', '`userid`', '`targetuserid`', '`sendtime`', '`failurerekwkwason`', '`rekwkwtrycount`', '`lkwkwastrekwkwtrytime`', '`kwkwisresolved`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        # 消息ID 根据名称选择合适的函数来生成数据
        messageid = get(faker,'消息ID')
        values.append('\''+str(messageid)+'\'')
        
        # 用于外键补充
        
        
        
        # 平台名称 根据名称选择合适的函数来生成数据
        platkwkwfkwkworm = get(faker,'平台名称')
        values.append('\''+str(platkwkwfkwkworm)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户ID 根据名称选择合适的函数来生成数据
        userid = get(faker,'用户ID')
        values.append('\''+str(userid)+'\'')
        
        # 用于外键补充
        
        
        
        # 目标用户ID 根据名称选择合适的函数来生成数据
        targetuserid = get(faker,'目标用户ID')
        values.append('\''+str(targetuserid)+'\'')
        
        # 用于外键补充
        
        
        
        # 发送时间 根据名称选择合适的函数来生成数据
        sendtime = get(faker,'发送时间')
        values.append('\''+str(sendtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 失败原因 根据名称选择合适的函数来生成数据
        failurerekwkwason = get(faker,'失败原因')
        values.append('\''+str(failurerekwkwason)+'\'')
        
        # 用于外键补充
        
        
        
        # 重试次数 根据名称选择合适的函数来生成数据
        rekwkwtrycount = get(faker,'重试次数')
        values.append('\''+str(rekwkwtrycount)+'\'')
        
        # 用于外键补充
        
        
        
        # 上次重试时间 根据名称选择合适的函数来生成数据
        lkwkwastrekwkwtrytime = get(faker,'上次重试时间')
        values.append('\''+str(lkwkwastrekwkwtrytime)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否已解决 根据名称选择合适的函数来生成数据
        kwkwisresolved = get(faker,'是否已解决')
        values.append('\''+str(kwkwisresolved)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息发送成功日志表
def generate_messagesendsuccesslog(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagesendsuccesslog'
    fields_en = ['`messageid`', '`platkwkwfkwkworm`', '`userid`', '`receiverid`', '`sendtime`', '`content`', '`status`', '`errkwkworkwkwinfo`', '`relatedtkwkwaskid`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 消息ID 根据名称选择合适的函数来生成数据
        messageid = get(faker,'消息ID')
        values.append('\''+str(messageid)+'\'')
        
        # 用于外键补充
        
        
        
        # 平台名称 根据名称选择合适的函数来生成数据
        platkwkwfkwkworm = get(faker,'平台名称')
        values.append('\''+str(platkwkwfkwkworm)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户ID 根据名称选择合适的函数来生成数据
        userid = get(faker,'用户ID')
        values.append('\''+str(userid)+'\'')
        
        # 用于外键补充
        
        
        
        # 接收者ID 根据名称选择合适的函数来生成数据
        receiverid = get(faker,'接收者ID')
        values.append('\''+str(receiverid)+'\'')
        
        # 用于外键补充
        
        
        
        # 发送时间 根据名称选择合适的函数来生成数据
        sendtime = get(faker,'发送时间')
        values.append('\''+str(sendtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 发送内容 根据名称选择合适的函数来生成数据
        content = get(faker,'发送内容')
        values.append('\''+str(content)+'\'')
        
        # 用于外键补充
        
        
        
        # 发送状态 根据名称选择合适的函数来生成数据
        status = get(faker,'发送状态')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        
        # 错误信息 根据名称选择合适的函数来生成数据
        errkwkworkwkwinfo = get(faker,'错误信息')
        values.append('\''+str(errkwkworkwkwinfo)+'\'')
        
        # 用于外键补充
        
        
        
        if '关联任务ID' not in cache:
            relatedtkwkwaskid = get(faker,'关联任务ID')
        else:
            relatedtkwkwaskid = faker.random.choice(list(cache.get('关联任务ID', )))
        
        # 用于外键补充
        
        if '关联任务ID' not in cache:
            cache['关联任务ID'] = set()
        cache['关联任务ID'].add(relatedtkwkwaskid)
        values.append('\''+str(relatedtkwkwaskid)+'\'')
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息模板分类表
def generate_messagetemplatecategkwkwory(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagetemplatecategkwkwory'
    fields_en = ['`id`', '`name`', '`description`', '`createdat`', '`updatedat`', '`kwkwisactive`', '`parentid`', '`skwkwortkwkworder`', '`templatecount`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        # 分类名称 根据名称选择合适的函数来生成数据
        name = get(faker,'分类名称')
        values.append('\''+str(name)+'\'')
        
        # 用于外键补充
        
        
        
        # 分类描述 根据名称选择合适的函数来生成数据
        description = get(faker,'分类描述')
        values.append('\''+str(description)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatedat = get(faker,'更新时间')
        values.append('\''+str(updatedat)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否激活用于控制分类是否可用 根据名称选择合适的函数来生成数据
        kwkwisactive = get(faker,'是否激活用于控制分类是否可用')
        values.append('\''+str(kwkwisactive)+'\'')
        
        # 用于外键补充
        
        
        
        # 父级分类ID用于构建分类层级结构 根据名称选择合适的函数来生成数据
        parentid = get(faker,'父级分类ID用于构建分类层级结构')
        values.append('\''+str(parentid)+'\'')
        
        # 用于外键补充
        
        
        
        # 排序顺序用于控制分类在列中的显示顺序 根据名称选择合适的函数来生成数据
        skwkwortkwkworder = get(faker,'排序顺序用于控制分类在列中的显示顺序')
        values.append('\''+str(skwkwortkwkworder)+'\'')
        
        # 用于外键补充
        
        
        
        # 模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护 根据名称选择合适的函数来生成数据
        templatecount = get(faker,'模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护')
        values.append('\''+str(templatecount)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息模板标签表
def generate_messagetemplatetag(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagetemplatetag'
    fields_en = ['`id`', '`templateid`', '`tagname`', '`description`', '`createdat`', '`updatedat`', '`kwkwisactive`', '`usagecount`', '`creatkwkworid`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        if '消息模板ID关联字段指向消息模板的ID' not in cache:
            templateid = get(faker,'消息模板ID关联字段指向消息模板的ID')
        else:
            templateid = faker.random.choice(list(cache.get('消息模板ID关联字段指向消息模板的ID', )))
        
        # 用于外键补充
        
        if '消息模板ID关联字段指向消息模板的ID' not in cache:
            cache['消息模板ID关联字段指向消息模板的ID'] = set()
        cache['消息模板ID关联字段指向消息模板的ID'].add(templateid)
        values.append('\''+str(templateid)+'\'')
        
        
        
        # 标签名称 根据名称选择合适的函数来生成数据
        tagname = get(faker,'标签名称')
        values.append('\''+str(tagname)+'\'')
        
        # 用于外键补充
        
        
        
        # 标签描述 根据名称选择合适的函数来生成数据
        description = get(faker,'标签描述')
        values.append('\''+str(description)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatedat = get(faker,'更新时间')
        values.append('\''+str(updatedat)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否激活用于控制标签是否可用 根据名称选择合适的函数来生成数据
        kwkwisactive = get(faker,'是否激活用于控制标签是否可用')
        values.append('\''+str(kwkwisactive)+'\'')
        
        # 用于外键补充
        
        
        
        # 使用次数记录该标签被用于消息模板的次数 根据名称选择合适的函数来生成数据
        usagecount = get(faker,'使用次数记录该标签被用于消息模板的次数')
        values.append('\''+str(usagecount)+'\'')
        
        # 用于外键补充
        
        
        
        if '创建者ID关联字段指向用户的ID' not in cache:
            creatkwkworid = get(faker,'创建者ID关联字段指向用户的ID')
        else:
            creatkwkworid = faker.random.choice(list(cache.get('创建者ID关联字段指向用户的ID', )))
        
        # 用于外键补充
        
        if '创建者ID关联字段指向用户的ID' not in cache:
            cache['创建者ID关联字段指向用户的ID'] = set()
        cache['创建者ID关联字段指向用户的ID'].add(creatkwkworid)
        values.append('\''+str(creatkwkworid)+'\'')
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 用户权限表
def generate_userpermkwkwission(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='userpermkwkwission'
    fields_en = ['`userid`', '`permkwkwissionid`', '`permkwkwissionname`', '`permkwkwissiondescription`', '`createtime`', '`updatetime`', '`isactive`', '`isdeleted`', '`rolename`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 用户ID 根据名称选择合适的函数来生成数据
        userid = get(faker,'用户ID')
        values.append('\''+str(userid)+'\'')
        
        # 用于外键补充
        
        
        
        # 权限ID 根据名称选择合适的函数来生成数据
        permkwkwissionid = get(faker,'权限ID')
        values.append('\''+str(permkwkwissionid)+'\'')
        
        # 用于外键补充
        
        
        
        # 权限名称 根据名称选择合适的函数来生成数据
        permkwkwissionname = get(faker,'权限名称')
        values.append('\''+str(permkwkwissionname)+'\'')
        
        # 用于外键补充
        
        
        
        # 权限描述 根据名称选择合适的函数来生成数据
        permkwkwissiondescription = get(faker,'权限描述')
        values.append('\''+str(permkwkwissiondescription)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createtime = get(faker,'创建时间')
        values.append('\''+str(createtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatetime = get(faker,'更新时间')
        values.append('\''+str(updatetime)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否激活 根据名称选择合适的函数来生成数据
        isactive = get(faker,'是否激活')
        values.append('\''+str(isactive)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否删除 根据名称选择合适的函数来生成数据
        isdeleted = get(faker,'是否删除')
        values.append('\''+str(isdeleted)+'\'')
        
        # 用于外键补充
        
        
        
        if '角色名称关联字段' not in cache:
            rolename = get(faker,'角色名称关联字段')
        else:
            rolename = faker.random.choice(list(cache.get('角色名称关联字段', )))
        
        # 用于外键补充
        
        if '角色名称关联字段' not in cache:
            cache['角色名称关联字段'] = set()
        cache['角色名称关联字段'].add(rolename)
        values.append('\''+str(rolename)+'\'')
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 系统配置表
def generate_systemconfig(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='systemconfig'
    fields_en = ['`id`', '`configname`', '`configvalue`', '`description`', '`createtime`', '`updatetime`', '`kwkwisactive`', '`creatkwkworid`', '`relatedsystemid`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        # 配置名称 根据名称选择合适的函数来生成数据
        configname = get(faker,'配置名称')
        values.append('\''+str(configname)+'\'')
        
        # 用于外键补充
        
        
        
        # 配置值 根据名称选择合适的函数来生成数据
        configvalue = get(faker,'配置值')
        values.append('\''+str(configvalue)+'\'')
        
        # 用于外键补充
        
        
        
        # 配置描述 根据名称选择合适的函数来生成数据
        description = get(faker,'配置描述')
        values.append('\''+str(description)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createtime = get(faker,'创建时间')
        values.append('\''+str(createtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatetime = get(faker,'更新时间')
        values.append('\''+str(updatetime)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否激活1为激活0为未激活 根据名称选择合适的函数来生成数据
        kwkwisactive = get(faker,'是否激活1为激活0为未激活')
        values.append('\''+str(kwkwisactive)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建者ID 根据名称选择合适的函数来生成数据
        creatkwkworid = get(faker,'创建者ID')
        values.append('\''+str(creatkwkworid)+'\'')
        
        # 用于外键补充
        
        
        
        if '关联系统ID' not in cache:
            relatedsystemid = get(faker,'关联系统ID')
        else:
            relatedsystemid = faker.random.choice(list(cache.get('关联系统ID', )))
        
        # 用于外键补充
        
        if '关联系统ID' not in cache:
            cache['关联系统ID'] = set()
        cache['关联系统ID'].add(relatedsystemid)
        values.append('\''+str(relatedsystemid)+'\'')
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 通知推送表
def generate_notkwkwificationpush(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='notkwkwificationpush'
    fields_en = ['`id`', '`platkwkwfkwkwormid`', '`userid`', '`messagecontent`', '`pushstatus`', '`pushtime`', '`rekwkwtrycount`', '`failrekwkwason`', '`createdat`', '`updatedat`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        if '平台ID关联字段指向平台的ID' not in cache:
            platkwkwfkwkwormid = get(faker,'平台ID关联字段指向平台的ID')
        else:
            platkwkwfkwkwormid = faker.random.choice(list(cache.get('平台ID关联字段指向平台的ID', )))
        
        # 用于外键补充
        
        if '平台ID关联字段指向平台的ID' not in cache:
            cache['平台ID关联字段指向平台的ID'] = set()
        cache['平台ID关联字段指向平台的ID'].add(platkwkwfkwkwormid)
        values.append('\''+str(platkwkwfkwkwormid)+'\'')
        
        
        
        if '用户ID关联字段指向用户的ID' not in cache:
            userid = get(faker,'用户ID关联字段指向用户的ID')
        else:
            userid = faker.random.choice(list(cache.get('用户ID关联字段指向用户的ID', )))
        
        # 用于外键补充
        
        if '用户ID关联字段指向用户的ID' not in cache:
            cache['用户ID关联字段指向用户的ID'] = set()
        cache['用户ID关联字段指向用户的ID'].add(userid)
        values.append('\''+str(userid)+'\'')
        
        
        
        # 消息内容 根据名称选择合适的函数来生成数据
        messagecontent = get(faker,'消息内容')
        values.append('\''+str(messagecontent)+'\'')
        
        # 用于外键补充
        
        
        
        # 推送状态例如待推送、已推送、推送失败 根据名称选择合适的函数来生成数据
        pushstatus = get(faker,'推送状态例如待推送、已推送、推送失败')
        values.append('\''+str(pushstatus)+'\'')
        
        # 用于外键补充
        
        
        
        # 推送时间 根据名称选择合适的函数来生成数据
        pushtime = get(faker,'推送时间')
        values.append('\''+str(pushtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 重试次数 根据名称选择合适的函数来生成数据
        rekwkwtrycount = get(faker,'重试次数')
        values.append('\''+str(rekwkwtrycount)+'\'')
        
        # 用于外键补充
        
        
        
        # 失败原因 根据名称选择合适的函数来生成数据
        failrekwkwason = get(faker,'失败原因')
        values.append('\''+str(failrekwkwason)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatedat = get(faker,'更新时间')
        values.append('\''+str(updatedat)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息队列表
def generate_messagequeue(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagequeue'
    fields_en = ['`id`', '`platkwkwfkwkworm`', '`userid`', '`messagecontent`', '`status`', '`createdat`', '`updatedat`', '`rekwkwtrycount`', '`nextrekwkwtrytime`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        # 平台名称记录消息需要发送的平台如微信、微博等 根据名称选择合适的函数来生成数据
        platkwkwfkwkworm = get(faker,'平台名称记录消息需要发送的平台如微信、微博等')
        values.append('\''+str(platkwkwfkwkworm)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户ID接收消息的用户ID用于标识消息接收者 根据名称选择合适的函数来生成数据
        userid = get(faker,'用户ID接收消息的用户ID用于标识消息接收者')
        values.append('\''+str(userid)+'\'')
        
        # 用于外键补充
        
        
        
        # 消息内容需要发送的具体消息内容 根据名称选择合适的函数来生成数据
        messagecontent = get(faker,'消息内容需要发送的具体消息内容')
        values.append('\''+str(messagecontent)+'\'')
        
        # 用于外键补充
        
        
        
        # 消息状态如待发送、发送中、已发送、发送失败等 根据名称选择合适的函数来生成数据
        status = get(faker,'消息状态如待发送、发送中、已发送、发送失败等')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间消息加入队列的时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'创建时间消息加入队列的时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间消息状态最后一次更新的时间 根据名称选择合适的函数来生成数据
        updatedat = get(faker,'更新时间消息状态最后一次更新的时间')
        values.append('\''+str(updatedat)+'\'')
        
        # 用于外键补充
        
        
        
        # 重试次数如果消息发送失败记录重试的次数 根据名称选择合适的函数来生成数据
        rekwkwtrycount = get(faker,'重试次数如果消息发送失败记录重试的次数')
        values.append('\''+str(rekwkwtrycount)+'\'')
        
        # 用于外键补充
        
        
        
        # 下一次重试时间如果消息发送失败记录下一次尝试发送的时间 根据名称选择合适的函数来生成数据
        nextrekwkwtrytime = get(faker,'下一次重试时间如果消息发送失败记录下一次尝试发送的时间')
        values.append('\''+str(nextrekwkwtrytime)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息队列状态表
def generate_messagequeuestatus(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagequeuestatus'
    fields_en = ['`id`', '`platkwkwfkwkwormid`', '`messageid`', '`status`', '`createdat`', '`updatedat`', '`rekwkwtrycount`', '`nextrekwkwtrytime`', '`errkwkwormessage`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        if '平台ID关联字段指向不同平台的唯一标识' not in cache:
            platkwkwfkwkwormid = get(faker,'平台ID关联字段指向不同平台的唯一标识')
        else:
            platkwkwfkwkwormid = faker.random.choice(list(cache.get('平台ID关联字段指向不同平台的唯一标识', )))
        
        # 用于外键补充
        
        if '平台ID关联字段指向不同平台的唯一标识' not in cache:
            cache['平台ID关联字段指向不同平台的唯一标识'] = set()
        cache['平台ID关联字段指向不同平台的唯一标识'].add(platkwkwfkwkwormid)
        values.append('\''+str(platkwkwfkwkwormid)+'\'')
        
        
        
        if '消息ID关联字段指向具体消息的唯一标识' not in cache:
            messageid = get(faker,'消息ID关联字段指向具体消息的唯一标识')
        else:
            messageid = faker.random.choice(list(cache.get('消息ID关联字段指向具体消息的唯一标识', )))
        
        # 用于外键补充
        
        if '消息ID关联字段指向具体消息的唯一标识' not in cache:
            cache['消息ID关联字段指向具体消息的唯一标识'] = set()
        cache['消息ID关联字段指向具体消息的唯一标识'].add(messageid)
        values.append('\''+str(messageid)+'\'')
        
        
        
        # 状态如待发送、发送中、发送成功、发送失败 根据名称选择合适的函数来生成数据
        status = get(faker,'状态如待发送、发送中、发送成功、发送失败')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatedat = get(faker,'更新时间')
        values.append('\''+str(updatedat)+'\'')
        
        # 用于外键补充
        
        
        
        # 重试次数 根据名称选择合适的函数来生成数据
        rekwkwtrycount = get(faker,'重试次数')
        values.append('\''+str(rekwkwtrycount)+'\'')
        
        # 用于外键补充
        
        
        
        # 下一次重试时间 根据名称选择合适的函数来生成数据
        nextrekwkwtrytime = get(faker,'下一次重试时间')
        values.append('\''+str(nextrekwkwtrytime)+'\'')
        
        # 用于外键补充
        
        
        
        # 错误信息如果发送失败记录失败原因 根据名称选择合适的函数来生成数据
        errkwkwormessage = get(faker,'错误信息如果发送失败记录失败原因')
        values.append('\''+str(errkwkwormessage)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息重试记录表
def generate_messagerekwkwtryreckwkword(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagerekwkwtryreckwkword'
    fields_en = ['`messageid`', '`platkwkwfkwkworm`', '`targetuserid`', '`content`', '`rekwkwtrycount`', '`lkwkwastrekwkwtrytime`', '`nextrekwkwtrytime`', '`status`', '`errkwkworkwkwinfo`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        if '消息ID关联消息的ID' not in cache:
            messageid = get(faker,'消息ID关联消息的ID')
        else:
            messageid = faker.random.choice(list(cache.get('消息ID关联消息的ID', )))
        
        # 用于外键补充
        
        if '消息ID关联消息的ID' not in cache:
            cache['消息ID关联消息的ID'] = set()
        cache['消息ID关联消息的ID'].add(messageid)
        values.append('\''+str(messageid)+'\'')
        
        
        
        # 平台名称 根据名称选择合适的函数来生成数据
        platkwkwfkwkworm = get(faker,'平台名称')
        values.append('\''+str(platkwkwfkwkworm)+'\'')
        
        # 用于外键补充
        
        
        
        # 目标用户ID 根据名称选择合适的函数来生成数据
        targetuserid = get(faker,'目标用户ID')
        values.append('\''+str(targetuserid)+'\'')
        
        # 用于外键补充
        
        
        
        # 消息内容 根据名称选择合适的函数来生成数据
        content = get(faker,'消息内容')
        values.append('\''+str(content)+'\'')
        
        # 用于外键补充
        
        
        
        # 重试次数 根据名称选择合适的函数来生成数据
        rekwkwtrycount = get(faker,'重试次数')
        values.append('\''+str(rekwkwtrycount)+'\'')
        
        # 用于外键补充
        
        
        
        # 上次重试时间 根据名称选择合适的函数来生成数据
        lkwkwastrekwkwtrytime = get(faker,'上次重试时间')
        values.append('\''+str(lkwkwastrekwkwtrytime)+'\'')
        
        # 用于外键补充
        
        
        
        # 下一次重试时间 根据名称选择合适的函数来生成数据
        nextrekwkwtrytime = get(faker,'下一次重试时间')
        values.append('\''+str(nextrekwkwtrytime)+'\'')
        
        # 用于外键补充
        
        
        
        # 消息状态如待发送、发送中、发送成功、发送失败 根据名称选择合适的函数来生成数据
        status = get(faker,'消息状态如待发送、发送中、发送成功、发送失败')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        
        # 错误信息如果发送失败记录错误信息 根据名称选择合适的函数来生成数据
        errkwkworkwkwinfo = get(faker,'错误信息如果发送失败记录错误信息')
        values.append('\''+str(errkwkworkwkwinfo)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 账号黑名单表
def generate_accountblacklkwkwist(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='accountblacklkwkwist'
    fields_en = ['`id`', '`accountid`', '`blacklkwkwisttype`', '`rekwkwason`', '`createtime`', '`updatetime`', '`kwkwisactive`', '`creatkwkworid`', '`relatedaccountid`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        # 账号ID 根据名称选择合适的函数来生成数据
        accountid = get(faker,'账号ID')
        values.append('\''+str(accountid)+'\'')
        
        # 用于外键补充
        
        
        
        # 黑名单类型 根据名称选择合适的函数来生成数据
        blacklkwkwisttype = get(faker,'黑名单类型')
        values.append('\''+str(blacklkwkwisttype)+'\'')
        
        # 用于外键补充
        
        
        
        # 加入黑名单原因 根据名称选择合适的函数来生成数据
        rekwkwason = get(faker,'加入黑名单原因')
        values.append('\''+str(rekwkwason)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createtime = get(faker,'创建时间')
        values.append('\''+str(createtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatetime = get(faker,'更新时间')
        values.append('\''+str(updatetime)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否有效用于标记黑名单记录是否仍然有效 根据名称选择合适的函数来生成数据
        kwkwisactive = get(faker,'是否有效用于标记黑名单记录是否仍然有效')
        values.append('\''+str(kwkwisactive)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建者ID 根据名称选择合适的函数来生成数据
        creatkwkworid = get(faker,'创建者ID')
        values.append('\''+str(creatkwkworid)+'\'')
        
        # 用于外键补充
        
        
        
        # 相关账号ID如果黑名单与特定操作或另一账号相关 根据名称选择合适的函数来生成数据
        relatedaccountid = get(faker,'相关账号ID如果黑名单与特定操作或另一账号相关')
        values.append('\''+str(relatedaccountid)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 用户反馈表
def generate_userfeedback(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='userfeedback'
    fields_en = ['`id`', '`userid`', '`feedbackcontent`', '`feedbacktype`', '`createdat`', '`status`', '`responsecontent`', '`responseat`', '`kwkwisresolved`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        if '用户ID关联用户' not in cache:
            userid = get(faker,'用户ID关联用户')
        else:
            userid = faker.random.choice(list(cache.get('用户ID关联用户', )))
        
        # 用于外键补充
        
        if '用户ID关联用户' not in cache:
            cache['用户ID关联用户'] = set()
        cache['用户ID关联用户'].add(userid)
        values.append('\''+str(userid)+'\'')
        
        
        
        # 反馈内容 根据名称选择合适的函数来生成数据
        feedbackcontent = get(faker,'反馈内容')
        values.append('\''+str(feedbackcontent)+'\'')
        
        # 用于外键补充
        
        
        
        # 反馈类型如建议、投诉、咨询等 根据名称选择合适的函数来生成数据
        feedbacktype = get(faker,'反馈类型如建议、投诉、咨询等')
        values.append('\''+str(feedbacktype)+'\'')
        
        # 用于外键补充
        
        
        
        # 反馈创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'反馈创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 反馈状态如待处理、已处理、已忽略等 根据名称选择合适的函数来生成数据
        status = get(faker,'反馈状态如待处理、已处理、已忽略等')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        
        # 回复内容 根据名称选择合适的函数来生成数据
        responsecontent = get(faker,'回复内容')
        values.append('\''+str(responsecontent)+'\'')
        
        # 用于外键补充
        
        
        
        # 回复时间 根据名称选择合适的函数来生成数据
        responseat = get(faker,'回复时间')
        values.append('\''+str(responseat)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否已解决是否 根据名称选择合适的函数来生成数据
        kwkwisresolved = get(faker,'是否已解决是否')
        values.append('\''+str(kwkwisresolved)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 账号安全日志表
def generate_accountsecuritylog(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='accountsecuritylog'
    fields_en = ['`id`', '`accountid`', '`logtype`', '`action`', '`ipaddressip`', '`timestamp`', '`result`', '`description`', '`relatedaccountid`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        # 账号ID 根据名称选择合适的函数来生成数据
        accountid = get(faker,'账号ID')
        values.append('\''+str(accountid)+'\'')
        
        # 用于外键补充
        
        
        
        # 日志类型 根据名称选择合适的函数来生成数据
        logtype = get(faker,'日志类型')
        values.append('\''+str(logtype)+'\'')
        
        # 用于外键补充
        
        
        
        # 动作描述 根据名称选择合适的函数来生成数据
        action = get(faker,'动作描述')
        values.append('\''+str(action)+'\'')
        
        # 用于外键补充
        
        
        
        # 地址 根据名称选择合适的函数来生成数据
        ipaddressip = get(faker,'地址')
        values.append('\''+str(ipaddressip)+'\'')
        
        # 用于外键补充
        
        
        
        # 时间戳 根据名称选择合适的函数来生成数据
        timestamp = get(faker,'时间戳')
        values.append('\''+str(timestamp)+'\'')
        
        # 用于外键补充
        
        
        
        # 结果状态 根据名称选择合适的函数来生成数据
        result = get(faker,'结果状态')
        values.append('\''+str(result)+'\'')
        
        # 用于外键补充
        
        
        
        # 描述信息 根据名称选择合适的函数来生成数据
        description = get(faker,'描述信息')
        values.append('\''+str(description)+'\'')
        
        # 用于外键补充
        
        
        
        if '关联账号ID' not in cache:
            relatedaccountid = get(faker,'关联账号ID')
        else:
            relatedaccountid = faker.random.choice(list(cache.get('关联账号ID', )))
        
        # 用于外键补充
        
        if '关联账号ID' not in cache:
            cache['关联账号ID'] = set()
        cache['关联账号ID'].add(relatedaccountid)
        values.append('\''+str(relatedaccountid)+'\'')
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息模板编辑历史表
def generate_messagetemplateedithkwkwistkwkwory(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagetemplateedithkwkwistkwkwory'
    fields_en = ['`id`', '`templateid`', '`editkwkworid`', '`edittime`', '`editcontent`', '`version`', '`status`', '`remark`', '`kwkwislatest`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        if '消息模板ID关联字段指向消息模板的ID' not in cache:
            templateid = get(faker,'消息模板ID关联字段指向消息模板的ID')
        else:
            templateid = faker.random.choice(list(cache.get('消息模板ID关联字段指向消息模板的ID', )))
        
        # 用于外键补充
        
        if '消息模板ID关联字段指向消息模板的ID' not in cache:
            cache['消息模板ID关联字段指向消息模板的ID'] = set()
        cache['消息模板ID关联字段指向消息模板的ID'].add(templateid)
        values.append('\''+str(templateid)+'\'')
        
        
        
        if '编辑者ID关联字段指向用户的ID' not in cache:
            editkwkworid = get(faker,'编辑者ID关联字段指向用户的ID')
        else:
            editkwkworid = faker.random.choice(list(cache.get('编辑者ID关联字段指向用户的ID', )))
        
        # 用于外键补充
        
        if '编辑者ID关联字段指向用户的ID' not in cache:
            cache['编辑者ID关联字段指向用户的ID'] = set()
        cache['编辑者ID关联字段指向用户的ID'].add(editkwkworid)
        values.append('\''+str(editkwkworid)+'\'')
        
        
        
        # 编辑时间 根据名称选择合适的函数来生成数据
        edittime = get(faker,'编辑时间')
        values.append('\''+str(edittime)+'\'')
        
        # 用于外键补充
        
        
        
        # 编辑内容本次编辑的具体内容或变更 根据名称选择合适的函数来生成数据
        editcontent = get(faker,'编辑内容本次编辑的具体内容或变更')
        values.append('\''+str(editcontent)+'\'')
        
        # 用于外键补充
        
        
        
        # 版本号每次编辑递增 根据名称选择合适的函数来生成数据
        version = get(faker,'版本号每次编辑递增')
        values.append('\''+str(version)+'\'')
        
        # 用于外键补充
        
        
        
        # 状态如有效、已删除等 根据名称选择合适的函数来生成数据
        status = get(faker,'状态如有效、已删除等')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        
        # 备注编辑时的额外说明或备注信息 根据名称选择合适的函数来生成数据
        remark = get(faker,'备注编辑时的额外说明或备注信息')
        values.append('\''+str(remark)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否为最新版本标识当前记录是否为该模板的最新编辑版本 根据名称选择合适的函数来生成数据
        kwkwislatest = get(faker,'是否为最新版本标识当前记录是否为该模板的最新编辑版本')
        values.append('\''+str(kwkwislatest)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息模板审核记录表
def generate_messagetemplatereviewreckwkword(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagetemplatereviewreckwkword'
    fields_en = ['`id`', '`templateid`', '`reviewerid`', '`reviewtime`', '`reviewstatus`', '`reviewcomment`', '`createtime`', '`updatetime`', '`kwkwiskwkwdeleted`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        if '消息模板ID关联消息模板' not in cache:
            templateid = get(faker,'消息模板ID关联消息模板')
        else:
            templateid = faker.random.choice(list(cache.get('消息模板ID关联消息模板', )))
        
        # 用于外键补充
        
        if '消息模板ID关联消息模板' not in cache:
            cache['消息模板ID关联消息模板'] = set()
        cache['消息模板ID关联消息模板'].add(templateid)
        values.append('\''+str(templateid)+'\'')
        
        
        
        if '审核者ID关联用户' not in cache:
            reviewerid = get(faker,'审核者ID关联用户')
        else:
            reviewerid = faker.random.choice(list(cache.get('审核者ID关联用户', )))
        
        # 用于外键补充
        
        if '审核者ID关联用户' not in cache:
            cache['审核者ID关联用户'] = set()
        cache['审核者ID关联用户'].add(reviewerid)
        values.append('\''+str(reviewerid)+'\'')
        
        
        
        # 审核时间 根据名称选择合适的函数来生成数据
        reviewtime = get(faker,'审核时间')
        values.append('\''+str(reviewtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 审核状态如待审核、审核通过、审核拒绝 根据名称选择合适的函数来生成数据
        reviewstatus = get(faker,'审核状态如待审核、审核通过、审核拒绝')
        values.append('\''+str(reviewstatus)+'\'')
        
        # 用于外键补充
        
        
        
        # 审核意见 根据名称选择合适的函数来生成数据
        reviewcomment = get(faker,'审核意见')
        values.append('\''+str(reviewcomment)+'\'')
        
        # 用于外键补充
        
        
        
        # 记录创建时间 根据名称选择合适的函数来生成数据
        createtime = get(faker,'记录创建时间')
        values.append('\''+str(createtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 记录更新时间 根据名称选择合适的函数来生成数据
        updatetime = get(faker,'记录更新时间')
        values.append('\''+str(updatetime)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否删除逻辑删除标记 根据名称选择合适的函数来生成数据
        kwkwiskwkwdeleted = get(faker,'是否删除逻辑删除标记')
        values.append('\''+str(kwkwiskwkwdeleted)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息发送策略表
def generate_messagesendstrategy(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagesendstrategy'
    fields_en = ['`id`', '`name`', '`description`', '`platkwkwfkwkworm`', '`targettype`', '`contenttemplate`', '`scheduletype`', '`starttime`', '`endtime`', '`userid`', '`status`', '`createdat`', '`updatedat`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        # 策略名称 根据名称选择合适的函数来生成数据
        name = get(faker,'策略名称')
        values.append('\''+str(name)+'\'')
        
        # 用于外键补充
        
        
        
        # 策略描述 根据名称选择合适的函数来生成数据
        description = get(faker,'策略描述')
        values.append('\''+str(description)+'\'')
        
        # 用于外键补充
        
        
        
        # 平台类型 根据名称选择合适的函数来生成数据
        platkwkwfkwkworm = get(faker,'平台类型')
        values.append('\''+str(platkwkwfkwkworm)+'\'')
        
        # 用于外键补充
        
        
        
        # 目标类型 根据名称选择合适的函数来生成数据
        targettype = get(faker,'目标类型')
        values.append('\''+str(targettype)+'\'')
        
        # 用于外键补充
        
        
        
        # 内容模板 根据名称选择合适的函数来生成数据
        contenttemplate = get(faker,'内容模板')
        values.append('\''+str(contenttemplate)+'\'')
        
        # 用于外键补充
        
        
        
        # 计划类型如一次性、周期性 根据名称选择合适的函数来生成数据
        scheduletype = get(faker,'计划类型如一次性、周期性')
        values.append('\''+str(scheduletype)+'\'')
        
        # 用于外键补充
        
        
        
        # 开始时间 根据名称选择合适的函数来生成数据
        starttime = get(faker,'开始时间')
        values.append('\''+str(starttime)+'\'')
        
        # 用于外键补充
        
        
        
        # 结束时间 根据名称选择合适的函数来生成数据
        endtime = get(faker,'结束时间')
        values.append('\''+str(endtime)+'\'')
        
        # 用于外键补充
        
        
        
        if '用户ID关联用户' not in cache:
            userid = get(faker,'用户ID关联用户')
        else:
            userid = faker.random.choice(list(cache.get('用户ID关联用户', )))
        
        # 用于外键补充
        
        if '用户ID关联用户' not in cache:
            cache['用户ID关联用户'] = set()
        cache['用户ID关联用户'].add(userid)
        values.append('\''+str(userid)+'\'')
        
        
        
        # 状态如启用、禁用 根据名称选择合适的函数来生成数据
        status = get(faker,'状态如启用、禁用')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatedat = get(faker,'更新时间')
        values.append('\''+str(updatedat)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息发送频率限制表
def generate_messagesendfrequencylimit(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagesendfrequencylimit'
    fields_en = ['`id`', '`platkwkwfkwkwormid`', '`userid`', '`messagetype`', '`maxsendcount`', '`timeperiod`', '`lkwkwastsendtime`', '`resettime`', '`status`', '`kwkwnote`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        if '平台ID关联到不同平台的用于区分不同平台的发送频率限制' not in cache:
            platkwkwfkwkwormid = get(faker,'平台ID关联到不同平台的用于区分不同平台的发送频率限制')
        else:
            platkwkwfkwkwormid = faker.random.choice(list(cache.get('平台ID关联到不同平台的用于区分不同平台的发送频率限制', )))
        
        # 用于外键补充
        
        if '平台ID关联到不同平台的用于区分不同平台的发送频率限制' not in cache:
            cache['平台ID关联到不同平台的用于区分不同平台的发送频率限制'] = set()
        cache['平台ID关联到不同平台的用于区分不同平台的发送频率限制'].add(platkwkwfkwkwormid)
        values.append('\''+str(platkwkwfkwkwormid)+'\'')
        
        
        
        if '用户ID关联到用户示该限制是针对哪个用户的' not in cache:
            userid = get(faker,'用户ID关联到用户示该限制是针对哪个用户的')
        else:
            userid = faker.random.choice(list(cache.get('用户ID关联到用户示该限制是针对哪个用户的', )))
        
        # 用于外键补充
        
        if '用户ID关联到用户示该限制是针对哪个用户的' not in cache:
            cache['用户ID关联到用户示该限制是针对哪个用户的'] = set()
        cache['用户ID关联到用户示该限制是针对哪个用户的'].add(userid)
        values.append('\''+str(userid)+'\'')
        
        
        
        # 消息类型如文本、图片、视频等用于区分不同类型的消息发送频率 根据名称选择合适的函数来生成数据
        messagetype = get(faker,'消息类型如文本、图片、视频等用于区分不同类型的消息发送频率')
        values.append('\''+str(messagetype)+'\'')
        
        # 用于外键补充
        
        
        
        # 最大发送次数在指定时间周期内允许的最大发送次数 根据名称选择合适的函数来生成数据
        maxsendcount = get(faker,'最大发送次数在指定时间周期内允许的最大发送次数')
        values.append('\''+str(maxsendcount)+'\'')
        
        # 用于外键补充
        
        
        
        # 时间周期如每天、每小时等示上述最大发送次数的时间范围 根据名称选择合适的函数来生成数据
        timeperiod = get(faker,'时间周期如每天、每小时等示上述最大发送次数的时间范围')
        values.append('\''+str(timeperiod)+'\'')
        
        # 用于外键补充
        
        
        
        # 上次发送时间记录最后一次发送消息的时间用于计算下一次发送的时间 根据名称选择合适的函数来生成数据
        lkwkwastsendtime = get(faker,'上次发送时间记录最后一次发送消息的时间用于计算下一次发送的时间')
        values.append('\''+str(lkwkwastsendtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 重置时间时间周期的开始时间用于重置发送次数计数器 根据名称选择合适的函数来生成数据
        resettime = get(faker,'重置时间时间周期的开始时间用于重置发送次数计数器')
        values.append('\''+str(resettime)+'\'')
        
        # 用于外键补充
        
        
        
        # 状态如启用、禁用示该频率限制是否生效 根据名称选择合适的函数来生成数据
        status = get(faker,'状态如启用、禁用示该频率限制是否生效')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        
        # 备注用于记录该频率限制的其他相关信息或说明 根据名称选择合适的函数来生成数据
        kwkwnote = get(faker,'备注用于记录该频率限制的其他相关信息或说明')
        values.append('\''+str(kwkwnote)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息发送优先级表
def generate_messagesendprikwkwority(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagesendprikwkwority'
    fields_en = ['`id`', '`prikwkworitylevel`', '`description`', '`createdat`', '`updatedat`', '`kwkwisactive`', '`platkwkwfkwkwormid`', '`messagetypeid`', '`kwkwdefaultkwkwdelay`', '`maxrekwkwtrycount`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        
        # 用于外键补充
        
        
        
        # 优先级等级 根据名称选择合适的函数来生成数据
        prikwkworitylevel = get(faker,'优先级等级')
        values.append('\''+str(prikwkworitylevel)+'\'')
        
        # 用于外键补充
        
        
        
        # 优先级描述 根据名称选择合适的函数来生成数据
        description = get(faker,'优先级描述')
        values.append('\''+str(description)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatedat = get(faker,'更新时间')
        values.append('\''+str(updatedat)+'\'')
        
        # 用于外键补充
        
        
        
        # 是否激活 根据名称选择合适的函数来生成数据
        kwkwisactive = get(faker,'是否激活')
        values.append('\''+str(kwkwisactive)+'\'')
        
        # 用于外键补充
        
        
        
        if '平台ID关联字段指向平台' not in cache:
            platkwkwfkwkwormid = get(faker,'平台ID关联字段指向平台')
        else:
            platkwkwfkwkwormid = faker.random.choice(list(cache.get('平台ID关联字段指向平台', )))
        
        # 用于外键补充
        
        if '平台ID关联字段指向平台' not in cache:
            cache['平台ID关联字段指向平台'] = set()
        cache['平台ID关联字段指向平台'].add(platkwkwfkwkwormid)
        values.append('\''+str(platkwkwfkwkwormid)+'\'')
        
        
        
        if '消息类型ID关联字段指向消息类型' not in cache:
            messagetypeid = get(faker,'消息类型ID关联字段指向消息类型')
        else:
            messagetypeid = faker.random.choice(list(cache.get('消息类型ID关联字段指向消息类型', )))
        
        # 用于外键补充
        
        if '消息类型ID关联字段指向消息类型' not in cache:
            cache['消息类型ID关联字段指向消息类型'] = set()
        cache['消息类型ID关联字段指向消息类型'].add(messagetypeid)
        values.append('\''+str(messagetypeid)+'\'')
        
        
        
        # 默认延迟时间秒 根据名称选择合适的函数来生成数据
        kwkwdefaultkwkwdelay = get(faker,'默认延迟时间秒')
        values.append('\''+str(kwkwdefaultkwkwdelay)+'\'')
        
        # 用于外键补充
        
        
        
        # 最大重试次数 根据名称选择合适的函数来生成数据
        maxrekwkwtrycount = get(faker,'最大重试次数')
        values.append('\''+str(maxrekwkwtrycount)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 消息模板使用统计表
def generate_messagetemplateusagestatkwkwistics(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='messagetemplateusagestatkwkwistics'
    fields_en = ['`templateid`', '`usagecount`', '`lkwkwastusedtime`', '`createdat`', '`updatedat`', '`platkwkwfkwkworm`', '`userid`', '`status`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 消息模板ID 根据名称选择合适的函数来生成数据
        templateid = get(faker,'消息模板ID')
        values.append('\''+str(templateid)+'\'')
        
        # 用于外键补充
        
        
        
        # 使用次数 根据名称选择合适的函数来生成数据
        usagecount = get(faker,'使用次数')
        values.append('\''+str(usagecount)+'\'')
        
        # 用于外键补充
        
        
        
        # 最后使用时间 根据名称选择合适的函数来生成数据
        lkwkwastusedtime = get(faker,'最后使用时间')
        values.append('\''+str(lkwkwastusedtime)+'\'')
        
        # 用于外键补充
        
        
        
        # 创建时间 根据名称选择合适的函数来生成数据
        createdat = get(faker,'创建时间')
        values.append('\''+str(createdat)+'\'')
        
        # 用于外键补充
        
        
        
        # 更新时间 根据名称选择合适的函数来生成数据
        updatedat = get(faker,'更新时间')
        values.append('\''+str(updatedat)+'\'')
        
        # 用于外键补充
        
        
        
        # 使用平台 根据名称选择合适的函数来生成数据
        platkwkwfkwkworm = get(faker,'使用平台')
        values.append('\''+str(platkwkwfkwkworm)+'\'')
        
        # 用于外键补充
        
        
        
        # 用户ID 根据名称选择合适的函数来生成数据
        userid = get(faker,'用户ID')
        values.append('\''+str(userid)+'\'')
        
        # 用于外键补充
        
        
        
        # 状态 根据名称选择合适的函数来生成数据
        status = get(faker,'状态')
        values.append('\''+str(status)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache

# 系统管理员
def generate_supermanager(faker, sql, out, database, cache=None):
    if cache is None:
        cache = dict()
    table='supermanager'
    fields_en = ['`username`']
    if '`id`' in fields_en:
        fields_en.remove('`id`')
    for i in range(100):
        values = list()
        
        
        # 管理员姓名 根据名称选择合适的函数来生成数据
        username = get(faker,'管理员姓名')
        values.append('\''+str(username)+'\'')
        
        # 用于外键补充
        
        
        out.write(sql.format(databasename=database,table=table,fields_en=','.join(fields_en),values=','.join(values)))
    return cache


def generate():
    cache = dict()
    with codecs.open('faker.sql', 'w', encoding='utf-8') as out:
        sql = 'insert into {databasename}.{table} ({fields_en}) values({values});\r\n'
        faker = Faker('zh_CN')
        database = 'vm772_58dd091a279b5392'
        # 表名字符串,字段英文名

            
        # 用户信息表
        cache.update(generate_userinfo(faker, sql, out, database,cache=cache))
        
        # 平台账号表
        cache.update(generate_platkwkwfkwkwormaccount(faker, sql, out, database,cache=cache))
        
        # 私信模板表
        cache.update(generate_messagetemplate(faker, sql, out, database,cache=cache))
        
        # 任务管理表
        cache.update(generate_tkwkwaskmanagement(faker, sql, out, database,cache=cache))
        
        # 任务执行记录表
        cache.update(generate_tkwkwaskexecutionreckwkword(faker, sql, out, database,cache=cache))
        
        # 任务状态表
        cache.update(generate_tkwkwaskstatus(faker, sql, out, database,cache=cache))
        
        # 定时任务表
        cache.update(generate_scheduledtkwkwask(faker, sql, out, database,cache=cache))
        
        # 消息发送记录表
        cache.update(generate_messagesendreckwkword(faker, sql, out, database,cache=cache))
        
        # 消息接收记录表
        cache.update(generate_messagereceivereckwkword(faker, sql, out, database,cache=cache))
        
        # 用户偏好设置表
        cache.update(generate_userpreference(faker, sql, out, database,cache=cache))
        
        # 账号绑定关系表
        cache.update(generate_accountbkwkwindkwkwing(faker, sql, out, database,cache=cache))
        
        # 消息内容审核表
        cache.update(generate_messagecontentreview(faker, sql, out, database,cache=cache))
        
        # 消息发送失败日志表
        cache.update(generate_messagesendfailurelog(faker, sql, out, database,cache=cache))
        
        # 消息发送成功日志表
        cache.update(generate_messagesendsuccesslog(faker, sql, out, database,cache=cache))
        
        # 消息模板分类表
        cache.update(generate_messagetemplatecategkwkwory(faker, sql, out, database,cache=cache))
        
        # 消息模板标签表
        cache.update(generate_messagetemplatetag(faker, sql, out, database,cache=cache))
        
        # 用户权限表
        cache.update(generate_userpermkwkwission(faker, sql, out, database,cache=cache))
        
        # 系统配置表
        cache.update(generate_systemconfig(faker, sql, out, database,cache=cache))
        
        # 通知推送表
        cache.update(generate_notkwkwificationpush(faker, sql, out, database,cache=cache))
        
        # 消息队列表
        cache.update(generate_messagequeue(faker, sql, out, database,cache=cache))
        
        # 消息队列状态表
        cache.update(generate_messagequeuestatus(faker, sql, out, database,cache=cache))
        
        # 消息重试记录表
        cache.update(generate_messagerekwkwtryreckwkword(faker, sql, out, database,cache=cache))
        
        # 账号黑名单表
        cache.update(generate_accountblacklkwkwist(faker, sql, out, database,cache=cache))
        
        # 用户反馈表
        cache.update(generate_userfeedback(faker, sql, out, database,cache=cache))
        
        # 账号安全日志表
        cache.update(generate_accountsecuritylog(faker, sql, out, database,cache=cache))
        
        # 消息模板编辑历史表
        cache.update(generate_messagetemplateedithkwkwistkwkwory(faker, sql, out, database,cache=cache))
        
        # 消息模板审核记录表
        cache.update(generate_messagetemplatereviewreckwkword(faker, sql, out, database,cache=cache))
        
        # 消息发送策略表
        cache.update(generate_messagesendstrategy(faker, sql, out, database,cache=cache))
        
        # 消息发送频率限制表
        cache.update(generate_messagesendfrequencylimit(faker, sql, out, database,cache=cache))
        
        # 消息发送优先级表
        cache.update(generate_messagesendprikwkwority(faker, sql, out, database,cache=cache))
        
        # 消息模板使用统计表
        cache.update(generate_messagetemplateusagestatkwkwistics(faker, sql, out, database,cache=cache))
        
        # 系统管理员
        cache.update(generate_supermanager(faker, sql, out, database,cache=cache))
        

    from pymysql.connections import Connection
    from pymysql.cursors import DictCursor
    conn = Connection(port=3306, host='localhost', user='root', password=os.getenv('PM_UNIT_DATABASE_PSW', '123456'),
                      database='vm772_58dd091a279b5392')
    with codecs.open('faker.sql', 'r', encoding='utf-8') as ins:
        with conn.cursor(DictCursor) as cursor:
            count = 0
            for i, sql in enumerate(ins.readlines()):
                try:
                    cursor.execute(sql)
                    cursor.fetchall()
                except Exception as e:
                    print('error: ', e)
                    print(sql)
                    continue
                count += 1
                    
        conn.commit()
        print('Generate OK,Insert Total:', count, '个记录', i+1, '个sql')
    os.remove('faker.sql')


if __name__ == '__main__':
    generate()

