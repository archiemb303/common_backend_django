#from abc import ABC
from genericbackend import settings
from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    location = settings.AWS_PUBLIC_MEDIA_LOCATION
    file_overwrite = False
    default_acl = 'public-read'
    file_overwrite = False
    custom_domain = False


class PrivateMediaStorage(S3Boto3Storage):
    location = settings.AWS_PRIVATE_MEDIA_LOCATION
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False


class PublicPreMediaStorage(S3Boto3Storage):
    location = settings.AWS_PRE_MEDIA_LOCATION
    file_overwrite = False
    default_acl = 'public-read'
    file_overwrite = False
    custom_domain = False
