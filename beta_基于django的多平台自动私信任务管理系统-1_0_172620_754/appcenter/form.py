from django import forms

from captcha.fields import CaptchaField


class mc_userinfo_form(forms.Form):
    """
    # For Table: 用户信息表
    """

    userid = forms.UUIDField(
        label="用户ID唯一标识",
        required=True,
    )

    username = forms.CharField(
        label="用户名用户登录名或昵称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    pkwkwasswkwkwordhkwkwash = forms.CharField(
        label="密码哈希存储加密后的密码",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    email = forms.Textarea()

    phonenumber = forms.CharField(
        label="手机号码用户联系电话",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    regkwkwistertime = forms.DateTimeField(
        label="注册时间用户注册时的日期和时间",
        required=True,
    )

    lkwkwastlogkwkwintime = forms.DateTimeField(
        label="最后登录时间用户最后一次登录的日期和时间",
        required=True,
    )

    status = forms.CharField(
        label="用户状态如活跃、禁用等",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    avatarurl = forms.ImageField(
        label="头像URL用户头像图片的存储地址",
        required=True,
    )

    roleid = forms.Select()

    class Meta:
        pass


class mc_platkwkwfkwkwormaccount_form(forms.Form):
    """
    # For Table: 平台账号表
    """

    platkwkwfkwkwormid = forms.UUIDField(
        label="平台ID",
        required=True,
    )

    accountname = forms.CharField(
        label="账号名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    accounttype = forms.CharField(
        label="账号类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    platkwkwfkwkwormname = forms.CharField(
        label="所属平台名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    pkwkwasswkwkword = forms.CharField(
        label="密码加密存储",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    accesstoken = forms.CharField(
        label="访问令牌",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    status = forms.CharField(
        label="账号状态如启用、禁用",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    lkwkwastlogkwkwintime = forms.DateTimeField(
        label="最后登录时间",
        required=True,
    )

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwassociateduserid = forms.Select()

    class Meta:
        pass


class mc_messagetemplate_form(forms.Form):
    """
    # For Table: 私信模板表
    """

    templateid = forms.UUIDField(
        label="模板ID",
        required=True,
    )

    templatename = forms.CharField(
        label="模板名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    templatecontent = forms.Textarea()

    creatkwkworid = forms.UUIDField(
        label="创建者ID",
        required=True,
    )

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwisactive = forms.BooleanField(
        label="是否激活",
        required=True,
    )

    platkwkwfkwkwormtype = forms.CharField(
        label="平台类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    targetuserid = forms.UUIDField(
        label="目标用户ID可选用于指定特定用户",
        required=True,
    )

    class Meta:
        pass


class mc_tkwkwaskmanagement_form(forms.Form):
    """
    # For Table: 任务管理表
    """

    tkwkwaskid = forms.UUIDField(
        label="任务ID",
        required=True,
    )

    tkwkwaskname = forms.CharField(
        label="任务名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    platkwkwfkwkworm = forms.CharField(
        label="平台",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    targetuserid = forms.UUIDField(
        label="目标用户ID",
        required=True,
    )

    messagecontent = forms.Textarea()

    scheduledtime = forms.DateTimeField(
        label="计划执行时间",
        required=True,
    )

    status = forms.CharField(
        label="任务状态",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createdtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedtime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwassociateduserid = forms.Select()

    class Meta:
        pass


class mc_tkwkwaskexecutionreckwkword_form(forms.Form):
    """
    # For Table: 任务执行记录表
    """

    tkwkwaskid = forms.UUIDField(
        label="任务ID",
        required=True,
    )

    executiontime = forms.DateTimeField(
        label="执行时间",
        required=True,
    )

    status = forms.CharField(
        label="执行状态",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    userid = forms.UUIDField(
        label="用户ID",
        required=True,
    )

    platkwkwfkwkworm = forms.CharField(
        label="平台",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    messagecontent = forms.Textarea()

    recipientid = forms.UUIDField(
        label="接收者ID",
        required=True,
    )

    senderid = forms.UUIDField(
        label="发送者ID",
        required=True,
    )

    tkwkwasktemplateid = forms.UUIDField(
        label="任务模板ID",
        required=True,
    )

    errkwkwormessage = forms.CharField(
        label="错误信息",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_tkwkwaskstatus_form(forms.Form):
    """
    # For Table: 任务状态表
    """

    tkwkwaskid = forms.UUIDField(
        label="任务ID",
        required=True,
    )

    statuscode = forms.CharField(
        label="状态码",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    statusname = forms.CharField(
        label="状态名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    completedat = forms.DateTimeField(
        label="完成时间",
        required=True,
    )

    userid = forms.UUIDField(
        label="用户ID",
        required=True,
    )

    platkwkwfkwkwormid = forms.UUIDField(
        label="平台ID",
        required=True,
    )

    messagecontent = forms.Textarea()

    kwkwisactive = forms.BooleanField(
        label="是否激活",
        required=True,
    )

    class Meta:
        pass


class mc_scheduledtkwkwask_form(forms.Form):
    """
    # For Table: 定时任务表
    """

    tkwkwaskid = forms.UUIDField(
        label="任务ID",
        required=True,
    )

    tkwkwaskname = forms.CharField(
        label="任务名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    targetplatkwkwfkwkworm = forms.CharField(
        label="目标平台",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    scheduletime = forms.DateTimeField(
        label="计划执行时间",
        required=True,
    )

    executestatus = forms.CharField(
        label="执行状态",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    lkwkwasterrkwkwor = forms.CharField(
        label="最近一次错误信息",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    creatkwkwor = forms.CharField(
        label="创建者",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    relateduserid = forms.Select()

    class Meta:
        pass


class mc_messagesendreckwkword_form(forms.Form):
    """
    # For Table: 消息发送记录表
    """

    id = forms.UUIDField(
        label="唯一标识符",
        required=True,
    )

    platkwkwfkwkwormid = forms.Select()

    userid = forms.Select()

    targetuserid = forms.UUIDField(
        label="目标用户ID如果是私信则为目标接收者的ID",
        required=True,
    )

    messagecontent = forms.Textarea()

    sendtime = forms.DateTimeField(
        label="发送时间",
        required=True,
    )

    status = forms.CharField(
        label="发送状态如待发送、发送中、已发送、发送失败",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    rekwkwtrycount = forms.CharField(
        label="重试次数记录消息发送失败后的重试次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    lkwkwastrekwkwtrytime = forms.DateTimeField(
        label="上次重试时间记录最后一次尝试发送的时间",
        required=True,
    )

    errkwkwormessage = forms.CharField(
        label="错误信息如果发送失败记录失败的具体原因",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_messagereceivereckwkword_form(forms.Form):
    """
    # For Table: 消息接收记录表
    """

    id = forms.UUIDField(
        label="唯一标识符",
        required=True,
    )

    userid = forms.Select()

    platkwkwfkwkwormid = forms.Select()

    messagecontent = forms.Textarea()

    receivetime = forms.DateTimeField(
        label="接收时间",
        required=True,
    )

    status = forms.CharField(
        label="接收状态如已接收、未处理、已处理等",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    responsecontent = forms.Textarea()

    responsetime = forms.DateTimeField(
        label="回复时间",
        required=True,
    )

    kwkwisread = forms.BooleanField(
        label="是否已读示用户是否已读该消息",
        required=True,
    )

    class Meta:
        pass


class mc_userpreference_form(forms.Form):
    """
    # For Table: 用户偏好设置表
    """

    userid = forms.UUIDField(
        label="用户ID",
        required=True,
    )

    preferencename = forms.CharField(
        label="偏好名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    preferencevalue = forms.CharField(
        label="偏好值",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    preferencetype = forms.CharField(
        label="偏好类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwisactive = forms.BooleanField(
        label="是否激活",
        required=True,
    )

    description = forms.Textarea()

    platkwkwfkwkwormid = forms.Select()

    class Meta:
        pass


class mc_accountbkwkwindkwkwing_form(forms.Form):
    """
    # For Table: 账号绑定关系表
    """

    id = forms.UUIDField(
        label="唯一标识符",
        required=True,
    )

    accountid = forms.UUIDField(
        label="账号ID",
        required=True,
    )

    platkwkwfkwkwormid = forms.UUIDField(
        label="平台ID",
        required=True,
    )

    bkwkwindkwkwingtype = forms.CharField(
        label="绑定类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    bkwkwindkwkwingstatus = forms.CharField(
        label="绑定状态",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    userid = forms.UUIDField(
        label="用户ID",
        required=True,
    )

    class Meta:
        pass


class mc_messagecontentreview_form(forms.Form):
    """
    # For Table: 消息内容审核表
    """

    id = forms.Textarea()

    content = forms.Textarea()

    userid = forms.UUIDField(
        label="用户ID",
        required=True,
    )

    platkwkwfkwkworm = forms.CharField(
        label="平台名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    reviewstatus = forms.CharField(
        label="审核状态",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    reviewtime = forms.DateTimeField(
        label="审核时间",
        required=True,
    )

    reviewerid = forms.UUIDField(
        label="审核员ID",
        required=True,
    )

    rejectionrekwkwason = forms.CharField(
        label="拒绝原因",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    kwkwissensitive = forms.Textarea()

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    class Meta:
        pass


class mc_messagesendfailurelog_form(forms.Form):
    """
    # For Table: 消息发送失败日志表
    """

    id = forms.UUIDField(
        label="唯一标识符",
        required=True,
    )

    messageid = forms.UUIDField(
        label="消息ID",
        required=True,
    )

    platkwkwfkwkworm = forms.CharField(
        label="平台名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    userid = forms.UUIDField(
        label="用户ID",
        required=True,
    )

    targetuserid = forms.UUIDField(
        label="目标用户ID",
        required=True,
    )

    sendtime = forms.DateTimeField(
        label="发送时间",
        required=True,
    )

    failurerekwkwason = forms.CharField(
        label="失败原因",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    rekwkwtrycount = forms.CharField(
        label="重试次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    lkwkwastrekwkwtrytime = forms.DateTimeField(
        label="上次重试时间",
        required=True,
    )

    kwkwisresolved = forms.BooleanField(
        label="是否已解决",
        required=True,
    )

    class Meta:
        pass


class mc_messagesendsuccesslog_form(forms.Form):
    """
    # For Table: 消息发送成功日志表
    """

    messageid = forms.UUIDField(
        label="消息ID",
        required=True,
    )

    platkwkwfkwkworm = forms.CharField(
        label="平台名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    userid = forms.UUIDField(
        label="用户ID",
        required=True,
    )

    receiverid = forms.UUIDField(
        label="接收者ID",
        required=True,
    )

    sendtime = forms.DateTimeField(
        label="发送时间",
        required=True,
    )

    content = forms.Textarea()

    status = forms.CharField(
        label="发送状态",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    errkwkworkwkwinfo = forms.CharField(
        label="错误信息",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    relatedtkwkwaskid = forms.Select()

    class Meta:
        pass


class mc_messagetemplatecategkwkwory_form(forms.Form):
    """
    # For Table: 消息模板分类表
    """

    id = forms.UUIDField(
        label="唯一标识符",
        required=True,
    )

    name = forms.CharField(
        label="分类名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwisactive = forms.BooleanField(
        label="是否激活用于控制分类是否可用",
        required=True,
    )

    parentid = forms.UUIDField(
        label="父级分类ID用于构建分类层级结构",
        required=True,
    )

    skwkwortkwkworder = forms.CharField(
        label="排序顺序用于控制分类在列中的显示顺序",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    templatecount = forms.IntegerField(
        label="模板数量可选统计属于该分类的消息模板数量可通过触发器或应用逻辑维护",
        required=True,
    )

    class Meta:
        pass


class mc_messagetemplatetag_form(forms.Form):
    """
    # For Table: 消息模板标签表
    """

    id = forms.UUIDField(
        label="唯一标识符",
        required=True,
    )

    templateid = forms.Select()

    tagname = forms.CharField(
        label="标签名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwisactive = forms.BooleanField(
        label="是否激活用于控制标签是否可用",
        required=True,
    )

    usagecount = forms.CharField(
        label="使用次数记录该标签被用于消息模板的次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    creatkwkworid = forms.Select()

    class Meta:
        pass


class mc_userpermkwkwission_form(forms.Form):
    """
    # For Table: 用户权限表
    """

    userid = forms.UUIDField(
        label="用户ID",
        required=True,
    )

    permkwkwissionid = forms.UUIDField(
        label="权限ID",
        required=True,
    )

    permkwkwissionname = forms.CharField(
        label="权限名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    permkwkwissiondescription = forms.Textarea()

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    isactive = forms.BooleanField(
        label="是否激活",
        required=True,
    )

    isdeleted = forms.BooleanField(
        label="是否删除",
        required=True,
    )

    rolename = forms.Select()

    class Meta:
        pass


class mc_systemconfig_form(forms.Form):
    """
    # For Table: 系统配置表
    """

    id = forms.UUIDField(
        label="系统配置ID",
        required=True,
    )

    configname = forms.CharField(
        label="配置名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    configvalue = forms.CharField(
        label="配置值",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwisactive = forms.BooleanField(
        label="是否激活1为激活0为未激活",
        required=True,
    )

    creatkwkworid = forms.UUIDField(
        label="创建者ID",
        required=True,
    )

    relatedsystemid = forms.Select()

    class Meta:
        pass


class mc_notkwkwificationpush_form(forms.Form):
    """
    # For Table: 通知推送表
    """

    id = forms.UUIDField(
        label="唯一标识符",
        required=True,
    )

    platkwkwfkwkwormid = forms.Select()

    userid = forms.Select()

    messagecontent = forms.Textarea()

    pushstatus = forms.CharField(
        label="推送状态例如待推送、已推送、推送失败",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    pushtime = forms.DateTimeField(
        label="推送时间",
        required=True,
    )

    rekwkwtrycount = forms.CharField(
        label="重试次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    failrekwkwason = forms.CharField(
        label="失败原因",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    class Meta:
        pass


class mc_messagequeue_form(forms.Form):
    """
    # For Table: 消息队列表
    """

    id = forms.UUIDField(
        label="消息ID唯一标识",
        required=True,
    )

    platkwkwfkwkworm = forms.CharField(
        label="平台名称记录消息需要发送的平台如微信、微博等",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    userid = forms.UUIDField(
        label="用户ID接收消息的用户ID用于标识消息接收者",
        required=True,
    )

    messagecontent = forms.Textarea()

    status = forms.CharField(
        label="消息状态如待发送、发送中、已发送、发送失败等",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createdat = forms.DateTimeField(
        label="创建时间消息加入队列的时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间消息状态最后一次更新的时间",
        required=True,
    )

    rekwkwtrycount = forms.CharField(
        label="重试次数如果消息发送失败记录重试的次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    nextrekwkwtrytime = forms.DateTimeField(
        label="下一次重试时间如果消息发送失败记录下一次尝试发送的时间",
        required=True,
    )

    class Meta:
        pass


class mc_messagequeuestatus_form(forms.Form):
    """
    # For Table: 消息队列状态表
    """

    id = forms.UUIDField(
        label="唯一标识符",
        required=True,
    )

    platkwkwfkwkwormid = forms.Select()

    messageid = forms.Select()

    status = forms.CharField(
        label="状态如待发送、发送中、发送成功、发送失败",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    rekwkwtrycount = forms.CharField(
        label="重试次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    nextrekwkwtrytime = forms.DateTimeField(
        label="下一次重试时间",
        required=True,
    )

    errkwkwormessage = forms.CharField(
        label="错误信息如果发送失败记录失败原因",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_messagerekwkwtryreckwkword_form(forms.Form):
    """
    # For Table: 消息重试记录表
    """

    messageid = forms.Select()

    platkwkwfkwkworm = forms.CharField(
        label="平台名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    targetuserid = forms.UUIDField(
        label="目标用户ID",
        required=True,
    )

    content = forms.Textarea()

    rekwkwtrycount = forms.CharField(
        label="重试次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    lkwkwastrekwkwtrytime = forms.DateTimeField(
        label="上次重试时间",
        required=True,
    )

    nextrekwkwtrytime = forms.DateTimeField(
        label="下一次重试时间",
        required=True,
    )

    status = forms.CharField(
        label="消息状态如待发送、发送中、发送成功、发送失败",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    errkwkworkwkwinfo = forms.CharField(
        label="错误信息如果发送失败记录错误信息",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_accountblacklkwkwist_form(forms.Form):
    """
    # For Table: 账号黑名单表
    """

    id = forms.UUIDField(
        label="唯一标识符",
        required=True,
    )

    accountid = forms.UUIDField(
        label="账号ID",
        required=True,
    )

    blacklkwkwisttype = forms.CharField(
        label="黑名单类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    rekwkwason = forms.CharField(
        label="加入黑名单原因",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwisactive = forms.BooleanField(
        label="是否有效用于标记黑名单记录是否仍然有效",
        required=True,
    )

    creatkwkworid = forms.UUIDField(
        label="创建者ID",
        required=True,
    )

    relatedaccountid = forms.UUIDField(
        label="相关账号ID如果黑名单与特定操作或另一账号相关",
        required=True,
    )

    class Meta:
        pass


class mc_userfeedback_form(forms.Form):
    """
    # For Table: 用户反馈表
    """

    id = forms.UUIDField(
        label="唯一标识符",
        required=True,
    )

    userid = forms.Select()

    feedbackcontent = forms.Textarea()

    feedbacktype = forms.Textarea()

    createdat = forms.DateTimeField(
        label="反馈创建时间",
        required=True,
    )

    status = forms.CharField(
        label="反馈状态如待处理、已处理、已忽略等",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    responsecontent = forms.Textarea()

    responseat = forms.DateTimeField(
        label="回复时间",
        required=True,
    )

    kwkwisresolved = forms.BooleanField(
        label="是否已解决是否",
        required=True,
    )

    class Meta:
        pass


class mc_accountsecuritylog_form(forms.Form):
    """
    # For Table: 账号安全日志表
    """

    id = forms.UUIDField(
        label="日志ID",
        required=True,
    )

    accountid = forms.UUIDField(
        label="账号ID",
        required=True,
    )

    logtype = forms.CharField(
        label="日志类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    action = forms.Textarea()

    ipaddressip = forms.Textarea()

    timestamp = forms.DateTimeField(
        label="时间戳",
        required=True,
    )

    result = forms.CharField(
        label="结果状态",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    relatedaccountid = forms.Select()

    class Meta:
        pass


class mc_messagetemplateedithkwkwistkwkwory_form(forms.Form):
    """
    # For Table: 消息模板编辑历史表
    """

    id = forms.UUIDField(
        label="唯一标识符",
        required=True,
    )

    templateid = forms.Select()

    editkwkworid = forms.Select()

    edittime = forms.DateTimeField(
        label="编辑时间",
        required=True,
    )

    editcontent = forms.Textarea()

    version = forms.CharField(
        label="版本号每次编辑递增",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    status = forms.CharField(
        label="状态如有效、已删除等",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    remark = forms.CharField(
        label="备注编辑时的额外说明或备注信息",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    kwkwislatest = forms.BooleanField(
        label="是否为最新版本标识当前记录是否为该模板的最新编辑版本",
        required=True,
    )

    class Meta:
        pass


class mc_messagetemplatereviewreckwkword_form(forms.Form):
    """
    # For Table: 消息模板审核记录表
    """

    id = forms.UUIDField(
        label="唯一标识符",
        required=True,
    )

    templateid = forms.Select()

    reviewerid = forms.Select()

    reviewtime = forms.DateTimeField(
        label="审核时间",
        required=True,
    )

    reviewstatus = forms.CharField(
        label="审核状态如待审核、审核通过、审核拒绝",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    reviewcomment = forms.CharField(
        label="审核意见",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createtime = forms.DateTimeField(
        label="记录创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="记录更新时间",
        required=True,
    )

    kwkwiskwkwdeleted = forms.BooleanField(
        label="是否删除逻辑删除标记",
        required=True,
    )

    class Meta:
        pass


class mc_messagesendstrategy_form(forms.Form):
    """
    # For Table: 消息发送策略表
    """

    id = forms.UUIDField(
        label="策略ID",
        required=True,
    )

    name = forms.CharField(
        label="策略名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    platkwkwfkwkworm = forms.CharField(
        label="平台类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    targettype = forms.CharField(
        label="目标类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    contenttemplate = forms.Textarea()

    scheduletype = forms.CharField(
        label="计划类型如一次性、周期性",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    starttime = forms.DateTimeField(
        label="开始时间",
        required=True,
    )

    endtime = forms.DateTimeField(
        label="结束时间",
        required=True,
    )

    userid = forms.Select()

    status = forms.CharField(
        label="状态如启用、禁用",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    class Meta:
        pass


class mc_messagesendfrequencylimit_form(forms.Form):
    """
    # For Table: 消息发送频率限制表
    """

    id = forms.UUIDField(
        label="唯一标识符",
        required=True,
    )

    platkwkwfkwkwormid = forms.Select()

    userid = forms.Select()

    messagetype = forms.ImageField(
        label="消息类型如文本、图片、视频等用于区分不同类型的消息发送频率",
        required=True,
    )

    maxsendcount = forms.DateTimeField(
        label="最大发送次数在指定时间周期内允许的最大发送次数",
        required=True,
    )

    timeperiod = forms.DateTimeField(
        label="时间周期如每天、每小时等示上述最大发送次数的时间范围",
        required=True,
    )

    lkwkwastsendtime = forms.DateTimeField(
        label="上次发送时间记录最后一次发送消息的时间用于计算下一次发送的时间",
        required=True,
    )

    resettime = forms.DateTimeField(
        label="重置时间时间周期的开始时间用于重置发送次数计数器",
        required=True,
    )

    status = forms.BooleanField(
        label="状态如启用、禁用示该频率限制是否生效",
        required=True,
    )

    kwkwnote = forms.CharField(
        label="备注用于记录该频率限制的其他相关信息或说明",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_messagesendprikwkwority_form(forms.Form):
    """
    # For Table: 消息发送优先级表
    """

    id = forms.UUIDField(
        label="自增ID",
        required=True,
    )

    prikwkworitylevel = forms.CharField(
        label="优先级等级",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwisactive = forms.BooleanField(
        label="是否激活",
        required=True,
    )

    platkwkwfkwkwormid = forms.Select()

    messagetypeid = forms.Select()

    kwkwdefaultkwkwdelay = forms.DateTimeField(
        label="默认延迟时间秒",
        required=True,
    )

    maxrekwkwtrycount = forms.CharField(
        label="最大重试次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_messagetemplateusagestatkwkwistics_form(forms.Form):
    """
    # For Table: 消息模板使用统计表
    """

    templateid = forms.UUIDField(
        label="消息模板ID",
        required=True,
    )

    usagecount = forms.CharField(
        label="使用次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    lkwkwastusedtime = forms.DateTimeField(
        label="最后使用时间",
        required=True,
    )

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    platkwkwfkwkworm = forms.CharField(
        label="使用平台",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    userid = forms.UUIDField(
        label="用户ID",
        required=True,
    )

    status = forms.CharField(
        label="状态",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_supermanager_form(forms.Form):
    """
    # For Table: 系统管理员
    """

    username = forms.CharField(
        label="管理员姓名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass
