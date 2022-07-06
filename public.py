from flask import *
from database import *
# from newcnn import *
from yolo_video import *
import uuid



public=Blueprint('public',__name__)


@public.route('/')
def home():
	return render_template('home.html')


@public.route('/about')
def about():
	return render_template('about.html')



@public.route('/fileupload',methods=['get','post'])
def fileupload():
	data={}

	if "upload" in request.form:
		i=request.files['i']
		path="static/uploads/"+str(uuid.uuid4())+i.filename
		i.save(path)
		q="insert into file values(null,'%s',curdate())"%(path)
		insert(q)
		outs=valssss(path)
		print("hhh",outs)
		flash(outs," Detected")
		return redirect(url_for('public.fileupload'))
	q="SELECT * FROM file "
	r=select(q)
	data['users']=r	
	return render_template('fileupload.html',data=data)

@public.route('/detectviolence')
def detectviolence():
	outs=valssss(0)
	print("hhh",outs)
	flash(outs," Detected")
	return render_template('home.html')