from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, IngresoUsuarioForm
from .models import HorasUsuario, CuotaUsuario
from django.core import serializers
from datetime import date, datetime

# Create your views here.
Max_Hour_Progress_Bar = 5 # x = 100% of the progress bar

@login_required(login_url='sign-in')
def index(request):
  cuotaObject = CuotaUsuario.objects.all().filter(email=request.user.email)
  data = serializers.serialize( "python", cuotaObject)
  fechaActual = datetime.today().strftime('%Y-%m-%d')
  if request.method=='POST':
    fecha = request.POST['fecha']
    form = CuotaUsuario(email=request.user.email, fechaExpiracion=datetime.strftime(datetime.strptime(fecha, '%d-%m-%Y'), '%Y-%m-%d'))
    if data:
      cuotaObject.update(fechaInicio=fechaActual, fechaExpiracion=datetime.strftime(datetime.strptime(fecha, '%d-%m-%Y'), '%Y-%m-%d'))
    else:
      form.save()
    return redirect('index')
  if data:
    delta = data[0]['fields']['fechaExpiracion']-data[0]['fields']['fechaInicio']
    diasCuota = datetime.now().day-datetime.strptime(datetime.strftime(data[0]['fields']['fechaInicio'], '%d'),'%d').day
    
    print(delta.days)
    porcentaje = 100 if delta.days == 0 else ((diasCuota/delta.days)*100)
    print(data[0]['fields'])
    if porcentaje>=100:
      porcentaje=100
      ctx={'hasALoggedDate':False, 'diasCuota':diasCuota,'totalDiasCuota':delta.days, 'porcentajeProgreso':int(porcentaje), 'fechaActual':fechaActual}
      return render(request,'index.html', ctx)
    ctx={'hasALoggedDate':True, 'diasCuota':diasCuota,'totalDiasCuota':delta.days, 'porcentajeProgreso':int(porcentaje), 'fechaActual':fechaActual}
    return render(request,'index.html', ctx)
  ctx={'hasALoggedDate':False, 'firstTime':True, 'totalProgreso':0, 'porcentajeProgreso':0, 'fechaActual':fechaActual}
  return render(request,'index.html', ctx)

#Login-Register pages
def data_len_validation(form):
  user,password = form.cleaned_data.get('usuario'),form.cleaned_data.get('password')
  print(user,password)
  if len(user) >3 and len(user) < 17 and len(password) >3 and len(password) < 15:
    return True
  else:
    return False

def sign_up(request):
  if not request.user.is_authenticated:
    if request.method == 'GET':
      form = RegistroUsuarioForm()
      ctx={
        'form':form
      }
      return render(request, 'sign-up.html',ctx)
    else:
      form = RegistroUsuarioForm(request.POST)
      if form.is_valid() and data_len_validation(form):
        usuario = authenticate(request,user=form.cleaned_data,site='sign_up')
        if usuario:
          login(request,usuario)
          return redirect('index')
        else:
          print("vino por aca")
          return redirect('sign-up', )
      #return render(request, 'sign-up.html')
  return redirect('index')

def sign_in(request):
  if not request.user.is_authenticated:
    if request.method == 'GET':
      form = IngresoUsuarioForm()
      ctx={
        'form':form
      }
      return render(request,'sign-in.html',ctx)
    else:
      form = IngresoUsuarioForm(request.POST)
      if form.is_valid():
        usuario = authenticate(request,user=form.cleaned_data,site='sign_in')
        if usuario:
          login(request,usuario)
          return redirect('index')
        else:
          return redirect('index')
      return redirect('sign-in')
  return redirect('index')

def log_out(request):
  logout(request)
  return redirect('sign-in')

#performance page
@login_required(login_url='sign-in')
def performan(request):
  days_without_time = []
  average = []
  horasObject = HorasUsuario.objects.all().filter(email=request.user.email)
  data = serializers.serialize( "python", horasObject)
  data = data[0]['fields']
  data.pop('email')
  progress_bar = {}
  for x in data:
    if data[x]==-1:
      days_without_time.append(x)
      progress_bar[x] = 0
    elif data[x]>=0:
      progress_bar[x] = int((data[x]*100)/Max_Hour_Progress_Bar)
    else:
      print("achasdjfasd")
  if not days_without_time:
    average = [x for x in data.values()]
    average = int(sum(average)/6)
    horasObject.update(lunes=-1,martes=-1,miercoles=-1,jueves=-1,viernes=-1,sabado=-1,promedio=average)
    return redirect('performance')
  ctx = {'day':days_without_time[0],'max_hour_progress_bar':Max_Hour_Progress_Bar,'progress':progress_bar,'average':data['promedio']}
  if request.method=='POST':
    hours = int(request.POST['tiempo'])
    if hours <= Max_Hour_Progress_Bar and hours >0:
      day = days_without_time[0]
      data[day] = hours
      print(hours,data)
      horasObject.update(**data)
      return redirect('performance')
    else:
      return redirect('performance')
  else:
    return render(request,'rendimiento.html',ctx)