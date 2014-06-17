import pickle
from django.db                      import models
from django.db.models.signals       import pre_save
from django.dispatch                import receiver

class AccessHistory(models.Model):
    key = models.CharField(max_length=64, db_index=True)
    history_pickle = models.BinaryField()

    MAX_HISTORY_SIZE = 10

    @receiver(pre_save)
    def callback_pre_save(sender, instance, *args, **kwargs):
        try:
            instance.history_pickle =  pickle.loads(instance.history_pickle)
        except:
            instance.history_pickle = instance.history_pickle
        instance.history_pickle = pickle.dumps(instance.history_pickle)

    def get_history(self):
        try:
            value = pickle.loads(self.history_pickle)
        except:
            value = self.history_pickle
        if not isinstance(value, list):
            value = []
        return value 

    def update_history(self, page_type): 
        access_history_array = self.get_history()
        access_history_array.append(page_type) ## append an element
        if len(access_history_array) > AccessHistory.MAX_HISTORY_SIZE:
            ## delete head element
            access_history_array.pop(0)
        self.history_pickle = pickle.dumps(access_history_array)
        self.save(update_fields=['history_pickle'])

    def summarize_history(self):
        if isinstance(self.get_history(), list):
            num_page_a = self.get_history().count("page-a")
            num_page_b = self.get_history().count("page-b")
            num_page_c = self.get_history().count("page-c")
            return [num_page_a, num_page_b, num_page_c]
        else:
            return [0, 0, 0]
