from django.db import models

# Create your models here.

class Team(models.Model):
	tID 	= models.AutoField(primary_key=True)
	tName 	= models.CharField(max_length=50)
	def __str__(self):
		return self.tName

class Player(models.Model):
	pID 	= models.AutoField(primary_key=True)
	team    = models.ForeignKey(
		Team,
		models.SET_NULL,
		blank=False,
		null=True,
	)
	pNum	= models.IntegerField(blank=False) #背號
	# pNum	= models.IntegerField(blank=False) #背號
	pName 	= models.CharField(max_length=50)
	stuID	= models.CharField(max_length=15)
	def __str__(self):
		return self.pName

class Contest(models.Model):
	cID		= models.AutoField(primary_key=True)
	team    = models.ForeignKey(
		Team,
		models.SET_NULL,
		blank=False,
		null=True,
	)
	cName	= models.CharField(max_length=15) #ex:大資盃、台大盃
	date	= models.DateField()
	oppo	= models.CharField(max_length=20) #ex:台大電機
	def __str__(self):
		retName=self.cName+"_"+self.team.tName+"vs"+self.oppo
		return retName

class QRecord(models.Model):
	qID 	= models.AutoField(primary_key=True)
	p2M		= models.IntegerField(default=0)
	p2A		= models.IntegerField(default=0)
	p3M		= models.IntegerField(default=0)
	p3A		= models.IntegerField(default=0)
	ftM		= models.IntegerField(default=0)
	ftA		= models.IntegerField(default=0)
	dR		= models.IntegerField(default=0)
	oR		= models.IntegerField(default=0)
	ass		= models.IntegerField(default=0)
	blk		= models.IntegerField(default=0)
	steal	= models.IntegerField(default=0)
	turno	= models.IntegerField(default=0)
	foul	= models.IntegerField(default=0)

class GameRecord(models.Model):
	player 	= models.ForeignKey(
		Player,
		models.SET_NULL,
		blank=False,
		null=True,
	)
	contest = models.ForeignKey(
		Contest,
		models.SET_NULL,
		blank=False,
		null=True,
	)
	q1		= models.ForeignKey(
		QRecord,
		models.SET_NULL,
		related_name='q1',
		blank=False,
		null=True,
	)
	q2		= models.ForeignKey(
		QRecord,
		models.SET_NULL,
		related_name='q2',
		blank=False,
		null=True,
	)
	q3		= models.ForeignKey(
		QRecord,
		models.SET_NULL,
		related_name='q3',
		blank=False,
		null=True,
	)
	q4		= models.ForeignKey(
		QRecord,
		models.SET_NULL,
		related_name='q4',
		blank=False,
		null=True,
	)
	def __str__(self):
		retName=self.contest.cName+'_'+self.player.team.tName+self.player.pName+"vs"+self.contest.oppo
		return retName
