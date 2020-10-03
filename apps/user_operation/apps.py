from django.apps import AppConfig


class UserOperationConfig(AppConfig):
    name = 'user_operation'
    verbose_name = "人员和处室"

    def ready(self):
        import user_operation.signals
