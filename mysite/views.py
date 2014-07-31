from django.shortcuts import render_to_response,render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from books.forms import *
import datetime

def current_datetime(request):
    current_date = datetime.datetime.now()
    # return render_to_response('current_datetime.html',{'current_date':now})
    return render_to_response('current_datetime.html',locals())
def display_meta(request):
	values=request.META.items()
	values.sort()
	# html=[]
	# for k,v in values:
	# 	html.append('<tr><td>%s</td><td>%s</td></tr>' % (k,v))
	# return HttpResponse('<table>%s</table>'% '/n'.join(html))
	return render_to_response('display_meta.html',{'values':values})
def contact(request):
	if request.method=='POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			send_mail(cd['subject'],
				cd['message'],
				cd.get('email','xxx@example.com'),
				['siteowner@example.com'],)
			return HttpResponseRedirect('/contact/thanks')
	else:
		form=ContactForm(initial={'subject':'I love your site!'})
	return render(request,'contact_form.html',{'form':form})
def testform(request):
	if request.method=='POST':
		test=TestForm(request.POST)
		if test.is_valid():
			cd=test.cleaned_data
			if request.POST.has_key('save'):
				request.session['first']=cd
			if request.POST.has_key('next'):
				request.session['first']=cd
				return HttpResponseRedirect('test-next')
	else:
		if request.session.has_key('first'):
			test=TestForm(request.session['first'])
		else:
			test=TestForm(initial={'name':'I love your site!'})
	return render(request,'test_form.html',{'form':test})

def testnext_form(request):
	if request.method=='POST':
		next=TestnextForm(request.POST)
		if next.is_valid():
			cd=next.cleaned_data
			if request.POST.has_key('save'):
				request.session['second']=cd
			if request.POST.has_key('forward'):
				request.session['second']=cd
				return 	HttpResponseRedirect(reverse('mysite.views.testform'))		
	else:
		if request.session.has_key('second'):
			next=TestnextForm(request.session['second'])
		else:
			next=TestnextForm(initial={'email':'test@example.com'})
	return render(request,'test_next.html',{'form':next})
