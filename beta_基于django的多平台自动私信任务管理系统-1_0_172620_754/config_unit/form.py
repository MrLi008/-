from django import forms
from captcha.fields import CaptchaField

from appcenter.form import *

all_tables_form = {
    "userinfo": mc_userinfo_form,
    "platkwkwfkwkwormaccount": mc_platkwkwfkwkwormaccount_form,
    "messagetemplate": mc_messagetemplate_form,
    "tkwkwaskmanagement": mc_tkwkwaskmanagement_form,
    "tkwkwaskexecutionreckwkword": mc_tkwkwaskexecutionreckwkword_form,
    "tkwkwaskstatus": mc_tkwkwaskstatus_form,
    "scheduledtkwkwask": mc_scheduledtkwkwask_form,
    "messagesendreckwkword": mc_messagesendreckwkword_form,
    "messagereceivereckwkword": mc_messagereceivereckwkword_form,
    "userpreference": mc_userpreference_form,
    "accountbkwkwindkwkwing": mc_accountbkwkwindkwkwing_form,
    "messagecontentreview": mc_messagecontentreview_form,
    "messagesendfailurelog": mc_messagesendfailurelog_form,
    "messagesendsuccesslog": mc_messagesendsuccesslog_form,
    "messagetemplatecategkwkwory": mc_messagetemplatecategkwkwory_form,
    "messagetemplatetag": mc_messagetemplatetag_form,
    "userpermkwkwission": mc_userpermkwkwission_form,
    "systemconfig": mc_systemconfig_form,
    "notkwkwificationpush": mc_notkwkwificationpush_form,
    "messagequeue": mc_messagequeue_form,
    "messagequeuestatus": mc_messagequeuestatus_form,
    "messagerekwkwtryreckwkword": mc_messagerekwkwtryreckwkword_form,
    "accountblacklkwkwist": mc_accountblacklkwkwist_form,
    "userfeedback": mc_userfeedback_form,
    "accountsecuritylog": mc_accountsecuritylog_form,
    "messagetemplateedithkwkwistkwkwory": mc_messagetemplateedithkwkwistkwkwory_form,
    "messagetemplatereviewreckwkword": mc_messagetemplatereviewreckwkword_form,
    "messagesendstrategy": mc_messagesendstrategy_form,
    "messagesendfrequencylimit": mc_messagesendfrequencylimit_form,
    "messagesendprikwkwority": mc_messagesendprikwkwority_form,
    "messagetemplateusagestatkwkwistics": mc_messagetemplateusagestatkwkwistics_form,
    "supermanager": mc_supermanager_form,
}
