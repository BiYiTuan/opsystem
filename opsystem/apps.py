# encoding: utf-8
from django.apps import AppConfig
from django.core import checks
from django.utils.translation import ugettext_lazy as _
import xadmin


class XAdminConfig(AppConfig):
    """Simple AppConfig which does not do automatic discovery."""

    name = 'xadmin'
    # verbose_name = _("Administration")
    verbose_name = u"账号菜单"
    verbose_name_plural = verbose_name

    def ready(self):
        self.module.autodiscover()
        setattr(xadmin,'site',xadmin.site)