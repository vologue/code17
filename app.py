from flask import Flask,render_template,request, redirect, url_for
import MySQLdb
from jinja2 import Template
import json
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
from werkzeug import secure_filename
import os
app = Flask(__name__)
app.config['MONGO_DBNAME']  ='Interact'

app.config.update(
	UPLOAD_FOLDER='/uploads',
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'raghavp98@gmail.com',
	MAIL_PASSWORD = 'aundriul98'
	)
mongo = PyMongo(app)
mail = Mail(app)

@app.route('/job-dec/<id>')
def jdec(id):
	ids=id.split('-')
	con=MySQLdb.connect("localhost","vologue","quasaro98","Interract")
	cur = con.cursor()
	que="select Name from Company where CID like '%s'" %(ids[0])
	cur.execute(que)
	j=cur.fetchall()
	l=[]
	open=mongo.db.jobs
	for i in open.find():
		if(i['cid']==ids[0] and i['jid']==ids[1]):
			l=i
			break
	return render_template('jdec.html',job=l)
	

@app.route('/applicants/<id>')
def works(id):
	ids=id.split('-')
	lis=[]
	stages=[]
	op=mongo.db.list
	for m in op.find():
		if(ids[0]==m['cid']):
			jbs=m['opns']
			for op in jbs:
				if(op['jid']==ids[1]):
					stages=op['stages']
	for staj in range(1,9):
		if((stages['%d'%(staj)])=="Rename Stage"):
			cout=staj
			break

	return render_template('stages.html',stage=stages,cid=ids[0],jid=ids[1],count=cout)

@app.route('/applicants/update/<id>')
def getapp(id):
	ids=id.split('-')
	open=mongo.db.Applicant
	lis=[]
	for i in open.find():
		j=i['jobs']
		for k in j:
			if(ids[1]==k['jid'] and ids[0]==k['cid']):		
				lis.append({'aid':i['aid'],'name':i['name'],'email':i['email'],'status':k['status'],'cid':k['cid'],'jid':k['jid']})
	list1=json.dumps(lis)
	return list1

@app.route('/applicants/tables/<id>')
def showapp(id):
	ids=id.split('-')
	lis=[]
	stages=[]
	op=mongo.db.list
	for m in op.find():
		if(ids[0]==m['cid']):
			jbs=m['opns']
			for op in jbs:
				if(op['jid']==ids[1]):
					stages=op['stages']
	for staj in range(1,9):
		if((stages['%d'%(staj)])=="Rename Stage"):
			cout=staj
			break

	return render_template("tables.html",stage=stages,cid=ids[0],jid=ids[1])



@app.route('/CreateOpening/<coid>')
def showform(coid):
	return render_template('form2.html', cide=coid)

@app.route('/register')
def acc():
	return render_template("register.html")

@app.route('/createacc',methods=['POST'])
def ccreate():
	con=MySQLdb.connect("localhost","vologue","quasaro98","Interract")
	cur = con.cursor()
	cname=request.form['name']
	email=request.form['email']
	pas=request.form['pass']
	hr=request.form['hr']
	cont=request.form['cont']
	que="insert into Company (Name,email,HRname,PNO,jopns) Value('%s','%s','%s','%s',%d)" %(cname,email,hr,cont,0)
	jo=[]
	cur.execute(que)
	con.commit()
	que="select CID from Company where CID=(SELECT max(CID) FROM Company)"
	cur.execute(que)
	c=cur.fetchall()
	k=c[0]
	l=k[0]
	a=l%10
	l=l/10
	b=l%10
	l=l/10
	m="%d%d%d" %(l,b,a)
	open=mongo.db.Company
	open.insert({
		"name":cname,
		"cid":m,
		"jobs":jo,
		"user":email,
		"pass":pas
		})
	op=mongo.db.list
	op.insert({
		"cid":m,
		"opns":[]
		})
	op=mongo.db.jobs
	op.insert({
		"cid":m,
		"jobs":jo
		})
	return render_template("login.html")


@app.route('/company/<email>')
def comp(email):
	con=MySQLdb.connect("localhost","vologue","quasaro98","Interract")
	cur = con.cursor()
	que="select CID,Name,Email,jopns from Company where Email like '%s'" %(email)
	cur.execute(que)
	m=cur.fetchall()
	c=m[0][0]
	h=c%10
	c=c/10
	g=c%10
	c=c/10
	cid="%d%d%d" %(c,g,h)	
	l=[]
	open=mongo.db.jobs
	for i in open.find():
		if(i['cid']==cid):
			l.append(i)
	print(l)
	return render_template("Dashboard.html", ci=m,k=l)
	
@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/loginreq', methods=['POST'])
def logcheck():
	usr=request.form['email']
	pas=request.form['pass']
	open=mongo.db.Company
	for i in open.find():
		if (i['pass']==pas and i['user']==usr):
			return redirect("/company/%s" %(usr))
	return "fail"

@app.route('/listjobs')
def jobs():
	lis=[]
	open=mongo.db.jobs
	lis=open.find()
	return render_template("res.html",jbs=lis)

@app.route('/updateget',methods=['POST'])
def update():
	stat=request.json['stage']
	ind=request.json['ind']
	open=mongo.db.Applicant
	op=mongo.db.jobs
	jbs=op.find()
	email=[]
	for i in range (0,len(ind)):
		if(ind[i]!=''):
			open.update({'aid':stat[i]['aid'],
			'jobs.cid':stat[i]['cid'],
			'jobs.jid':stat[i]['jid']},
			{'$set':{'jobs.$.status':ind[i]}},
			upsert=False,multi=True)
			stage=ind[i]
			email.append(stat[i]['email'])
	for j in jbs: 
		if(j['jid']==stat[0]['jid'] and j['cid']==stat[0]['cid']):
			sub=j['sub%s'%(stage)]
			mailc=j['mail%s'%(stage)]
			msg = Message('%s'%sub,sender="raghavp98@gmail.com",recipients=email)
			msg.body = "%s" %mailc           
			mail.send(msg)


	print(email)
	return "suc"

@app.route('/<id>/applicant', methods=['POST'])
def applicant(id):
	ids=id.split('-')
	name=request.form['name']
	email=request.form['email']
	dob=request.form['dob']
	loc=request.form['location']
	pno=request.form['number']
	ans=request.form['ans']
	stdate=request.form['startd']
	empstat=request.form['empstat']
	f = request.files['file']
	con=MySQLdb.connect("localhost","vologue","quasaro98","Interract")
	cur = con.cursor()
	flag=False
	que="insert into Applicant (Name,Email) values('%s','%s')" %(name,email)
	try:
		cur.execute(que)
		con.commit()
		flag=True
	except:
		return ("exists")
	finally:
		que="select Aid from Applicant where email like '%s'" %(email)
		cur.execute(que)
		res=cur.fetchall()
		l=res[0][0]
		a=l%10
		l=l/10
		b=l%10
		l=l/10
		c=l%10
		l=l/10
		aid="%d%d%d%d" %(l,c,b,a) 
	f.save(secure_filename(aid+'.pdf'))	
	open=mongo.db.Applicant
	if(flag):
		open.insert({
			'name':name,
			'aid':aid,
			'email':email,
			'dob':dob,
			'location':loc,
			'pno':pno,
			'empstat':empstat,
			'jobs':[{
				'jid':ids[1],
				'cid':ids[0],
				'status':'1',
				'ans':ans,
				'sdate':stdate
				}]
			})
	else:
		open.update({'aid':aid},{"$push":{'jobs':{'jid':ids[1],'cid':ids[0],'status':'1'}}},upsert=False,multi=False)
	open=mongo.db.jobs
	jbs=open.find()
	for j in jbs: 
		if(j['jid']==ids[1] and j['cid']==ids[0]):
			sub=j['sub1']
			mailc=j['mail1']
			msg = Message('%s'%sub,sender="raghavp98@gmail.com",recipients=[email])
			msg.body = "%s" %mailc           
			mail.send(msg)
	return "success"

@app.route('/apply/<id>')
def apply(id):
	ids=id.split('-')
	con=MySQLdb.connect("localhost","vologue","quasaro98","Interract")
	cur = con.cursor()
	que="select Name from Company where CID like '%s'" %(ids[0])
	cur.execute(que)
	j=cur.fetchall()
	l=[]
	open=mongo.db.jobs
	for i in open.find():
		if(i['cid']==ids[0] and i['jid']==ids[1]):
			l=i
			q=i['cques']
			break
	lis=[]
	qu=q[1:]
	q=qu[:-1]
	ques=q.split('"')
	qu=[]
	for i in ques:
		if(i != '' and i != ','):
			qu.append(i)
	num=len(qu)
	#return"apply for job %s <br> offered by company %s" %(ids[1],j[0][0])
	return render_template("application.html",jbs=l,c=j[0][0],cid=ids[0],q=qu,n=num)



@app.route('/createop/<cid>', methods=['POST','GET'])
def getdat(cid):
	 con=MySQLdb.connect("localhost","vologue","quasaro98","Interract")
	 cur = con.cursor()
	 que="select jopns,email from Company where CID like '%s'" %(cid)
	 cur.execute(que)
	 j=cur.fetchall()
	 email=j[0][1]
	 l=j[0][0]
	 a=l%10
	 l=l/10
	 b=l%10
	 l=l/10
	 jtitle= request.form['title1']
	 prole = request.form['primaryrole']
	 jtype= request.form['type']
	 skill= request.form.getlist('skills')
	 loca = request.form['location']
	 exp = request.form['experience']
	 salf= request.form['salf']
	 salt= request.form['salt']
	 sal="%s-%s" %(salf,salt)
	 for it in skill:
	 	print(it)
	 	print('\n')
	 try:
	 	ph= request.form['ph']
	 	res= request.form['res']
	 except:
	 	if(ph=="on"):
	 		res="off"
	 	elif(res=="on"):
	 		ph=="off"
	 	else:
	 		ph="off"
	 		res="off"
	 try:
	 	cqtype=request.form['cqty']
	 	cques=request.form['cques']
	 except:
	 	cques=""
	 	cqtype=""
	 currency= request.form['curr']
	 jdec= request.form['jdec']
	 sub1= request.form['st1sub']
	 mail1=request.form['st1mail']
	 sub2= request.form['st2sub']
	 mail2=request.form['st2mail']
	 sub3= request.form['st3sub']
	 mail3=request.form['st3mail']
	 sub4= request.form['st4sub']
	 mail4=request.form['st4mail']
	 sub5= request.form['st5sub']
	 mail5=request.form['st5mail']
	 st1n=request.form['st1n']
	 st1t=request.form['st1t']
	 st2n=request.form['st2n']
	 st2t=request.form['st2t']
	 st3n=request.form['st3n']
	 st3t=request.form['st3t']
	 st4n=request.form['st4n']
	 st4t=request.form['st4t']
	 st5n=request.form['st5n']
	 st5t=request.form['st5t']
	 st6n=request.form['st6n']
	 st6t=request.form['st6t']
	 st7n=request.form['st7n']
	 st7t=request.form['st7t']
	 st8n=request.form['st8n']
	 st8t=request.form['st8t']
	 link="/apply/%s-%d%d%d" %(cid,l,b,a)
	 open=mongo.db.jobs
	 open.insert({'cid':cid,
	 		"jid": "%d%d%d" %(l,b,a),
	 			  "Job Tiltle" : jtitle,
	 			  "Role" : prole,
	 			  "Job Type" : jtype,
	 			  "Skills Req" : skill,
	 			  "loacation" : loca,
	 			  "Experience" : exp,
	 			  "Salary range":sal,
	 			  "Currency" : currency,
	 			  "Job Decription":jdec,
	 			  "reqphone":ph,
	 			  "reqres":res,
	 			  "link":link,
	 			  "cques":cques,
	 			  "cqtype":cqtype,
	 			  "sub1":sub1,
	 			  "mail1":mail1,
	 			  "sub2":sub2,
	 			  "mail2":mail2,
	 			  "sub3":sub3,
	 			  "mail3":mail3,	
	 			  "sub4":sub4,
	 			  "mail4":mail4,
	 			  "sub5":sub5,
	 			  "mail5":mail5})
	 que="Update Company set jopns=jopns+1 where CID='%s'" %(cid)
	 cur.execute(que)
	 con.commit()
	 op=mongo.db.list
	 op.update({'cid':cid},{"$push":{'opns':{"jid":"%d%d%d" %(l,b,a),
	 			"stages":{'1':st1n,
	 					  '2':st2n,
	 					  '3':st3n,
	 					  '4':st4n,
	 					  '5':st5n,
	 					  '6':st6n,
	 					  '7':st7n,
	 					  '8':st8n	}
	 			}}},upsert=False,multi=False)
	 return redirect("/company/%s" %(email))

if __name__ == '__main__':
   app.run(debug = True,host ="0.0.0.0")

