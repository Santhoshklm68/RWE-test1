class CustomAppRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'Author':
            return 'custom_db'
        return 'default'
    

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'Author':
            return 'custom_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return (
            obj1._meta.app_label == obj2._meta.app_label
            or 'custom_db' in [obj1._state.db, obj2._state.db]
        )

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'custom_db':
            return app_label == 'Author'
        elif db == 'default':
            return app_label != 'Author'
        return None
