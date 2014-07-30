from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book
from books.forms import ContactForm
from django.core.mail import send_mail
# Create your views here.
# def search_form(request):
# 	return render_to_response('search_form.html')
def search(request):
	error=[]
	if 'q' in request.GET:
		q=request.GET['q']
		if not q:
			error.append('Enter a search term.')
		elif len(q)>20:
			error.append('Please enter at most 20 characters.')
		else:
			books=Book.objects.filter(title__icontains=q)
			return render_to_response('search_results.html',{'books':books,'query':q})
	return render_to_response('search_form.html',{'error':error})
def contact(request):
	error=[]
	if request.method=='POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email','xx@example.com'),
				['site@example.com'],
				)
			return HttpResponseRedirect('/contact/thanks')
	else:
		form=ContactForm()
	return render_to_response('contact_form.html',{'form':form})
	# if request.method=='POST':
	# 	if not request.POST.get('subject',''):
	# 		error.append('Enter a subject.')
	# 	if not request.POST.get('message',''):
	# 		error.append('Enter a message')
	# 	if request.POST.get('email') and '@' not in request.POST['email']:
	# 		error.append('Enter a valid e-mail address.')
	# 	if not error:
	# 		send_mail(
	# 			request.POST['subject'],
	# 			request.POST['message'],
	# 			request.POST.get('email','xx@example.com'),
	# 			['siteowner@example.com'],
	# 			)
	# 		return HttpResponseRedirect('/contact/thanks/')
	# return render_to_response('contact_form.html',{'error':error})
