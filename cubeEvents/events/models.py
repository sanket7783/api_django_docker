from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from jsonfield import JSONField

from datetime import datetime,timedelta

class Event(models.Model):
    user_id = models.IntegerField(null=False)
    ts = models.CharField(max_length=50,null=False)
    lat_long = models.CharField(max_length=100)
    noun = models.CharField(max_length=10)
    verb = models.CharField(max_length=10)
    time_spent_on_the_screen = models.IntegerField()
    properties = JSONField()

    def __str__(self):
        return str(self.user_id)+" "+self.verb

feedback_queue = []

# signal receiver
@receiver(pre_save,sender=Event)
def CheckFirstEntry(sender,instance,**kwargs):
    user_id_list = sender.objects.all().values("user_id").distinct()
    data = {"user_id":instance.user_id}
    print("**************************************************")
    if instance.verb=="pay":
        feedback_queue.append(instance)
    if data not in user_id_list:
        print("New entry")
    else:
        print("already present")
        five_mins = timedelta(seconds=300)
        time_before_five_mins = datetime.now()-five_mins
        txns = sender.objects.filter(user_id=instance.user_id) & sender.objects.filter(verb="pay") & sender.objects.filter(ts__gte=time_before_five_mins) 
        sum = 0
        
        for txn in txns[:5]:
            sum+=txn.properties["value"]
        #import pdb;pdb.set_trace()
        if sum>=20000:
            print("transaction exceeeds 20K")




    
