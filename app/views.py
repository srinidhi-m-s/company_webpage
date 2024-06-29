from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from app.models import (
    GeneralInfo,
    ServiceInfo,
    Testimonials,
    Faq,
    ContactFormLogs,
    Blog)
def index(request):
    one_rec=GeneralInfo.objects.first()
    

    services=ServiceInfo.objects.all()

    testimonials=Testimonials.objects.all()

    faqs=Faq.objects.all()

    recent_blogs = Blog.objects.all().order_by("-created_at")[:3]

    for blog in recent_blogs:
        print(f"blog: {blog}")
    default_value =""
    context = {
        "email" : getattr(one_rec, "email", default_value),
        "desc":getattr(one_rec, "desc", default_value),
        "location" :getattr(one_rec, "location", default_value),
        "company_name":getattr(one_rec, "company_name", default_value),
        "phone" : getattr(one_rec, "phone", default_value),
        "open_hours":getattr(one_rec, "open_hours", default_value),
        "video_url" : getattr(one_rec, "video_url", default_value),
        "twitter_url" :getattr(one_rec, "twitter_url", default_value),
        "facebook_url" : getattr(one_rec, "facebook_url", default_value),
        "insta_url" : getattr(one_rec, "insta_url", default_value),
        "linkedin_url" : getattr(one_rec, "linkedin_url", default_value),
        "services":services,
        "testimonials":testimonials,
        "faqs":faqs,
        "recent_blogs":recent_blogs,
    }
    
   
    return render(request,"index.html",context)

def contact_form(request):
    if request.method =='POST':
        print("\nUser has submitted form")
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        context={
            "name":name,
            "email":email,
            "subject": subject,
            "message" : message,
        }
        html_content= render_to_string('email.html',context)
        is_success=False
        is_error = False
        error_message=""
        try:
            send_mail(
                subject= subject,
                message=None,
                html_message = html_content,
                from_email= settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
        except Exception as e:
            messages.error(request, f"Email not sent: {str(e)}")
            is_error=True
            error_message=str(e)
        else:
            messages.success(request, "email sent")
            is_success=True
        ContactFormLogs.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            action_time=timezone.now(),
            is_success=is_success,
            is_error=is_error,
            error_message=error_message,

        )   
    return redirect('home')

def blog_detail(request, blog_id):
    blog=Blog.objects.get(id=blog_id)
    recent_blogs = Blog.objects.all().exclude(id=blog_id).order_by("-created_at")[:2]
    
    context={
        "blog":blog,
        "recent_blogs":recent_blogs,
    }
    return render(request, "blog_details.html", context)

def blogs(request):
    all_blogs= Blog.objects.all().order_by("-created_at")
    blogs_per_page=3
    paginator = Paginator(all_blogs,blogs_per_page)
    print(f"paginator.num_pages:{paginator.num_pages}")
    page= request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs= paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    context={
        "blogs":blogs,
    }
    return render(request, "blogs.html", context)
