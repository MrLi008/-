from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="config_visual_view_index"),
    path("bi", views.bi, name="config_visual_view_bi"),
    path("bi_level_2", views.bi_level_2, name="config_visual_view_bi_level_2"),
    path("bi_new", views.bi_new, name="config_visual_view_bi_new"),
    path("bi_v1", views.bi, name="config_visual_view_bi_v1"),
    path("bi_v2", views.bi, name="config_visual_view_bi_v2"),
    path("bi_v3", views.bi, name="config_visual_view_bi_v3"),
    path("bi_v4", views.bi, name="config_visual_view_bi_v4"),
    path("bi_v5", views.bi, name="config_visual_view_bi_v5"),
    #
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpuserinfo",
        views.view_userinfo,
        name="bi_tpuserinfo",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpplatkwkwfkwkwormaccount",
        views.view_platkwkwfkwkwormaccount,
        name="bi_tpplatkwkwfkwkwormaccount",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagetemplate",
        views.view_messagetemplate,
        name="bi_tpmessagetemplate",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tptkwkwaskmanagement",
        views.view_tkwkwaskmanagement,
        name="bi_tptkwkwaskmanagement",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tptkwkwaskexecutionreckwkword",
        views.view_tkwkwaskexecutionreckwkword,
        name="bi_tptkwkwaskexecutionreckwkword",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tptkwkwaskstatus",
        views.view_tkwkwaskstatus,
        name="bi_tptkwkwaskstatus",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpscheduledtkwkwask",
        views.view_scheduledtkwkwask,
        name="bi_tpscheduledtkwkwask",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagesendreckwkword",
        views.view_messagesendreckwkword,
        name="bi_tpmessagesendreckwkword",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagereceivereckwkword",
        views.view_messagereceivereckwkword,
        name="bi_tpmessagereceivereckwkword",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpuserpreference",
        views.view_userpreference,
        name="bi_tpuserpreference",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpaccountbkwkwindkwkwing",
        views.view_accountbkwkwindkwkwing,
        name="bi_tpaccountbkwkwindkwkwing",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagecontentreview",
        views.view_messagecontentreview,
        name="bi_tpmessagecontentreview",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagesendfailurelog",
        views.view_messagesendfailurelog,
        name="bi_tpmessagesendfailurelog",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagesendsuccesslog",
        views.view_messagesendsuccesslog,
        name="bi_tpmessagesendsuccesslog",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagetemplatecategkwkwory",
        views.view_messagetemplatecategkwkwory,
        name="bi_tpmessagetemplatecategkwkwory",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagetemplatetag",
        views.view_messagetemplatetag,
        name="bi_tpmessagetemplatetag",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpuserpermkwkwission",
        views.view_userpermkwkwission,
        name="bi_tpuserpermkwkwission",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpsystemconfig",
        views.view_systemconfig,
        name="bi_tpsystemconfig",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpnotkwkwificationpush",
        views.view_notkwkwificationpush,
        name="bi_tpnotkwkwificationpush",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagequeue",
        views.view_messagequeue,
        name="bi_tpmessagequeue",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagequeuestatus",
        views.view_messagequeuestatus,
        name="bi_tpmessagequeuestatus",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagerekwkwtryreckwkword",
        views.view_messagerekwkwtryreckwkword,
        name="bi_tpmessagerekwkwtryreckwkword",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpaccountblacklkwkwist",
        views.view_accountblacklkwkwist,
        name="bi_tpaccountblacklkwkwist",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpuserfeedback",
        views.view_userfeedback,
        name="bi_tpuserfeedback",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpaccountsecuritylog",
        views.view_accountsecuritylog,
        name="bi_tpaccountsecuritylog",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagetemplateedithkwkwistkwkwory",
        views.view_messagetemplateedithkwkwistkwkwory,
        name="bi_tpmessagetemplateedithkwkwistkwkwory",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagetemplatereviewreckwkword",
        views.view_messagetemplatereviewreckwkword,
        name="bi_tpmessagetemplatereviewreckwkword",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagesendstrategy",
        views.view_messagesendstrategy,
        name="bi_tpmessagesendstrategy",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagesendfrequencylimit",
        views.view_messagesendfrequencylimit,
        name="bi_tpmessagesendfrequencylimit",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagesendprikwkwority",
        views.view_messagesendprikwkwority,
        name="bi_tpmessagesendprikwkwority",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpmessagetemplateusagestatkwkwistics",
        views.view_messagetemplateusagestatkwkwistics,
        name="bi_tpmessagetemplateusagestatkwkwistics",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpsupermanager",
        views.view_supermanager,
        name="bi_tpsupermanager",
    ),
]
