from django.utils.translation import gettext_lazy as _


class UserConstants:
    ADMIN, STAFF = (1, 2)

    @classmethod
    def get_user_type_choices(cls):
        choices = (
            (cls.ADMIN, _("Admin")),
            (cls.STAFF, _("Staff")),
        )
        return choices