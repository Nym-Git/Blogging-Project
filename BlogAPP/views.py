from django.shortcuts import render, redirect, get_object_or_404
from .models import Instruction, Comment, User_Information, Category, GoogleAdd
from .forms import InstructionFORMS, commentFORMS, SignupFORMS, profileFORMS, categoryFORMS
from django.views.generic.edit import UpdateView, DeleteView
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator


# Post Creation View
def indexVIEW(request):
  if request.method == 'POST':
    form = InstructionFORMS(request.POST, request.FILES)
    if form.is_valid():
      new_req = Instruction(User_Name = request.user,Title_M=request.POST['TitleF'],Category_M=request.POST['CategoryF'],Details_M=request.POST['DetailsF'], ImagesM=request.FILES['Images'],)
      new_req.save()
      return HttpResponseRedirect('display')

  else:
    form = InstructionFORMS()
  
  htmlcode = True
  context = {'form': form, 'git':htmlcode}
  return render(request,'index.html', context)



# Category field name fetching in database by this VIEW
def categoryVIEW(request):
  if request.method == 'POST':
    form = categoryFORMS(request.POST)
    if form.is_valid():
      new_req = Category(Category_Field=request.POST['category'])
      new_req.save()
      return HttpResponseRedirect(reverse('display'))

  else:
    form = categoryFORMS()

  context = {'form': form}
  return render(request,'choise.html', context)



# Display the Posts-Data View
def display(request):
  adds = GoogleAdd.objects.all()
  Category_manu = Category.objects.all()                # borrow the Category manu form categorys model for Sow on the navbar
  All_POSTs = Instruction.objects.all().order_by('-id')
  
  paginator = Paginator(All_POSTs, 12)
  page = request.GET.get('page')
  All_POSTs = paginator.get_page(page)
  return render(request,'display.html', {'PostS':All_POSTs, 'manu':Category_manu, 'ADDS': adds})



# Display the Posts-Trending-Data View
def trendingVIEW(request):
  Category_manu = Category.objects.all()                # borrow the Category manu form categorys model for Sow on the navbar
  All_POSTs = Instruction.objects.all().order_by('-Liked_int_M')
  return render(request,'trending.html', {'PostS':All_POSTs, 'manu':Category_manu})



# Content by Filtering
def Filter_DisplayVIEW(request, choice):
  Category_manu = Category.objects.all()                             # borrow the Category manu form categorys model for Sow on the navbar
  Filtered_All_POSTs = Instruction.objects.filter(Category_M=choice).order_by('-id')
  return render(request,'FilterDisplay.html', {'choice': choice, 'PostS': Filtered_All_POSTs, 'manu':Category_manu})



# account Info form and display too #may be confusing
def UserInfo(request):
  if request.method == 'POST':
    form = profileFORMS(request.POST, request.FILES)
    if form.is_valid():
      new_req = User_Information(User_Name = request.user, First_name = request.user.first_name, Last_name= request.user.last_name, PAN_ID_Number=request.POST['panF'], Adhar_Card_Number=request.POST['adharF'], Mobile_Number=request.POST['mobileF'],Instagram=request.POST['instaF'],Facebook=request.POST['fbF'],LindedIN=request.POST['inF'],AboutU=request.POST['aboutUF'],Photo=request.FILES['photoF'])
      new_req.save()
      return HttpResponseRedirect(reverse('userProfile'))

  else:
    form = profileFORMS()

  user_id_local_var = request.user                       #filtering user who is the present user by one to one field
  Unique_user_info = User_Information.objects.filter(User_Name = user_id_local_var)
                                                         #filtering user's posts
  All_POSTs = Instruction.objects.filter(User_Name = user_id_local_var)

  return render(request,'user.html', {'form':form,'User_InfoS': Unique_user_info, 'Post': All_POSTs})




# Display Post-exactly-DATA with comments Display logic
def detailsView(request, id):
  POSTs_key = Instruction.objects.filter(id=id)        # For display the unique Data

  if request.method == 'POST':                         # comment form, fetching comment data
    form = commentFORMS(request.POST)
    if form.is_valid():
      post_id_local_var = Instruction.objects.get(id=id)
      newReq = Comment(Comment=request.POST['CommentF'], User_Name = request.user, post_ID = post_id_local_var)
      newReq.save()
      return HttpResponseRedirect(reverse('details', args=[str(id)]))     # For refrace the page

  else:
    form = commentFORMS()

  if request.user.is_authenticated:
    user_id_local_var = request.user                       #filtering user who is the present user by one to one field
    Unique_user_info = User_Information.objects.filter(User_Name = user_id_local_var)
  else:
    Unique_user_info = False

  user_image = User_Information.objects.all()


  All_Comments = Comment.objects.order_by('id').filter(post_ID=id)       # Filtering the comment for Display on exact post
  return render(request,'detials.html', {'User': Unique_user_info, 'ID_Post':POSTs_key , 'CommentS':All_Comments, 'forms': form, 'UserInfoS':user_image})



# using NOW post author
def AdminView(request, id):
  POSTs_key = Instruction.objects.filter(id=id)
  Admin_POSTs = Instruction.objects.all().order_by('-id')
  user_image = User_Information.objects.all()
  return render(request,'userinfoform.html', {'ID_Post':POSTs_key, 'PostS':Admin_POSTs, 'UserInfo':user_image})



# SignUP by class based view
class UserRegisterView(generic.CreateView):
  form_class = SignupFORMS
  template_name  = 'registration/register.html'
  success_url = reverse_lazy('login')



# account Info form and display too #may be confusing
def baseVIEW(request):
  user_id_local_var = request.user                       #filtering user who is the present user by one to one field
  Unique_user_info = User_Information.objects.filter(User_Name = user_id_local_var)

  return render(request,'Base.html', {'User_Info': Unique_user_info})



# Display Post-like
def likeView(request, id):
  user = request.user
  if request.method == 'POST':
    post_id = request.POST.get('post_id')
    post_obj = Instruction.objects.get(id=post_id)

    if user in post_obj.Likes_M.all():
      post_obj.Likes_M.remove(user)
      post_obj.Liked_int_M = post_obj.Liked_int_M - 1
      post_obj.save()

    else:
      post_obj.Likes_M.add(user)
      local_VAR_like_status=True
      post_obj.Liked_int_M = post_obj.Liked_int_M + 1
      post_obj.save()

  return HttpResponseRedirect(reverse('details', args=[str(id)]))



# google add
def addsView(request, id):
  user = request.user
  add_id = request.POST.get('add_id')
  add_obj = Instruction.objects.get(id=add_id)
  add_obj.clicking.add(user)
  add_obj.save()
  return render(request,'display.html')


# update the post [working]
class updateVIEW(UpdateView):
  model = Instruction
  template_name = 'update.html'
  fields = ['Title_M','Details_M','Category_M','ImagesM']
  success_url = reverse_lazy('display')



# delete the post
class DeleteVIEW(DeleteView):
    model = Instruction
    template_name = 'delete.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('display')



'''def updateVIEW(request, id):                     #it works when you have views.model function type
  getPostObj = Instruction.objects.get(id = id)
  form = InstructionFORMS(instance=Instruction)

  if request.method == 'POST':
    form = InstructionFORMS(request.POST, request.FILES, instance=Instruction)
    if form.is_valid():
      new_req = Instruction(User_Name = request.user,Title_M=request.POST['TitleF'],Category_M=request.POST['CategoryF'],Details_M=request.POST['DetailsF'], ImagesM=request.FILES['Images'],)
      new_req.save()
      return HttpResponseRedirect('display')

  context = {'form': form}
  return render(request,'index.html', context)
'''
