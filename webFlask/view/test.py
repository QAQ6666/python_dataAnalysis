from flask import Flask, request, render_template, session

from fun.publicFun import Infilter
from route import tableData, Histogram, weatherFiveFuture, xbkDataAnalysis, xiushi
from tools import readJson, Inverification, EmailSend
from fun.loginModel import LogVerification as lgv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
# app = Flask('__name__', static_url_path='')static_url_path: 指定静态文件路径，默认文件夹名static
chardict = tableData.watchCityCode()


# 默认为get请求
@app.route('/login')
@app.route('/login.html')
def loginTo():
    return render_template('login.html')


@app.route('/register')
@app.route('/register.html')
def registerTo():
    name = request.form["name"]
    email = request.form["email"]
    inviteCode = request.form["inviteCode"]
    password = request.form["password"]
    msg = Infilter.getinFilter(name, password)
    
    if msg:
        msg = EmailSend.EmailFormatVer(email)
        if msg:
            return render_template('404.html', msg=msg)
    else:

        return render_template('register.html')


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')


# 显式设置 get请求
@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('register.html')


@app.route('/dashboard')
@app.route('/dashboard.html')
def show_dashboard():
    imd = xbkDataAnalysis.xbkCN()
    # return app.send_static_file('/dashboard.html')发送静态文件
    return render_template('dashboard.html', img=imd)


@app.route('/user')
@app.route('/user.html')
def show_user():
    return render_template('user.html')


# 一种路由传值方法
@app.route('/table')
@app.route('/table.html')
def show_table():
    first = request.args.get('first')
    c = chardict[first]
    return render_template('table.html', chardict=c)


@app.route('/table/showeather')
def showWeather():
    city = request.args.get('city')
    code = readJson.strmatch(city)
    list = weatherFiveFuture.cityFivef(code)
    return render_template('/dynamicTem/showWeather.html', wealist=list)


@app.route('/typography')
@app.route('/typography.html')
def show_typography():
    return render_template('typography.html')


@app.route('/maps')
@app.route('/maps.html')
def show_maps():
    return render_template('maps.html')


@app.route('/notifications')
@app.route('/notifications.html')
def show_notifications():
    return render_template('notifications.html')


@app.route('/upgrade')
@app.route('/upgrade.html')
def show_upgrade():
    return render_template('upgrade.html')


# ajax调用
@app.route("/his")
def get_bar_chart():
    his = Histogram.histogram()
    return his.dump_options_with_quotes()


@app.route("/xbk")
def getxkb():
    s = xbkDataAnalysis.xbk()
    return s.dump_options_with_quotes()


@app.route("/xiu")
def getxiu():
    pie = xiushi.xius()
    return pie.dump_options_with_quotes()


@app.route("/single")
def getsingle():
    pie = xiushi.issingle()
    return pie.dump_options_with_quotes()


# 登录验证
@app.route("/loginAuthentication", methods=['POST'])
def loginAuthentication():
    username = request.form["Name"]
    Password = request.form['Password']

    msg = Infilter.getinFilter(username,Password)
    if msg:
        return render_template('404.html', msg=msg)
    else:
        u = lgv.LogVerification(username, Password)
        if not u:
            return render_template('login.html', u='登录失败，密码或用户名错误')
        else:
            session['name'] = username
            session['pwd'] = u
            return render_template('index.html', u=u)

if __name__ == '__main__':
    app.run()
