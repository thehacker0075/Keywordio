import email
from fnmatch import fnmatchcase
from django.shortcuts import render,redirect

from myapp.models import Admin, Book

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        Admin.objects.create(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            address=request.POST['address'], 
            password=request.POST['password'],
        )
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        try:
            admin=Admin.objects.get(
                email=request.POST['email'],
                password=request.POST['password']
            )
            request.session['email']=admin.email
            request.session['fname']=admin.fname
            return render(request,'admin_index.html')
        except:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        return render(request,'login.html')
    except:
        return render(request,'login.html')

def add_book(request):
    if request.method=='POST':
        admin_book=Admin.objects.get(email=request.session['email'])
        Book.objects.create(
            admin_book=admin_book,
            book_collection=request.POST['book_collection'],
            book_name=request.POST['book_name'],
            book_price=request.POST['book_price'],
            book_des=request.POST['book_des'],
            book_image=request.FILES['book_image'],
            )
        return render(request,'add_book.html')
    else:
        return render(request,'add_book.html')

def view_book(request):
    try:
        admin_book=Admin.objects.get(email=request.session['email'])
        books=Book.objects.filter(admin_book=admin_book).order_by('-id')[:]
        return render(request,'view_book.html',{'books':books})
    except:
        return render(request,'view_book.html')

def admin_edit_book(request,pk):
    book=Book.objects.get(pk=pk)
    if request.method=='POST':
        book.book_collection=request.POST['book_collection']
        book.book_book_name=request.POST['book_name']
        book.book_price=request.POST['book_price']
        book.book_des=request.POST['book_des']
        try:
            book.book_image=request.FILES['book_image']
        except:
            pass
        book.save()
        return render(request,'edit_book.html',{'book':book})
    else:
        return render(request,'edit_book.html',{'book':book})

def admin_delete_book(request,pk):
    book=Book.objects.get(pk=pk)
    book.delete()
    return redirect('view_book')