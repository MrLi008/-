from django.db import models
from appcenter.models import *
from config_visual.models import *
from sys_user.models import *
from sys_user.func import *

all_tables = dict()
gl = dict()

# Create your models here.

all_tables = {
    "userinfo": mymeta(mc_userinfo),
    "platkwkwfkwkwormaccount": mymeta(mc_platkwkwfkwkwormaccount),
    "messagetemplate": mymeta(mc_messagetemplate),
    "tkwkwaskmanagement": mymeta(mc_tkwkwaskmanagement),
    "tkwkwaskexecutionreckwkword": mymeta(mc_tkwkwaskexecutionreckwkword),
    "tkwkwaskstatus": mymeta(mc_tkwkwaskstatus),
    "scheduledtkwkwask": mymeta(mc_scheduledtkwkwask),
    "messagesendreckwkword": mymeta(mc_messagesendreckwkword),
    "messagereceivereckwkword": mymeta(mc_messagereceivereckwkword),
    "userpreference": mymeta(mc_userpreference),
    "accountbkwkwindkwkwing": mymeta(mc_accountbkwkwindkwkwing),
    "messagecontentreview": mymeta(mc_messagecontentreview),
    "messagesendfailurelog": mymeta(mc_messagesendfailurelog),
    "messagesendsuccesslog": mymeta(mc_messagesendsuccesslog),
    "messagetemplatecategkwkwory": mymeta(mc_messagetemplatecategkwkwory),
    "messagetemplatetag": mymeta(mc_messagetemplatetag),
    "userpermkwkwission": mymeta(mc_userpermkwkwission),
    "systemconfig": mymeta(mc_systemconfig),
    "notkwkwificationpush": mymeta(mc_notkwkwificationpush),
    "messagequeue": mymeta(mc_messagequeue),
    "messagequeuestatus": mymeta(mc_messagequeuestatus),
    "messagerekwkwtryreckwkword": mymeta(mc_messagerekwkwtryreckwkword),
    "accountblacklkwkwist": mymeta(mc_accountblacklkwkwist),
    "userfeedback": mymeta(mc_userfeedback),
    "accountsecuritylog": mymeta(mc_accountsecuritylog),
    "messagetemplateedithkwkwistkwkwory": mymeta(mc_messagetemplateedithkwkwistkwkwory),
    "messagetemplatereviewreckwkword": mymeta(mc_messagetemplatereviewreckwkword),
    "messagesendstrategy": mymeta(mc_messagesendstrategy),
    "messagesendfrequencylimit": mymeta(mc_messagesendfrequencylimit),
    "messagesendprikwkwority": mymeta(mc_messagesendprikwkwority),
    "messagetemplateusagestatkwkwistics": mymeta(mc_messagetemplateusagestatkwkwistics),
    "supermanager": mymeta(mc_supermanager),
}

# 所有用户表

all_tables_user = {
    "userinfo": mymeta(mc_userinfo),
    "supermanager": mymeta(mc_supermanager),
}
gl = {
    "userinfo": mc_userinfo,
    "platkwkwfkwkwormaccount": mc_platkwkwfkwkwormaccount,
    "messagetemplate": mc_messagetemplate,
    "tkwkwaskmanagement": mc_tkwkwaskmanagement,
    "tkwkwaskexecutionreckwkword": mc_tkwkwaskexecutionreckwkword,
    "tkwkwaskstatus": mc_tkwkwaskstatus,
    "scheduledtkwkwask": mc_scheduledtkwkwask,
    "messagesendreckwkword": mc_messagesendreckwkword,
    "messagereceivereckwkword": mc_messagereceivereckwkword,
    "userpreference": mc_userpreference,
    "accountbkwkwindkwkwing": mc_accountbkwkwindkwkwing,
    "messagecontentreview": mc_messagecontentreview,
    "messagesendfailurelog": mc_messagesendfailurelog,
    "messagesendsuccesslog": mc_messagesendsuccesslog,
    "messagetemplatecategkwkwory": mc_messagetemplatecategkwkwory,
    "messagetemplatetag": mc_messagetemplatetag,
    "userpermkwkwission": mc_userpermkwkwission,
    "systemconfig": mc_systemconfig,
    "notkwkwificationpush": mc_notkwkwificationpush,
    "messagequeue": mc_messagequeue,
    "messagequeuestatus": mc_messagequeuestatus,
    "messagerekwkwtryreckwkword": mc_messagerekwkwtryreckwkword,
    "accountblacklkwkwist": mc_accountblacklkwkwist,
    "userfeedback": mc_userfeedback,
    "accountsecuritylog": mc_accountsecuritylog,
    "messagetemplateedithkwkwistkwkwory": mc_messagetemplateedithkwkwistkwkwory,
    "messagetemplatereviewreckwkword": mc_messagetemplatereviewreckwkword,
    "messagesendstrategy": mc_messagesendstrategy,
    "messagesendfrequencylimit": mc_messagesendfrequencylimit,
    "messagesendprikwkwority": mc_messagesendprikwkwority,
    "messagetemplateusagestatkwkwistics": mc_messagetemplateusagestatkwkwistics,
    "supermanager": mc_supermanager,
}
