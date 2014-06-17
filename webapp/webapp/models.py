import pickle
from django.db                      import models
from django.db.models.signals       import pre_save
from django.dispatch                import receiver

class AccessHistory(models.Model):
    key = models.CharField(max_length=64, db_index=True)
    history_pickle = models.BinaryField()

    @receiver(pre_save)
    def callback_pre_save(sender, instance, *args, **kwargs):
        try:
            instance.history_pickle =  pickle.loads(instance.history_pickle)
        except:
            instance.history_pickle = instance.history_pickle
        instance.history_pickle = pickle.dumps(instance.history_pickle)

    def get_history(self):
        try:
            return pickle.loads(self.history_pickle)
        except:
            return self.history_pickle
