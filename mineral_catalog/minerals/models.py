from django.db import models


def key_w_spaces(key):
    display_list = list(key)
    display_list[0] = display_list[0].upper()
    for i, char in enumerate(display_list):
        if char == '_':
            display_list[i] = ' '
            display_list[i+1] = display_list[i+1].upper()
    return "".join(display_list)+':'


# Create your models here.
class Mineral(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(
        max_length=255,
        unique=True,
        )
    name = models.CharField(max_length=255)
    image_filename = models.CharField(max_length=255)
    image_caption = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    formula = models.CharField(max_length=255)
    strunz_classification = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    crystal_system = models.CharField(max_length=255)
    unit_cell = models.CharField(max_length=255)
    crystal_symmetry = models.CharField(max_length=255)
    cleavage = models.CharField(max_length=255)
    mohs_scale_hardness = models.CharField(max_length=255)
    luster = models.CharField(max_length=255)
    streak = models.CharField(max_length=255)
    diaphaneity = models.CharField(max_length=255)
    optical_properties = models.CharField(max_length=255)
    refractive_index = models.CharField(max_length=255)
    crystal_habit = models.CharField(max_length=255)
    specific_gravity = models.CharField(max_length=255)

    def keys(self):
        return (self.__dict__.keys())

    def values(self):
        return (self.__dict__.values())

    def kv_list(self):
        kv_list = []
        for key in self.__dict__.keys():
            if key not in ['_state', 'created_at', 'id', 'image_filename', 'image_caption']:
                if self.__dict__[key] is not '':
                    display_key = key_w_spaces(key)
                    sub_list = [display_key, self.__dict__[key]]
                    kv_list.append(sub_list)
        return kv_list

    def __str__(self):
        return str(self.__dict__)
