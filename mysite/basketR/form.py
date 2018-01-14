from django import forms
from .models import Player
# from django.core.urlresolvers import reverse 

class PlayerForm(forms.Form):
    pName = forms.CharField(max_length=20, required=True, label="名字")
    pNum  = forms.IntegerField(required=True, label="背號")
    stuID = forms.CharField(max_length=20, required=True, label="學號")

class ContestForm(forms.Form):
	#to model->contest
    # tID = forms.IntegerField()
    # def __init__(self,*args,**kwargs):
        # print("X")
        # self.tID = kwargs.pop("tID")
        # print("X3")

    print("ss")
    cName = forms.CharField(max_length=20, required=True, label="比賽名稱")
    date  = forms.DateField(required=True, label="日期")
    oppo = forms.CharField(max_length=20, required=True, label="對手")
    print("")
    # print(ttID)
    print("====================================")


    # a = Player.objects.filter(team_id=tID)
    # GENDER_CHOICES = []
    # # GENDER_CHOICES.append((u'ab',d))
    # for player in a:
    #     GENDER_CHOICES.append((player.pID,player.pName))
    # abc = forms.MultipleChoiceField(label="choose your players",choices = GENDER_CHOICES,widget = forms.CheckboxSelectMultiple())
    # print("hello")


    #to model->qRecord
 #    p2M		= forms.IntegerField(default=0)
	# p2A		= forms.IntegerField(default=0)
	# p3M		= forms.IntegerField(default=0)
	# p3A		= forms.IntegerField(default=0)
	# ftM		= forms.IntegerField(default=0)
	# ftA		= forms.IntegerField(default=0)
	# dR		= forms.IntegerField(default=0)
	# oR		= forms.IntegerField(default=0)
	# ass		= forms.IntegerField(default=0)
	# blk		= forms.IntegerField(default=0)
	# steal	= forms.IntegerField(default=0)
	# turno	= forms.IntegerField(default=0)
	# foul	= forms.IntegerField(default=0)




# class RecordForm(forms.Form):
# 	cName = forms.ChoiceField(required=True, label="比賽名稱", choices=GENDER_CHOICES)
# 	GENDER_CHOICES = (
# 		(u'M', u'Male'),
# 		(u'F', u'Female'),
# 	)

