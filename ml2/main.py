from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('index1.html')

@app.route('/add',methods=['POST','GET'])
def add():
    if request.method == 'GET':
        return "<h1>Go to <a href='/'>Home</a></h1>"
    try:
        import pandas as pd
        import joblib
        g = joblib.load("model.h5") 
        f = g.feature_names_in_
        f1 = str(request.form['Flow_ID'])
        s = request.form['Source_IP']
        print("Source_IP",s)
        p = str(request.form['Source_Port'])
        d = request.form['Destination_Port']
        b = str(request.form['Destination_IP']) 
        t = str(request.form['Timestamp']) 
        l = str(request.form['Label'])
        s1= float(request.form['Flow_Bytes_per_second'])
        fp = float(request.form['Flow_Packets_per_second'])
        fwp=float(request.form['Fwd_Packets_per_second'])

        s_data ={
            'Flow_ID': f1,
            'Source_IP': s,
            'Source_Port': p,
            'Destination_IP': b,
            'Destination_Port': d,
            'Timestamp': t,
            'Label': l,
            'Flow_Bytes_per_second': s1,
            'Flow_Packets_per_second': fp,
            'Fwd_Packets_per_second': fwp
        }

        s_data= pd.DataFrame([s_data])
        s_data = pd.get_dummies(s_data)
        s_data = s_data.reindex(columns=f, fill_value=0)
        
        pre = g.predict(s_data)
        print(pre) 
        if pre == 1:
            result = "cyber_attack"
        else:
            result = "not cyber_attack"
    except ValueError:
        result = "Invalid input! Please enter numbers only"
            
    return redirect(url_for('result',result=result))

@app.route('/result')
def result():
    result = request.args.get('result')
    return render_template('result.html',result=result)

if __name__ == '__main__':
    app.run(debug=True,port=8080)
