from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import datetime

from .models import Team, Player, Contest, QRecord, GameRecord
from .form import PlayerForm, ContestForm
# Create your views here.
def listteam(request):
	team_list = Team.objects.all()

	# team_list.append(team)

	context = {'team_list': team_list}
	return render(request, 'team.html', context)

def listrecord(request):
	record_list = GameRecord.objects.all()

	# team_list.append(team)

	context = {'record_list': record_list}
	return render(request, 'listrecord.html', context)

def detail(request, tID):
	team = Team.objects.get(tID=tID)
	player = Player.objects.filter(team=team)
	contest = Contest.objects.filter(team=team)

	if 'ok' in request.POST:
		pName = request.POST['pName']
		pNum = request.POST['pNum']
		stuID = request.POST['stuID']
		c = Player(pName=pName, pNum=pNum, stuID=stuID, team=team)
		c.save()
		# return HttpResponseRedirect("/team/")
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	if 'delPlayer' in request.POST:
		pID = request.POST['jj']
		if pID:
			if len(GameRecord.objects.filter(player_id=pID))  == 0:
				Player.objects.filter(pID=pID).delete()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	if 'delGame' in request.POST:
		cID = request.POST['gID']
		if cID:
			Contest.objects.filter(cID=cID).delete()
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	if 'upd' in request.POST:
		pID = request.POST['jj']
		pName = request.POST['pName']
		pNum = int(request.POST['pNum'])
		stuID = request.POST['stuID']
		if pID:
			Player.objects.filter(pID=pID).update(pName=pName, pNum = pNum, stuID = stuID)
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


	f = PlayerForm()
	context = {'team':team, 'player':player, 'contest':contest, 'PlayerForm':f}
	return render(request, 'detail.html', context)


def record(request, tID, cID):
	team = Team.objects.get(tID=tID)
	# player = Player.objects.filter(team=team)
	# contest = Contest.objects.filter(team=team)
	c1 = Contest.objects.get(cID=cID)
	game = GameRecord.objects.filter(contest=c1)
	allgame = []
	for rc in game:
		player  = rc.player
		p2M		= rc.q1.p2M + rc.q2.p2M + rc.q3.p2M + rc.q4.p2M
		p2A		= rc.q1.p2A + rc.q2.p2A + rc.q3.p2A + rc.q4.p2A
		p3M		= rc.q1.p3M + rc.q2.p3M + rc.q3.p3M + rc.q4.p3M
		p3A		= rc.q1.p3A + rc.q2.p3A + rc.q3.p3A + rc.q4.p3A
		ftM		= rc.q1.ftM + rc.q2.ftM + rc.q3.ftM + rc.q4.ftM
		ftA		= rc.q1.ftA + rc.q2.ftA + rc.q3.ftA + rc.q4.ftA
		dR		= rc.q1.dR + rc.q2.dR + rc.q3.dR + rc.q4.dR
		oR		= rc.q1.oR + rc.q2.oR + rc.q3.oR + rc.q4.oR
		ass		= rc.q1.ass + rc.q2.ass + rc.q3.ass + rc.q4.ass
		blk		= rc.q1.blk + rc.q2.blk + rc.q3.blk + rc.q4.blk
		steal	= rc.q1.steal + rc.q2.steal + rc.q3.steal + rc.q4.steal
		turno	= rc.q1.turno + rc.q2.turno + rc.q3.turno + rc.q4.turno
		foul	= rc.q1.foul + rc.q2.foul + rc.q3.foul + rc.q4.foul	
		# 衍生
		totalpt = p2M*2 + p3M*3 + ftM

		if (p2M+p2A) == 0:
			p2average = 0
		else:
			p2average = round(100*p2M/(p2M+p2A))

		if (p3M+p3A) == 0:
			p3average = 0
		else:
			p3average = round(100*p3M/(p3M+p3A))

		if (ftM+ftA) == 0:
			ftaverage = 0
		else:
			ftaverage = round(100*ftM/(ftM+ftA))

		package = {'player':player, 'p2M':p2M, 'p2A':p2A, 'p3M':p3M, 'p3A':p3A, 'ftM':ftM, 'ftA':ftA, 'dR':dR, 'oR':oR, 'ass':ass, 'blk':blk, 'steal':steal, 'turno':turno, 'foul':foul, 'totalpt':totalpt, 'p2average':p2average, 'p3average':p3average, 'ftaverage':ftaverage}
		allgame.append(package)



		context = {'team':team, 'game':game, 'c1':c1, 'allgame':allgame}

	return render(request, 'record.html', context)


# def addPlayer(request):
#     ctx = {}
#     if request.POST:
#         team = Team.objects.filter(tID=1)
#         pName = request.POST['pName']
#         pNum = request.POST['pNum']
#         stuID = request.POST['stuID']
#         Player.objects.create(team=team, pName=pName, pNum=pNum, stuID=stuID)
#     return render(request, "listteam.html", ctx)

# from django import forms

# class PlayerForm(forms.ModelForm):
#     class Meta:
#         model = Player
#         fields = ['pID', 'team', 'pName', 'pID', 'stuID']

# from django.http import HttpResponseRedirect

# def addPlayer(request):
#     if request.method == 'POST':
#         form = PlayerForm(request.POST)
#         if form.is_valid():
#             new_article = form.save()
#             return HttpResponseRedirect('/article/' + str(new_article.pk))

#     form = ArticleForm()
#     return render(request, 'create_article.html', {'form': form})

def addPlayer(request,id):
    if id:
        r = Team.objects.get(tID=id)
    else:
        return HttpResponseRedirect("/addPlayer/")
    if 'ok' in request.POST: 
        pName = request.POST['pName']
        pNum = request.POST['pNum']
        stuID = request.POST['stuID']
        c = Player(pName=pName, pNum=pNum, stuID=stuID, team=r)
        c.save()
    f = PlayerForm()
    return render_to_response('addPlayer.html',locals())

def delPlayer(request,pID):
    if pID:
    	Player.objects.filter(pID=pID).delete()
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render_to_response('detail.html',locals())


def welcome(request):
    if 'user_name' in request.GET:
    	# 對應到HTML中的USER_NAME
        return HttpResponse('Welcome!~'+request.GET['user_name'])   
    #先進來
    else:
        return render_to_response('team.html',locals())





def addGame(request, tID):
	if tID:
		team = Team.objects.get(tID=tID)
		player = Player.objects.filter(team=team)
	# else:
		# return HttpResponseRedirect("/addGame/")

	f = ContestForm(initial={'date':datetime.date.today()})
	context = {'team': team, 'player':player, 'ContestForm':f}
	
	return render(request, 'addGame.html', context)

def gameDetail(request, tID):
    
	if 'ok' in request.POST: 
		cName = request.POST['cName']
		date = request.POST['date']
		oppo = request.POST['oppo']
		player = request.POST.getlist('abc')
		team = Team.objects.get(tID=tID)
		c = Contest(cName=cName, date=date, oppo=oppo, team=team)
		# c.save()

		context = {'player':player}
	return render_to_response('addGdetail.html',context)
