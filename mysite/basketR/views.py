from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
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
	#沒有登入
	if not request.user.is_authenticated:
		messages.info(request, 'Please log in first!')
		return HttpResponseRedirect('/team')
	#點到別人的隊伍
	# print(request.user.get_short_name())
	# print("hello")
	if not request.user.is_superuser:
		if not request.user.get_short_name()==tID:
			messages.info(request, 'Not able to see!')
			return HttpResponseRedirect('/team')

	# print(request.user.email);
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
			GameRecord.objects.filter(contest_id=cID).delete()
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
	if 'finalsub' in request.POST:
		cName = request.POST['cName2']
		date = request.POST['date2']
		oppo = request.POST['oppo2']
		team = request.POST['team2']

		playerss=[]
		for xxx in request.POST:
			if xxx[0]== "_":
				playerss.append(int(request.POST[xxx]))
		team = Team.objects.get(tName = team)
		c = Contest(cName = cName, date = date, oppo=oppo, team = team)
		c.save()
		
		for xd in playerss:
			player = Player.objects.get(pID=xd)
			gamerecord = GameRecord()
			gamerecord.contest = c
			gamerecord.player = player
			for i in range(1,5):
				q = str(i)
				q = "q"+q
				x = player.pID
				x = str(x)
				target = q+"+"+x+"+"
				# Q = QRecord()
				# Q.p2M =request.POST[target+'p2M']
				# Q.p2A = request.POST[target+'p2A']
				# Q.p3M =request.POST[target+'p3M']
				# Q.p3A =request.POST[target+'p3A']
				# Q.ftM =request.POST[target+'ftM']
				# Q.ftA =request.POST[target+'ftA']
				# Q.dR =request.POST[target+'dR']
				# Q.oR =request.POST[target+'oR']
				# Q.ass =request.POST[target+'ass']
				# Q.blk =request.POST[target+'blk']
				# Q.steal =request.POST[target+'steal']
				# Q.turno =request.POST[target+'turno']
				# Q.foul =request.POST[target+'foul']
				# Q.save()



				# if (QRecord.objects.get(p2M=request.POST[target+'p2M'], p2A=request.POST[target+'p2A'], p3M=request.POST[target+'p3M'], p3A=request.POST[target+'p3A'], ftM=request.POST[target+'ftM'], ftA=request.POST[target+'ftA'], dR=request.POST[target+'dR'], oR=request.POST[target+'oR'], ass=request.POST[target+'ass'], blk=request.POST[target+'blk'], steal=request.POST[target+'steal'], turno=request.POST[target+'turno'], foul=request.POST[target+'foul'] )).exists():
				try:
					Q=QRecord.objects.get(p2M=request.POST[target+'p2M'], p2A=request.POST[target+'p2A'], p3M=request.POST[target+'p3M'], p3A=request.POST[target+'p3A'], ftM=request.POST[target+'ftM'], ftA=request.POST[target+'ftA'], dR=request.POST[target+'dR'], oR=request.POST[target+'oR'], ass=request.POST[target+'ass'], blk=request.POST[target+'blk'], steal=request.POST[target+'steal'], turno=request.POST[target+'turno'], foul=request.POST[target+'foul'])
				except:
					Q = QRecord()
					Q.p2M =request.POST[target+'p2M']
					Q.p2A = request.POST[target+'p2A']
					Q.p3M =request.POST[target+'p3M']
					Q.p3A =request.POST[target+'p3A']
					Q.ftM =request.POST[target+'ftM']
					Q.ftA =request.POST[target+'ftA']
					Q.dR =request.POST[target+'dR']
					Q.oR =request.POST[target+'oR']
					Q.ass =request.POST[target+'ass']
					Q.blk =request.POST[target+'blk']
					Q.steal =request.POST[target+'steal']
					Q.turno =request.POST[target+'turno']
					Q.foul =request.POST[target+'foul']
					Q.save()



				if i==1:
					gamerecord.q1 = Q
				elif i==2:
					gamerecord.q2 = Q
				elif i==3:
					gamerecord.q3 = Q
				else:
					gamerecord.q4 = Q

			gamerecord.save()
		return HttpResponseRedirect(reverse('teamDetail', args=[tID]))
		

				

	f = PlayerForm()
	context = {'team':team, 'player':player, 'contest':contest, 'PlayerForm':f}
	return render(request, 'detail.html', context)


def record(request, tID, cID):
	if 'upd' in request.POST:
		cID = request.POST['cID']
		pID = request.POST['pID']
		quarter = request.POST['quarter']

		# game = GameRecord.objects.get(contest_id=int(cID),player_id = int(pID))
		# q = game.q1
		# if quarter == 'q2':
		# 	q = game.q2
		# elif quarter =='q3':
		# 	q = game.q3
		# elif quarter =='q4':
		# 	q = game.q4

		# q.p2M = request.POST['p2M']
		# q.p2A = request.POST['p2A']
		# q.p3M = request.POST['p3M']
		# q.p3A = request.POST['p3A']
		# q.ftM = request.POST['ftM']
		# q.ftA = request.POST['ftA']
		# q.dR = request.POST['dR']
		# q.oR = request.POST['oR']
		# q.ass = request.POST['ass']
		# q.blk = request.POST['blk']
		# q.steal = request.POST['steal']
		# q.turno = request.POST['turno']
		# q.foul = request.POST['foul']
		# q.save()



		try:
			# print("hello")
			Q=QRecord.objects.get(p2M=request.POST['p2M'], p2A=request.POST['p2A'], p3M=request.POST['p3M'], p3A=request.POST['p3A'], ftM=request.POST['ftM'], ftA=request.POST['ftA'], dR=request.POST['dR'], oR=request.POST['oR'], ass=request.POST['ass'], blk=request.POST['blk'], steal=request.POST['steal'], turno=request.POST['turno'], foul=request.POST['foul'])
		except:
			print("hello")
			Q = QRecord()
			Q.p2M =request.POST['p2M']
			Q.p2A = request.POST['p2A']
			Q.p3M =request.POST['p3M']
			Q.p3A =request.POST['p3A']
			Q.ftM =request.POST['ftM']
			Q.ftA =request.POST['ftA']
			Q.dR =request.POST['dR']
			Q.oR =request.POST['oR']
			Q.ass =request.POST['ass']
			Q.blk =request.POST['blk']
			Q.steal =request.POST['steal']
			Q.turno =request.POST['turno']
			Q.foul =request.POST['foul']
			Q.save()
		game = GameRecord.objects.get(contest_id=int(cID),player_id = int(pID))
		if quarter =='q1':
			game.q1 = Q
			game.save()
			print('1')
		elif quarter == 'q2':
			game.q2 = Q
			game.save()
			print('2')
		elif quarter =='q3':
			game.q3 = Q
			game.save()
			print('3')
		elif quarter =='q4':
			game.q4 = Q
			game.save()
			print('4')



		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

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


# def addPlayer(request,id):
#     if id:
#         r = Team.objects.get(tID=id)
#     else:
#         return HttpResponseRedirect("/addPlayer/")
#     if 'ok' in request.POST: 
#         pName = request.POST['pName']
#         pNum = request.POST['pNum']
#         stuID = request.POST['stuID']
#         c = Player(pName=pName, pNum=pNum, stuID=stuID, team=r)
#         c.save()
#     f = PlayerForm()
#     return render_to_response('addPlayer.html',locals())

# def delPlayer(request,pID):
#     if pID:
#     	Player.objects.filter(pID=pID).delete()
#     else:
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#     return render_to_response('detail.html',locals())


# def welcome(request):
#     if 'user_name' in request.GET:
#     	# 對應到HTML中的USER_NAME
#         return HttpResponse('Welcome!~'+request.GET['user_name'])   
#     #先進來
#     else:
#         return render_to_response('team.html',locals())





def addGame(request, tID):

	team = Team.objects.get(tID=tID)
	player = Player.objects.filter(team=team)
	# else:
		# return HttpResponseRedirect("/addGame/")
	# a = int(tID)
	# f = ContestForm(initial={'date':datetime.date.today()}, tID=a)
	# print(type(f))
	context = {'team': team, 'player':player, 'ContestForm':ContestForm(initial={'date':datetime.date.today()})}
	
	return render(request, 'addGame.html', context)

def gameDetail(request, tID):
    
	if 'ok' in request.POST: 
		cName = request.POST['cName']
		date = request.POST['date']
		oppo = request.POST['oppo']

		player=[]
		for xxx in request.POST:
			if xxx[0]=='_':
				player.append(int(request.POST[xxx]))
		team = Team.objects.get(tID=tID)
		c = Contest(cName=cName, date=date, oppo=oppo, team=team)
		# c.save()
		player2 = []
		for i in player:
			player2.append(Player.objects.get(pID=i))
		context = {'player':player2, 'c':c, 'team':team}
		return render_to_response('addGdetail.html',context)
	# return render_to_response('addGdetail.html',context)


def login(request):
    if request.user.is_authenticated: 
        return HttpResponseRedirect('/team')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/team')
    else:
        return render_to_response('login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/team')

