from django.db import models

import json


# Create your models here.
class Mineral(models.Model):
    '''This class is the Model for storing mineral data
data comes from the provided json file'''
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(
        max_length=255,
        unique=True,
        )
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
    group = models.CharField(default="", max_length=255)

    @staticmethod
    def load_from_json(*args):
        '''This function loads minerals into the database from the provided json document.
I considered moving this function, but I thought it better to have it here than obscured
in a strange file.

This function is now called in .migrations/0001_initial.py
'''
        with open('./assets/minerals.json', 'r', encoding='utf-8') as f:
            json_string = ''
            for line in f:
                json_string += str(line)
            json_list = json.loads(json_string)
            for dict in json_list:
                mineral = Mineral(
                    name=dict['name']
                )
                mineral.__dict__.update(dict)
                for key in dict.keys():
                    if " " in key:
                        underscore_key = "_".join(key.split(" "))
                        setattr(mineral, underscore_key, dict[key])
                mineral.save()

    @staticmethod
    def key_w_spaces(key):
        '''This class method replaces an underscore (database version)
with a space (display version)
'''
        display_list = list(key)
        display_list[0] = display_list[0].upper()
        for i, char in enumerate(display_list):
            try:
                if char == '_':
                    display_list[i] = ' '
            except IndexError:
                pass
        return "".join(display_list)

    def kv_list(self):
        '''This class method returns the stored values as a list of
key value pairs [[key,value],[key,value]]

The best, DRYest way I could think of for translating data from the model
into a template-friendly, ordered, and iterable format was a list of lists'''
        # kv_list is the main list for storing title-description pairs
        kv_list = []
        '''second_list is the secondary list of information for the XC requirement
        '''
        second_list = []
        # iterate over the dictionary
        for key in self.__dict__.keys():
            # some values shouldn't be displayed at all.
            # If it's not on the ignore list:
            if key not in [
                    '_state', 'created_at', 'id', 'image_filename',
                    'image_caption']:
                # if there's a value is not blank,
                if self.__dict__[key] is not '':
                    display_key = self.key_w_spaces(key)
                    # save the child list
                    sub_list = [display_key, self.__dict__[key]]
                    '''XC Requirement: Display the most common or important
                    details at the top of the details list.
                    You can decide on what order to display them in.
                    The other miscellaneous details can be in any order.'''
                    # display 'important' details first
                    if key in ['name', 'category', 'color']:
                        kv_list.append(sub_list)
                    # otherwise, add it to the second list
                    else:
                        second_list.append(sub_list)
        # return the combined list
        return kv_list + second_list

    def __str__(self):
        return str(self.kv_list())
