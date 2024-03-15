from django.db import models

class BaseModel(models.Model):
    available = models.CharField(max_length=1, db_comment='是否啟用(0: 不啟用, 1: 啟用)')
    create_id = models.CharField(max_length=254, db_comment='創建者Id')
    create_date = models.DateTimeField(db_comment='創建日期')
    modify_id = models.CharField(max_length=254, db_comment='修改者Id')
    modify_date = models.DateTimeField(db_comment='修改日期')
class AccountEmailaddress(models.Model):
    email = models.CharField(max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'
        unique_together = (('user', 'email'),)


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class Application(BaseModel):
    chart_id = models.IntegerField(db_comment='圖表流水號')
    applicant = models.CharField(max_length=254, db_comment='申請人')
    guarantor = models.CharField(max_length=254, db_comment='保證人')
    start_date = models.DateTimeField(db_comment='開始日')
    end_data = models.DateTimeField(db_comment='到期日')
    reason = models.TextField()

    class Meta:
        managed = False
        db_table = 'application'
        db_table_comment = '圖表申請表'


class AssignedTaskSponsor(BaseModel):
    assigned_task_id = models.IntegerField(db_comment='交辦事項id\n')
    sponsor_user_id = models.CharField(max_length=254, db_comment='發起人 user_id\n')

    class Meta:
        managed = False
        db_table = 'assigned_task_sponsor'
        db_table_comment = '交辦事項發起人'


class AssignedTasks(BaseModel):
    chart_id = models.IntegerField(db_comment='圖表id')
    name = models.CharField(max_length=254, db_comment='事項名稱')
    default_processer = models.CharField(max_length=254, db_comment='預設處理人')

    class Meta:
        managed = False
        db_table = 'assigned_tasks'
        db_table_comment = '交辦事項'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chart(BaseModel):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'chart'
        db_table_comment = '視覺化後圖表'


class ChartDashboard(BaseModel):
    chart_id = models.IntegerField()
    dashboard_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'chart_dashboard'
        db_table_comment = '儀表板有哪些圖表'


class ChartGroup(BaseModel):
    chart_id = models.IntegerField(db_comment='圖表流水號')
    group_id = models.IntegerField(db_comment='群組流水號')

    class Meta:
        managed = False
        db_table = 'chart_group'
        db_table_comment = '哪個群組可以使用那些圖表'


class Dashboard(BaseModel):
    name = models.CharField(max_length=254, db_comment='儀錶板名稱')

    class Meta:
        managed = False
        db_table = 'dashboard'
        db_table_comment = '儀表板'


class Department(models.Model):
    id = models.CharField(primary_key=True, max_length=2, db_comment='部門 id')
    name = models.CharField(max_length=45, db_comment='部門名稱')
    available = models.CharField(max_length=1, db_comment='是否啟用(0: 不啟用, 1: 啟用)')

    class Meta:
        managed = False
        db_table = 'department'
        db_table_comment = '部門'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Export(BaseModel):
    chart_id = models.IntegerField(db_comment='圖表id\n')
    exporter = models.CharField(max_length=254, db_comment='可匯出的使用者')

    class Meta:
        managed = False
        db_table = 'export'
        db_table_comment = '匯出管理'


class Group(BaseModel):
    name = models.CharField(max_length=45, db_comment='群組名稱')

    class Meta:
        managed = False
        db_table = 'group'
        db_table_comment = '群組權限管理'


class Mail(BaseModel):
    assigned_task_id = models.IntegerField(blank=True, null=True, db_comment='交辦事項id')
    chart_id = models.CharField(max_length=45, db_comment='圖表id')
    name = models.CharField(max_length=254, db_comment='郵件名稱')
    status = models.CharField(max_length=1, db_comment='處理狀態')
    content = models.TextField(db_comment='郵件內容')
    publisher = models.CharField(max_length=254, db_comment='發信人')
    receiver = models.CharField(max_length=254, db_comment='接收人')
    email_send_time = models.DateTimeField(db_comment='email發送時間')

    class Meta:
        managed = False
        db_table = 'mail'
        db_table_comment = '系統或交辦事項郵件'


class MailMessage(BaseModel):
    mail_id = models.IntegerField(blank=True, null=True, db_comment='郵件id')
    message_id = models.IntegerField(blank=True, null=True, db_comment='訊息id')
    content = models.TextField(db_comment='訊息內容')

    class Meta:
        managed = False
        db_table = 'mail_message'
        db_table_comment = '郵件訊息'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=200)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.JSONField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)
    provider_id = models.CharField(max_length=200)
    settings = models.JSONField()

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.BigAutoField(primary_key=True)
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class UserGroup(BaseModel):
    user_id = models.CharField(max_length=254, db_comment='使用者流水號')
    group_id = models.IntegerField(db_comment='群組流水號')

    class Meta:
        managed = False
        db_table = 'user_group'
        db_table_comment = '使用者在哪個群組'

