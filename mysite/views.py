from django.shortcuts import render_to_response
from django.http import HttpResponse
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
