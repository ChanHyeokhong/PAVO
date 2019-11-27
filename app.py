#한국어 영어 구분가능
#URL읽어올수 있는 기능 추가됨
from flask import Flask, request, render_template, jsonify
from gensim.summarization import summarize
import api
import lanApi
import KOR
import IU
import IE
app = Flask(__name__)
app.debug=True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/korea', methods=['POST'])
def sub():
    pass

@app.route('/generic', methods=['GET','POST'])
def submit():
    n=[]
    r=[]
    x=[]
    ty = (request.form.get('lan'))
    if request.method == 'POST' and  ty == 'ENG':
        r=request.form['textT']
        tn=api.use_api(r,'en')
        n=tn.split("\n")
        c="\n".join(n)
        z=summarize(c)
        return render_template('generic.html',z=z,tn=tn,r=r)
    elif request.method == 'POST' and ty == 'CHI':
        r=request.form['textT']
        n=r.split("\n")
        c="\n".join(n)
        z=summarize(c)
        z=api.use_api(z,'zh-tw')
        tn = api.use_api(c, 'zh-tw')
        return render_template('generic.html',z=z,tn=tn,r=r)
    elif request.method == 'POST' and ty == 'SPI':
        r=request.form['textT']
        n=r.split("\n")
        c="\n".join(n)
        z=summarize(c)
        z=api.use_api(z,'es')
        tn=api.use_api(c,'es')
        return render_template('generic.html',z=z,tn=tn,r=r)
    elif request.method == 'POST' and ty == 'ARA':
        r=request.form['textT']
        n=r.split("\n")
        c="\n".join(n)
        z=summarize(c)
        z=api.use_api(z,'ar')
        tn=api.use_api(c,'ar')
        return render_template('generic.html',z=z,tn=tn,r=r)
    elif request.method == 'POST' and ty == 'HIN':
        r=request.form['textT']
        n=r.split("\n")
        c="\n".join(n)
        z=summarize(c)
        z=api.use_api(z,'hi')
        tn=api.use_api(c,'hi')
        return render_template('generic.html',z=z,tn=tn,r=r)
    elif request.method == 'POST' and  ty == 'kENG' : # URL(K)
        t,z=IU.CU(request.form['textU'])
        r=t+z
        tn=api.use_api(z,'en')
        z=summarize(z)
        x.append(t)
        x.append(z)
        z="\n".join(x)
        z=api.use_api(z,'en')
        return render_template('generic.html', z=z,r=r,tn=tn)
    elif request.method == 'POST' and  ty == 'kKOR' :
        t,z=IU.CU(request.form['textU'])
        r=t+z
        z=summarize(z)
        x.append(t)
        x.append(z)
        z="\n".join(x)
        return render_template('generic.html', z=z,r=r)
    elif request.method == 'POST' and  ty == 'kCHI' : # URL(K)
        t,z=IU.CU(request.form['textU'])
        r=t+z
        tn=api.use_api(z,'zh-tw')
        z=summarize(z)
        x.append(t)
        x.append(z)
        z="\n".join(x)
        z=api.use_api(z,'zh-tw')
        return render_template('generic.html', z=z,r=r,tn=tn)
    elif request.method == 'POST' and  ty == 'kSPI' : # URL(K)
        t,z=IU.CU(request.form['textU'])
        r=t+z
        tn=api.use_api(z,'es')
        z=summarize(z)
        x.append(t)
        x.append(z)
        z="\n".join(x)
        z=api.use_api(z,'es')
        return render_template('generic.html', z=z,r=r,tn=tn)
    elif request.method == 'POST' and  ty == 'kARA' : # URL(K)
        t,z=IU.CU(request.form['textU'])
        r=t+z
        tn=api.use_api(z,'ar')
        z=summarize(z)
        x.append(t)
        x.append(z)
        z="\n".join(x)
        z=api.use_api(z,'ar')
        return render_template('generic.html', z=z,r=r,tn=tn)
    elif request.method == 'POST' and  ty == 'kHIN' : # URL(K)
        t,z=IU.CU(request.form['textU'])
        r=t+z
        tn=api.use_api(z,'hi')
        z=summarize(z)
        x.append(t)
        x.append(z)
        z="\n".join(x)
        z=api.use_api(z,'hi')
        return render_template('generic.html', z=z,r=r,tn=tn)
    elif request.method == 'POST' and ty == 'eENG':
        t, z = IE.CU1(request.form['textU'])
        r=t+z
        z = summarize(z)
        x.append(t)
        x.append(z)
        z = "\n".join(x)
        return render_template('generic.html', z=z,r=r)
    elif request.method == 'POST' and ty == 'eKOR':
        t, z = IE.CU1(request.form['textU'])
        r = t + z
        tn=api.use_api(z,'ko')
        z = summarize(z)
        x.append(t)
        x.append(z)
        z = "\n".join(x)
        z=api.use_api(z,'ko')
        return render_template('generic.html', z=z,r=r,tn=tn)
    elif request.method == 'POST' and ty == 'eCHI':
        t, z = IE.CU1(request.form['textU'])
        r = t + z
        tn = api.use_api(z, 'zh-tw')
        z = summarize(z)
        x.append(t)
        x.append(z)
        z = "\n".join(x)
        z = api.use_api(z, 'zh-tw')
        return render_template('generic.html', z=z,r=r,tn=tn)
    elif request.method == 'POST' and ty == 'eSPI':
        t, z = IE.CU1(request.form['textU'])
        r=t+z
        tn = api.use_api(z, 'es')
        z = summarize(z)
        x.append(t)
        x.append(z)
        z = "\n".join(x)
        z = api.use_api(z, 'es')
        return render_template('generic.html', z=z,r=r,tn=tn)
    elif request.method == 'POST' and ty == 'eARA':
        t, z = IE.CU1(request.form['textU'])
        r = t + z
        tn = api.use_api(z, 'ar')
        z = KOR.kor(z)
        x.append(t)
        x.append(z)
        z = "\n".join(x)
        z = api.use_api(z, 'ar')
        return render_template('generic.html', z=z,r=r,tn=tn)
    elif request.method == 'POST' and ty == 'eHIN':
        t, z = IE.CU1(request.form['textU'])
        r = t + z
        tn = api.use_api(z, 'hi')
        z = summarize(z)
        x.append(t)
        x.append(z)
        z = "\n".join(x)
        z = api.use_api(z, 'hi')
        return render_template('generic.html', z=z,r=r,tn=tn)
    else :
        r = request.form['textT']
        tn=api.use_api(r,'ko')
        n=tn.split("\n")
        c="\n".join(n)
        z = KOR.kor(c)
        return render_template('generic.html',z=z,r=r,tn=tn)

@app.errorhandler(500)
def page_not_found(error):
    app.logger.error(error)
    return render_template('page_not_found.html'), 500


if __name__ == '__main__':
	app.run(debug=True)
