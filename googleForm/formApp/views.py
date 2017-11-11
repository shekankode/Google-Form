from models import FormHeader
from models import Questions
from models import Answers
from models import QuesAns
from django.shortcuts import render
# Create your views here.
def createForm(request):
    #Form = FormHeader.objects.all()
    newForm = FormHeader()
    newForm.title = request.POST['title']
    newForm.form_description = request.POST['form_description']
    newForm.save()
    forms = FormHeader.objects.all()
    return render(request, "main.html", {'formsVar':forms})

def formMain(request):
    return  render(request, "main.html")

def addQues(request):
    if request.method == 'POST':

        QuestionList= request.POST.getlist('QuestionList')
    else:
        print "testing"
    for i in QuestionList:
      newQues=Questions()
      newQues.ques=i
      newQues.save()
      Q=Questions.objects.all()
    return render(request,"preview.html",{'Q1':Q})
    #return render(request,"ques.html")

def test(request):
    return render(request,"ques.html")


def testans(request):
    return render(request,"answers.html")

def addAns(request):
    fieldTypeVal= request.POST['element']
    if request.method == 'POST':
        AnswerList=request.POST.getlist('AnswerList')
    else:
        print "try again !"
    for i in AnswerList:
        newAns=Answers()
        newAns.fieldType=fieldTypeVal
        newAns.ans=i
        newAns.save()
        A=Answers.objects.all()
    return render(request,"answers.html",{'A1':A})


def combo(request):
    return render(request,"combined.html")


# def addQuesAns(request):
#     fieldTypeVal = request.POST['element']
#     if request.method == 'POST':
#
#         QuestionList= request.POST.getlist('QuestionList')
#         AnswerList=request.POST.getlist('AnswerList')
#     else:
#         print "not working"
#
#     for i in QuestionList:
#         newQuesAns=QuesAns()
#         newQuesAns.ques1=i
#         for j in AnswerList:
#             newQuesAns.fieldType1=fieldTypeVal
#             newQuesAns.ans1=j
#         QA=QuesAns.objects.all()
#     return render(request, "preview.html", {'QA1': QA})