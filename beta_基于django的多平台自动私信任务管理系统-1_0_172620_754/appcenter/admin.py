from django.contrib import admin

from django.forms.widgets import Select

# Register your models here.

admin.site.site_header = "beta_基于django的多平台自动私信任务管理系统"
admin.site.site_title = "beta_基于django的多平台自动私信任务管理系统"
admin.site.index_title = "beta_基于django的多平台自动私信任务管理系统"

from .models import *


class mc_userinfo_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "avatarurl",
        "roleid",
        "email",
        "status",
        "userid",
        "pkwkwasswkwkwordhkwkwash",
        "regkwkwistertime",
        "username",
        "lkwkwastlogkwkwintime",
        "phonenumber",
    ]
    fields = [
        "avatarurl",
        "email",
        "status",
        "pkwkwasswkwkwordhkwkwash",
        "username",
        "roleid",
        "phonenumber",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["roleid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.roleid),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form


admin.site.register(mc_userinfo, mc_userinfo_admin)


class mc_platkwkwfkwkwormaccount_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "kwkwassociateduserid",
        "accountname",
        "createdat",
        "platkwkwfkwkwormname",
        "pkwkwasswkwkword",
        "status",
        "updatedat",
        "accesstoken",
        "accounttype",
        "username",
        "lkwkwastlogkwkwintime",
        "platkwkwfkwkwormid",
    ]
    fields = [
        "kwkwassociateduserid",
        "accountname",
        "platkwkwfkwkwormname",
        "pkwkwasswkwkword",
        "status",
        "accesstoken",
        "accounttype",
        "username",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["kwkwassociateduserid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form


admin.site.register(mc_platkwkwfkwkwormaccount, mc_platkwkwfkwkwormaccount_admin)


class mc_messagetemplate_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "templateid",
        "templatename",
        "platkwkwfkwkwormtype",
        "templatecontent",
        "createtime",
        "creatkwkworid",
        "targetuserid",
        "kwkwisactive",
        "updatetime",
    ]
    fields = [
        "templatename",
        "kwkwisactive",
        "templatecontent",
        "platkwkwfkwkwormtype",
    ]


admin.site.register(mc_messagetemplate, mc_messagetemplate_admin)


class mc_tkwkwaskmanagement_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "messagecontent",
        "scheduledtime",
        "createdtime",
        "kwkwassociateduserid",
        "tkwkwaskid",
        "status",
        "tkwkwaskname",
        "platkwkwfkwkworm",
        "updatedtime",
        "targetuserid",
    ]
    fields = [
        "messagecontent",
        "kwkwassociateduserid",
        "status",
        "tkwkwaskname",
        "platkwkwfkwkworm",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["kwkwassociateduserid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form


admin.site.register(mc_tkwkwaskmanagement, mc_tkwkwaskmanagement_admin)


class mc_tkwkwaskexecutionreckwkword_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "messagecontent",
        "recipientid",
        "tkwkwaskid",
        "errkwkwormessage",
        "status",
        "platkwkwfkwkworm",
        "userid",
        "senderid",
        "tkwkwasktemplateid",
        "executiontime",
    ]
    fields = [
        "messagecontent",
        "status",
        "errkwkwormessage",
        "platkwkwfkwkworm",
    ]


admin.site.register(
    mc_tkwkwaskexecutionreckwkword, mc_tkwkwaskexecutionreckwkword_admin
)


class mc_tkwkwaskstatus_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "messagecontent",
        "tkwkwaskid",
        "createdat",
        "updatedat",
        "userid",
        "statusname",
        "completedat",
        "statuscode",
        "platkwkwfkwkwormid",
        "kwkwisactive",
    ]
    fields = [
        "messagecontent",
        "statuscode",
        "kwkwisactive",
        "statusname",
    ]


admin.site.register(mc_tkwkwaskstatus, mc_tkwkwaskstatus_admin)


class mc_scheduledtkwkwask_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "targetplatkwkwfkwkworm",
        "lkwkwasterrkwkwor",
        "tkwkwaskid",
        "creatkwkwor",
        "tkwkwaskname",
        "relateduserid",
        "scheduletime",
        "createtime",
        "executestatus",
        "updatetime",
    ]
    fields = [
        "targetplatkwkwfkwkworm",
        "lkwkwasterrkwkwor",
        "creatkwkwor",
        "tkwkwaskname",
        "relateduserid",
        "executestatus",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["relateduserid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form


admin.site.register(mc_scheduledtkwkwask, mc_scheduledtkwkwask_admin)


class mc_messagesendreckwkword_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "messagecontent",
        "sendtime",
        "lkwkwastrekwkwtrytime",
        "errkwkwormessage",
        "id",
        "status",
        "userid",
        "rekwkwtrycount",
        "platkwkwfkwkwormid",
        "targetuserid",
    ]
    fields = [
        "messagecontent",
        "errkwkwormessage",
        "status",
        "userid",
        "rekwkwtrycount",
        "platkwkwfkwkwormid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["platkwkwfkwkwormid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.accountname),
                )
                for item in mc_platkwkwfkwkwormaccount.objects.all()
            ]
        )

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form


admin.site.register(mc_messagesendreckwkword, mc_messagesendreckwkword_admin)


class mc_messagereceivereckwkword_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "messagecontent",
        "id",
        "responsetime",
        "status",
        "responsecontent",
        "userid",
        "kwkwisread",
        "receivetime",
        "platkwkwfkwkwormid",
    ]
    fields = [
        "messagecontent",
        "status",
        "responsecontent",
        "userid",
        "kwkwisread",
        "platkwkwfkwkwormid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["platkwkwfkwkwormid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.accountname),
                )
                for item in mc_platkwkwfkwkwormaccount.objects.all()
            ]
        )

        return form


admin.site.register(mc_messagereceivereckwkword, mc_messagereceivereckwkword_admin)


class mc_userpreference_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "preferencevalue",
        "description",
        "preferencetype",
        "preferencename",
        "userid",
        "createtime",
        "platkwkwfkwkwormid",
        "kwkwisactive",
        "updatetime",
    ]
    fields = [
        "preferencevalue",
        "description",
        "preferencetype",
        "preferencename",
        "platkwkwfkwkwormid",
        "kwkwisactive",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["platkwkwfkwkwormid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.accountname),
                )
                for item in mc_platkwkwfkwkwormaccount.objects.all()
            ]
        )

        return form


admin.site.register(mc_userpreference, mc_userpreference_admin)


class mc_accountbkwkwindkwkwing_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "createdat",
        "bkwkwindkwkwingstatus",
        "id",
        "updatedat",
        "accountid",
        "userid",
        "bkwkwindkwkwingtype",
        "platkwkwfkwkwormid",
    ]
    fields = [
        "bkwkwindkwkwingtype",
        "bkwkwindkwkwingstatus",
    ]


admin.site.register(mc_accountbkwkwindkwkwing, mc_accountbkwkwindkwkwing_admin)


class mc_messagecontentreview_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "kwkwissensitive",
        "reviewstatus",
        "createdat",
        "id",
        "reviewtime",
        "content",
        "platkwkwfkwkworm",
        "userid",
        "rejectionrekwkwason",
        "reviewerid",
    ]
    fields = [
        "kwkwissensitive",
        "reviewstatus",
        "content",
        "platkwkwfkwkworm",
        "rejectionrekwkwason",
    ]


admin.site.register(mc_messagecontentreview, mc_messagecontentreview_admin)


class mc_messagesendfailurelog_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "sendtime",
        "lkwkwastrekwkwtrytime",
        "kwkwisresolved",
        "id",
        "failurerekwkwason",
        "messageid",
        "platkwkwfkwkworm",
        "userid",
        "rekwkwtrycount",
        "targetuserid",
    ]
    fields = [
        "failurerekwkwason",
        "rekwkwtrycount",
        "kwkwisresolved",
        "platkwkwfkwkworm",
    ]


admin.site.register(mc_messagesendfailurelog, mc_messagesendfailurelog_admin)


class mc_messagesendsuccesslog_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "sendtime",
        "relatedtkwkwaskid",
        "status",
        "messageid",
        "content",
        "platkwkwfkwkworm",
        "userid",
        "receiverid",
        "errkwkworkwkwinfo",
    ]
    fields = [
        "relatedtkwkwaskid",
        "status",
        "content",
        "platkwkwfkwkworm",
        "errkwkworkwkwinfo",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["relatedtkwkwaskid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.tkwkwaskname),
                )
                for item in mc_tkwkwaskmanagement.objects.all()
            ]
        )

        return form


admin.site.register(mc_messagesendsuccesslog, mc_messagesendsuccesslog_admin)


class mc_messagetemplatecategkwkwory_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "createdat",
        "id",
        "description",
        "updatedat",
        "templatecount",
        "parentid",
        "name",
        "kwkwisactive",
        "skwkwortkwkworder",
    ]
    fields = [
        "description",
        "templatecount",
        "kwkwisactive",
        "name",
        "skwkwortkwkworder",
    ]


admin.site.register(
    mc_messagetemplatecategkwkwory, mc_messagetemplatecategkwkwory_admin
)


class mc_messagetemplatetag_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "createdat",
        "id",
        "templateid",
        "description",
        "updatedat",
        "tagname",
        "usagecount",
        "creatkwkworid",
        "kwkwisactive",
    ]
    fields = [
        "templateid",
        "description",
        "tagname",
        "usagecount",
        "creatkwkworid",
        "kwkwisactive",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["templateid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.version),
                )
                for item in mc_messagetemplateedithkwkwistkwkwory.objects.all()
            ]
        )

        # :TODO
        form.base_fields["creatkwkworid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form


admin.site.register(mc_messagetemplatetag, mc_messagetemplatetag_admin)


class mc_userpermkwkwission_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "permkwkwissionname",
        "rolename",
        "userid",
        "isactive",
        "createtime",
        "isdeleted",
        "permkwkwissiondescription",
        "permkwkwissionid",
        "updatetime",
    ]
    fields = [
        "rolename",
        "isactive",
        "isdeleted",
        "permkwkwissiondescription",
        "permkwkwissionname",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["rolename"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.roleid),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form


admin.site.register(mc_userpermkwkwission, mc_userpermkwkwission_admin)


class mc_systemconfig_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "configvalue",
        "id",
        "description",
        "configname",
        "relatedsystemid",
        "createtime",
        "creatkwkworid",
        "kwkwisactive",
        "updatetime",
    ]
    fields = [
        "configvalue",
        "description",
        "configname",
        "relatedsystemid",
        "kwkwisactive",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["relatedsystemid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.relatedsystemid),
                )
                for item in mc_systemconfig.objects.all()
            ]
        )

        return form


admin.site.register(mc_systemconfig, mc_systemconfig_admin)


class mc_notkwkwificationpush_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "messagecontent",
        "failrekwkwason",
        "createdat",
        "id",
        "updatedat",
        "userid",
        "rekwkwtrycount",
        "pushtime",
        "pushstatus",
        "platkwkwfkwkwormid",
    ]
    fields = [
        "messagecontent",
        "failrekwkwason",
        "userid",
        "rekwkwtrycount",
        "pushstatus",
        "platkwkwfkwkwormid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["platkwkwfkwkwormid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.accountname),
                )
                for item in mc_platkwkwfkwkwormaccount.objects.all()
            ]
        )

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form


admin.site.register(mc_notkwkwificationpush, mc_notkwkwificationpush_admin)


class mc_messagequeue_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "messagecontent",
        "nextrekwkwtrytime",
        "createdat",
        "id",
        "updatedat",
        "status",
        "platkwkwfkwkworm",
        "userid",
        "rekwkwtrycount",
    ]
    fields = [
        "messagecontent",
        "status",
        "rekwkwtrycount",
        "platkwkwfkwkworm",
    ]


admin.site.register(mc_messagequeue, mc_messagequeue_admin)


class mc_messagequeuestatus_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "nextrekwkwtrytime",
        "createdat",
        "id",
        "updatedat",
        "status",
        "errkwkwormessage",
        "messageid",
        "rekwkwtrycount",
        "platkwkwfkwkwormid",
    ]
    fields = [
        "errkwkwormessage",
        "status",
        "messageid",
        "rekwkwtrycount",
        "platkwkwfkwkwormid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["platkwkwfkwkwormid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.accountname),
                )
                for item in mc_platkwkwfkwkwormaccount.objects.all()
            ]
        )

        # :TODO
        form.base_fields["messageid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.sendtime),
                )
                for item in mc_messagesendreckwkword.objects.all()
            ]
        )

        return form


admin.site.register(mc_messagequeuestatus, mc_messagequeuestatus_admin)


class mc_messagerekwkwtryreckwkword_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "lkwkwastrekwkwtrytime",
        "nextrekwkwtrytime",
        "status",
        "messageid",
        "content",
        "platkwkwfkwkworm",
        "rekwkwtrycount",
        "errkwkworkwkwinfo",
        "targetuserid",
    ]
    fields = [
        "status",
        "messageid",
        "content",
        "platkwkwfkwkworm",
        "rekwkwtrycount",
        "errkwkworkwkwinfo",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["messageid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.sendtime),
                )
                for item in mc_messagesendreckwkword.objects.all()
            ]
        )

        return form


admin.site.register(mc_messagerekwkwtryreckwkword, mc_messagerekwkwtryreckwkword_admin)


class mc_accountblacklkwkwist_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "relatedaccountid",
        "id",
        "accountid",
        "rekwkwason",
        "kwkwisactive",
        "createtime",
        "creatkwkworid",
        "blacklkwkwisttype",
        "updatetime",
    ]
    fields = [
        "kwkwisactive",
        "blacklkwkwisttype",
        "rekwkwason",
    ]


admin.site.register(mc_accountblacklkwkwist, mc_accountblacklkwkwist_admin)


class mc_userfeedback_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "feedbacktype",
        "kwkwisresolved",
        "createdat",
        "id",
        "status",
        "responsecontent",
        "responseat",
        "userid",
        "feedbackcontent",
    ]
    fields = [
        "feedbacktype",
        "kwkwisresolved",
        "status",
        "responsecontent",
        "userid",
        "feedbackcontent",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form


admin.site.register(mc_userfeedback, mc_userfeedback_admin)


class mc_accountsecuritylog_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "relatedaccountid",
        "logtype",
        "id",
        "description",
        "accountid",
        "action",
        "ipaddressip",
        "timestamp",
        "result",
    ]
    fields = [
        "relatedaccountid",
        "logtype",
        "description",
        "action",
        "ipaddressip",
        "result",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["relatedaccountid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.accountname),
                )
                for item in mc_platkwkwfkwkwormaccount.objects.all()
            ]
        )

        return form


admin.site.register(mc_accountsecuritylog, mc_accountsecuritylog_admin)


class mc_messagetemplateedithkwkwistkwkwory_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "kwkwislatest",
        "id",
        "templateid",
        "status",
        "edittime",
        "version",
        "remark",
        "editkwkworid",
        "editcontent",
    ]
    fields = [
        "kwkwislatest",
        "templateid",
        "status",
        "remark",
        "editkwkworid",
        "editcontent",
        "version",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["templateid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.name),
                )
                for item in mc_messagetemplatecategkwkwory.objects.all()
            ]
        )

        # :TODO
        form.base_fields["editkwkworid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form


admin.site.register(
    mc_messagetemplateedithkwkwistkwkwory, mc_messagetemplateedithkwkwistkwkwory_admin
)


class mc_messagetemplatereviewreckwkword_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "reviewstatus",
        "id",
        "templateid",
        "kwkwiskwkwdeleted",
        "reviewtime",
        "reviewcomment",
        "createtime",
        "updatetime",
        "reviewerid",
    ]
    fields = [
        "reviewstatus",
        "templateid",
        "kwkwiskwkwdeleted",
        "reviewcomment",
        "reviewerid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["templateid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.name),
                )
                for item in mc_messagetemplatecategkwkwory.objects.all()
            ]
        )

        # :TODO
        form.base_fields["reviewerid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form


admin.site.register(
    mc_messagetemplatereviewreckwkword, mc_messagetemplatereviewreckwkword_admin
)


class mc_messagesendstrategy_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "createdat",
        "id",
        "description",
        "status",
        "scheduletype",
        "updatedat",
        "platkwkwfkwkworm",
        "userid",
        "name",
        "endtime",
        "targettype",
        "starttime",
        "contenttemplate",
    ]
    fields = [
        "description",
        "status",
        "scheduletype",
        "platkwkwfkwkworm",
        "userid",
        "name",
        "targettype",
        "contenttemplate",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form


admin.site.register(mc_messagesendstrategy, mc_messagesendstrategy_admin)


class mc_messagesendfrequencylimit_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "id",
        "status",
        "maxsendcount",
        "kwkwnote",
        "userid",
        "lkwkwastsendtime",
        "messagetype",
        "timeperiod",
        "resettime",
        "platkwkwfkwkwormid",
    ]
    fields = [
        "status",
        "kwkwnote",
        "userid",
        "messagetype",
        "platkwkwfkwkwormid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["platkwkwfkwkwormid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.accountname),
                )
                for item in mc_platkwkwfkwkwormaccount.objects.all()
            ]
        )

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form


admin.site.register(mc_messagesendfrequencylimit, mc_messagesendfrequencylimit_admin)


class mc_messagesendprikwkwority_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "messagetypeid",
        "createdat",
        "id",
        "description",
        "updatedat",
        "maxrekwkwtrycount",
        "kwkwdefaultkwkwdelay",
        "platkwkwfkwkwormid",
        "kwkwisactive",
        "prikwkworitylevel",
    ]
    fields = [
        "messagetypeid",
        "maxrekwkwtrycount",
        "description",
        "platkwkwfkwkwormid",
        "kwkwisactive",
        "prikwkworitylevel",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["platkwkwfkwkwormid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.accountname),
                )
                for item in mc_platkwkwfkwkwormaccount.objects.all()
            ]
        )

        # :TODO
        form.base_fields["messagetypeid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.name),
                )
                for item in mc_messagetemplatecategkwkwory.objects.all()
            ]
        )

        return form


admin.site.register(mc_messagesendprikwkwority, mc_messagesendprikwkwority_admin)


class mc_messagetemplateusagestatkwkwistics_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "createdat",
        "templateid",
        "updatedat",
        "status",
        "platkwkwfkwkworm",
        "userid",
        "usagecount",
        "lkwkwastusedtime",
    ]
    fields = [
        "status",
        "usagecount",
        "platkwkwfkwkworm",
    ]


admin.site.register(
    mc_messagetemplateusagestatkwkwistics, mc_messagetemplateusagestatkwkwistics_admin
)


class mc_supermanager_admin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
    ]
    fields = [
        "username",
    ]


admin.site.register(mc_supermanager, mc_supermanager_admin)
