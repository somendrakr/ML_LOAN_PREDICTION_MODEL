from flask import Flask, escape, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('LOAN_PRIDICTION_MODEL.pickle', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method ==  'POST':
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        employed = request.form['employed']
        credit = float(request.form['credit'])
        area = request.form['area']
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # gender
        if (gender == "Male"):
            x[0]=1
        else:
            x[0]=0
        
        # married
        if(married=="Yes"):
            x[1] = 1
        else:
            x[1]=0

        # dependents
        if(dependents=='1'):
            x[2] = 1
            
        elif(dependents == '2'):
            x[2] = 2
           
        elif(dependents=="3+"):
            x[2] = 4
           
        else:
            x[2]=0 

        # education
        if (education=="Not Graduate"):
            x[3]=1
        else:
            x[3]=0

        # employed
        if (employed == "Yes"):
            x[4]=1
        else:
            x[4]=0

        x[5]=ApplicantIncome
        x[6]=CoapplicantIncome
        x[7]=LoanAmount
        x[8]=Loan_Amount_Term
        if credit==1:
            x[9]=1
        else:
            x[9]=0    
        
        # property type

        if(area=="Semiurban"):
            x[10]=1
        elif(area=="Urban"):
            x[10]=2
        else:
            x[10]=0


        
        
        
        for i in range(0,len(x)):
            print(x[i])
   
        prediction1 = model.predict([x])


        if(prediction1=="N"):
            prediction="No"
        else:
            prediction1="Yes"


        return render_template("prediction.html", prediction_text="loan status is {}".format(prediction1))




    else:
        return render_template("prediction.html")



if __name__ == "__main__":
    
    app.run(debug=True)