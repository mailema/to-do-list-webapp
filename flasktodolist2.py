import os
from flask import Flask,render_template,request,redirect

tasks_container=[]

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html',tasks_container=tasks_container)

@app.route('/add', methods=['POST'])
def add_task():
    task=request.form['input_name']
    if task!='':
        tasks_container.append(task)
    return redirect('/')
    
@app.route('/delete/<int:id>')
def delete_task(id):
    tasks_container.pop(id)
    return redirect('/')
        

if __name__=='__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)