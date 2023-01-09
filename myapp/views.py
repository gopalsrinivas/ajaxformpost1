from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
import os,json
from .models import *
from .forms import *

# Create your views here.
def get_ip_address(request):
    """ use requestobject to fetch client machine's IP Address """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')    ### Real IP address of client Machine
        print(ip)
    return ip 

def getStateDetails(request):
    country_id = request.GET.get("country")
    states = State.objects.filter(country_id=country_id)
    context = {
        'states':states
    }
    return render(request, 'myapp/load_states.html', context)

def getDistDetails(request):
    country_id = request.GET.get('country')
    state_id = request.GET.get('state')
    # data = str(country_id)+ '--' + str(state_id)
    # print(data)
    dists = District.objects.filter(country_id=country_id, state_id=state_id)
    context = {
        'dists':dists
    }
    return render(request, 'myapp/load_dist.html',context)


def empform(request):
    if request.method == 'POST':
        form = EmployeeDetailsModelForm(request.POST, request.FILES)
        emp_img = request.FILES.getlist('emp_img')
        emp_app = request.FILES.getlist('emp_app')
        prejoblocation = ",".join(request.POST.getlist('prejoblocation'))
        
        #postdata = str(studentimg) + str(emp_app) + str(stdntlang)
        #print(postdata)

        # Mobile Number validation
        mobileno = request.POST.get('mobile')
        if employeeDetails.objects.filter(mobile = mobileno):
            # some form errors occured.
            message = 'This Mobile Number already exist.'
            msg_status = 'failed'
            data = {
                "error": True,
                "message_status": msg_status,
                'message':message,
                "status":400
            }
            return JsonResponse(data,safe=False)

        # Email validation
        email = request.POST.get('email')
        if employeeDetails.objects.filter(email = email):
            # some form errors occured.
            message = 'This Email already exist.'
            msg_status = 'failed'
            data = {
                "error": True,
                "message_status": msg_status,
                'message':message,
                "status":400
            }
            return JsonResponse(data,safe=False)

        if form.is_valid():
            # File Validation
            for file in emp_app:
                ext = os.path.splitext(file.name)[1]
                valid_extensions = ['.pdf', '.csv', '.doc', '.docx', '.xlsx', '.xlx']
                if ext.lower() in valid_extensions:
                    # Form data insert into database
                    formpostdata = form.save(commit=False)
                    formpostdata.ip_address = get_ip_address(request)
                    formpostdata.prejoblocation = prejoblocation
                    formpostdata.save()

                    # Form Posting Response.
                    ser_instance = serializers.serialize('json', [formpostdata,])
                    message = 'Your Form Successfully Submitted !'
                    message_status = 'success'
                    data = {
                            'instance' : ser_instance,
                            'message' : message,
                            "message_status" : message_status,
                            'status' : 200,
                            }
                    return JsonResponse(data,safe=False)
                else:
                    # some form errors occured.
                    message = 'Unsupported file extension!'
                    message_status = 'failed'
                    data = {
                            'error':form.errors,
                            'message':message,
                            "message_status": message_status,
                            'status':400
                        }
                    return JsonResponse(data,safe=False)
        else:
            # some form errors occured.
            message='Your Form is not submitted !'
            message_status = 'failed'
            data = {
                    'error':form.errors,
                    'message':message,
                    'message_status': message_status,
                    'status':400
                    }
            return JsonResponse(data,safe=False)
    else:
        form = EmployeeDetailsModelForm()
        countrylist = Country.objects.all()
        statelist = State.objects.all()
        districtlist = District.objects.all()
        prejoblist = prejobloc.objects.all()
        empdtls = employeeDetails.objects.all().order_by('-id')

        context = {
            'form':form,
            'countrylist':countrylist,
            'statelist':statelist,
            'districtlist':districtlist,
            'prejoblist':prejoblist,
            'empdtls':empdtls,
        }
    return render(request, 'myapp/index.html', context)

def getEmpViewDetails(request,pk):
    empdetails = employeeDetails.objects.get(pk=pk)
    context = {
        'empdetails':empdetails
    }
    return render(request, 'myapp/empviewdetails.html', context)

def getSeachDetails(request):
    if request.GET.get('search'): # write your form name here      
        query = request.GET.get('search', None)    
        try:
            getSearchData = employeeDetails.objects.filter(
             Q(name__icontains=query) | Q(email__icontains=query) | Q(mobile__icontains=query)
             )
            context = {
               'getSearchData':getSearchData
             } 
            return render(request,"myapp/searchdata.html",context)
        except:
            getSearchData = "Data Not Found"
            context = {
               'getSearchData':getSearchData
             } 
            return render(request,"myapp/searchdata.html",context)
    else:
        getSearchData = employeeDetails.objects.all()
        context = {
               'getSearchData':getSearchData
             }
        return render(request,"myapp/searchdata.html",context)



