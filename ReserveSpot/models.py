# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiAccess(models.Model):
    api_key_id = models.AutoField(db_column='API_Key_ID', primary_key=True)  # Field name made lowercase.
    api_key = models.CharField(db_column='API_Key', unique=True, blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    permissions = models.TextField(db_column='Permissions', blank=True, null=True)  # Field name made lowercase.
    usage_limit = models.IntegerField(db_column='Usage_Limit', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='Created_At', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'API_Access'
        verbose_name_plural = 'API Access'


class Activities(models.Model):
    activity_id = models.AutoField(db_column='Activity_ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey('Categories', models.DO_NOTHING, db_column='Category_ID', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    age_restriction = models.IntegerField(db_column='Age_Restriction', blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.
    reviews_count = models.IntegerField(db_column='Reviews_Count', blank=True, null=True)  # Field name made lowercase.
    average_rating = models.DecimalField(db_column='Average_Rating', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    seasonal_tags = models.CharField(db_column='Seasonal_Tags', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='Created_At', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField(db_column='Updated_At', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Activities'
        verbose_name_plural = 'Activities'


class AuditLogs(models.Model):
    log_id = models.AutoField(db_column='Log_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(db_column='Action', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_Address', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Audit_Logs'
        verbose_name_plural = 'Audit Logs'


class Bookings(models.Model):
    booking_id = models.AutoField(db_column='Booking_ID', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    activity = models.ForeignKey(Activities, models.DO_NOTHING, db_column='Activity_ID', blank=True, null=True)  # Field name made lowercase.
    booking_date = models.DateField(db_column='Booking_Date', blank=True, null=True)  # Field name made lowercase.
    booking_status = models.TextField(db_column='Booking_Status', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    participants = models.IntegerField(db_column='Participants', blank=True, null=True)  # Field name made lowercase.
    total_price = models.DecimalField(db_column='Total_Price', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    special_requests = models.TextField(db_column='Special_Requests', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='Created_At', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bookings'
        verbose_name_plural = 'Bookings'


class Categories(models.Model):
    category_id = models.AutoField(db_column='Category_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categories'
        verbose_name_plural = 'Categories'


class IntegrationLogs(models.Model):
    integration_log_id = models.AutoField(db_column='Integration_Log_ID', primary_key=True)  # Field name made lowercase.
    api_key = models.ForeignKey(ApiAccess, models.DO_NOTHING, db_column='API_Key_ID', blank=True, null=True)  # Field name made lowercase.
    endpoint = models.CharField(db_column='Endpoint', blank=True, null=True)  # Field name made lowercase.
    request = models.TextField(db_column='Request', blank=True, null=True)  # Field name made lowercase.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Integration_Logs'
        verbose_name_plural = 'Integration Logs'


class LoginAttempts(models.Model):
    attempt_id = models.AutoField(db_column='Attempt_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp', blank=True, null=True)  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_Address', blank=True, null=True)  # Field name made lowercase.
    device = models.CharField(db_column='Device', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', blank=True, null=True)  # Field name made lowercase.
    risk_level = models.CharField(db_column='Risk_Level', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Login_Attempts'
        verbose_name_plural = 'Login Attempts'


class MagicLinkTokens(models.Model):
    token_id = models.AutoField(db_column='Token_ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(db_column='Token', unique=True, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='Created_At', blank=True, null=True)  # Field name made lowercase.
    is_used = models.BooleanField(db_column='Is_Used', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Magic_Link_Tokens'
        verbose_name_plural = 'Magic Link Tokens'
        
class Restaurants(models.Model):
    CUISINE_CHOICES = [
        ('Chinese', 'Chinese'),
        ('Western', 'Western'),
        ('Indian', 'Indian'),
        ('Muslim', 'Muslim'),
        ('Japanese', 'Japanese'),
        ('Italian', 'Italian'),
    ]

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    rating = models.FloatField()
    price = models.CharField(max_length=10)
    operationhours = models.CharField(max_length=20)
    description = models.TextField()
    image_url = models.URLField(max_length=200)
    cuisine = models.CharField(max_length=50, choices=CUISINE_CHOICES)
    
    class Meta:
        managed = False
        db_table = 'Restaurants'
        verbose_name_plural = 'Restaurants'

class Payments(models.Model):
    payment_id = models.AutoField(db_column='Payment_ID', primary_key=True)  # Field name made lowercase.
    booking = models.ForeignKey(Bookings, models.DO_NOTHING, db_column='Booking_ID', blank=True, null=True)  # Field name made lowercase.
    payment_method = models.TextField(db_column='Payment_Method', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    transaction_date = models.DateTimeField(db_column='Transaction_Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payments'
        verbose_name_plural = 'Payments'


class Promotions(models.Model):
    promotion_id = models.AutoField(db_column='Promotion_ID', primary_key=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    discount_percentage = models.DecimalField(db_column='Discount_Percentage', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_Date', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase.
    activity = models.ForeignKey(Activities, models.DO_NOTHING, db_column='Activity_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Promotions'
        verbose_name_plural = 'Promotions'


class Reviews(models.Model):
    review_id = models.AutoField(db_column='Review_ID', primary_key=True)  # Field name made lowercase.
    booking_id = models.IntegerField(db_column='Booking_ID', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    rating = models.DecimalField(db_column='Rating', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='Created_At', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reviews'
        verbose_name_plural = 'Reviews'


class TwoFactorAuthentication(models.Model):
    number_2fa_id = models.AutoField(db_column='2FA_ID', primary_key=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_ID', blank=True, null=True)  # Field name made lowercase.
    number_2fa_method = models.TextField(db_column='2FA_Method', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    number_2fa_status = models.TextField(db_column='2FA_Status', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier. This field type is a guess.
    created_at = models.DateTimeField(db_column='Created_At', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Two_Factor_Authentication'
        verbose_name_plural = 'Two Factor Authentication'


class Users(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, blank=True, null=True)  # Field name made lowercase.
    password_hash = models.CharField(db_column='Password_Hash', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, blank=True, null=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='Phone_Number', blank=True, null=True)  # Field name made lowercase.
    role = models.TextField(db_column='Role', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    preferences = models.TextField(db_column='Preferences', blank=True, null=True)  # Field name made lowercase.
    profile_image_url = models.CharField(db_column='Profile_Image_URL', blank=True, null=True)  # Field name made lowercase.
    social_media_links = models.TextField(db_column='Social_Media_Links', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='Created_At', blank=True, null=True)  # Field name made lowercase.
    last_login = models.DateTimeField(db_column='Last_Login', blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', blank=True, null=True)  # Field name made lowercase.
    clearance_level = models.IntegerField(db_column='Clearance_Level', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'
        verbose_name_plural = 'Users'


class Vendors(models.Model):
    vendor_id = models.AutoField(db_column='Vendor_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    contact_info = models.TextField(db_column='Contact_Info', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    ratings = models.DecimalField(db_column='Ratings', max_digits=3, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Vendors'
        verbose_name_plural = 'Vendors'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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