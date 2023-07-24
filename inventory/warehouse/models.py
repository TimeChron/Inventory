from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import logging

logger = logging.getLogger("warehouse_models")

# Abstract Warehouse
class Warehouse(models.Model):
    name = models.CharField(max_length = 45)
    store_code = models.CharField(max_length = 6, unique = True)
    address = models.TextField()
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    pincode = models.CharField(max_length = 6)
    publish = models.BooleanField(default=False)
    published_at = models.DateTimeField(null = True, blank=True)
    active = models.BooleanField(default=False)
    published_by = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)

    class Meta:
        abstract = True

    def publish_warehouse(self):
        pass

    def active_warehouse(self):
        pass

    def save(self, *args, **kwargs):
        if not self.store_code:
            # Load the last object
            last_object = Warehouse.objects.last()
            if last_object:
                # Load the last object code
                last_object_code = last_object.store_code
                code_constituent_list=last_object.split('-')
                next_code_number = int(code_constituent_list[-1]) + 1
            else:
                new_code_number = 1001
            store_code = 'WH-'+str(new_code_number)
            self.store_code = store_code
        super().save(*args, **kwargs)

class Store(Warehouse):

    warehouse_type = models.CharField(max_length=30, default='Store')

    class Meta:
        db_table = 'store'
        constraints = [
            models.UniqueConstraint(fields=['store_code', 'warehouse_type'], name='composite_key_store_code_warehouse_type')
        ]

    def value_of(self, obj, key):
        if obj and (isinstance(obj, tuple) or isinstance(obj, list)):
            logger.info('===The provided instance is either of tuple or list===')
            return None
        if obj and obj.get(key):
            return obj[key]
        else:
            return None

    def filter_data(self, data_dict):
        ## Function to filter out the datadict
        ## Return the filtered data

        logger.info("===Data dict for the filteration===%s"%data_dict)
        filtered_data_dict = {}
        for key in data_dict.keys():
            value = self.value_of(data_dict, key)
            filtered_data_dict.update({
                    key: value if value else ''
                })
        logger.info("===Filtered data map===%s"%filtered_data_dict)
        return filtered_data_dict

    def save(self, *args, **kwargs):
        # Add any specific logic to this save
        super().save(*args, **kwargs)

    @classmethod
    def create(cls, **data):
        # Function to create warehouse

        #Load the kwargs
        data_dict = dict(kwargs)
        filtered_data_dict = self.filter_data(data_dict)
        store_instance = supe(**filtered_data_dict)
        return store_instance

    def activate_warehouse(self, deactivate = False):
        if not deactivate:
            self.active = True
            logger.warning('===Warehouse has been activated===%s'%self.store_code)
        else:
            self.active = False
            logger.warning('===Warehouse has been deactivated===%s'%self.store_code)
        self.save()

        return True

    def publish_warehouse(self, user):
        ## The warehouse can only be published ones
        ## Once published can not be unpublished can only be activated and deactivated

        self.publish = True
        self.published_at = timezone,now()
        self.published_by = user

        self.save()

        return True



