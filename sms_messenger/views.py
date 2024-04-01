from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View, CreateView
from .send_sms import sms_instance
from django.contrib.auth import logout, authenticate, login
from sms_messenger.forms import LoginForm, MessagesForm
from .models import Messages, MessageHistory
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin


# Endpoint for sending sms message
def send_sms(request, pk):
    message = Messages.objects.get(id=pk)
    sms_instance.send(
        message=message.content, recipients=list(message.recipients.split(" "))
    )
    try:
        history = MessageHistory.objects.get(message=message)
        if history:
            history(timestamp=timezone.now)
            print("HISTORY ALREADY EXIST")
    except:
        new_history = MessageHistory(message=message)
        new_history.full_clean()
        new_history.save()
        print("NEW HISTORY SAVED")

    return redirect("history")


# Hompage View
class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "home.html")
        else:
            return redirect("login")


# View for sending sms to customers
class SendSmsView(View, LoginRequiredMixin):
    login_url = "app/login"
    redirect_field_name = "login"

    def get(self, request):
        form = MessagesForm()
        return render(request, "create_sms_form.html", {"form": form})

    def post(self, request):
        data = MessagesForm(request.POST)
        new_sms = Messages.objects.create(
            recipients=data["recipients"].data,
            content=data["content"].data,
            title=data["title"].data,
        )
        new_sms.full_clean()
        new_sms.save()
        sms_instance.send(
            message=new_sms.content, recipients=list(new_sms.recipients.split(" "))
        )
        return redirect("history")


# SMS history view
class MessageHistoryView(View, LoginRequiredMixin):
    login_url = "app/login"
    redirect_field_name = "login"

    def get(self, request):
        sms_messages = MessageHistory.objects.all()
        return render(request, "sms_history.html", {"sms_messages": sms_messages})


# create SMS template
class TemplatesView(CreateView, LoginRequiredMixin):
    login_url = "app/login"
    redirect_field_name = "login"

    def get(self, request):
        form = MessagesForm()
        return render(request, "create_template.html", {"form": form})

    def post(self, request):
        form = MessagesForm(request.POST)
        if form.is_valid():
            form.full_clean()
            form.save()
            return redirect("templates")
        return render(request, "create_template.html", {"form": form})


# Edit sms view
class EditSMSView(View, LoginRequiredMixin):
    login_url = "app/login"
    redirect_field_name = "login"

    def get(self, request, pk):
        sms = Messages.objects.get(id=pk)
        form = MessagesForm(instance=sms)
        return render(request, "create_sms_form.html", {"form": form})

    def post(self, request, pk):
        sms = Messages.objects.get(id=pk)
        form = MessagesForm(request.POST, instance=sms)
        if form.is_valid():
            form.full_clean()
            form.save()
            return redirect("history")
        return render(request, "create_sms_form.html", {"form": form})


# Edit template view
class EditTemplateView(View, LoginRequiredMixin):
    login_url = "app/login"
    redirect_field_name = "login"

    def get(self, request, pk):
        template = Messages.objects.get(id=pk)
        form = MessagesForm(instance=template)
        return render(request, "create_template.html", {"form": form})

    def post(self, request, pk):
        template = Messages.objects.get(id=pk)
        form = MessagesForm(request.POST, instance=template)
        if form.is_valid():
            form.full_clean()
            form.save()
            return redirect("templates")
        return render(request, "create_template.html", {"form": form})


# View for listing all templates
class TemplatesListView(View, LoginRequiredMixin):
    login_url = "app/login"
    redirect_field_name = "login"
    template_name = "templates_list.html"
    model = Messages

    def get(self, request):
        templates = self.model.objects.filter(is_template=True).all()
        return render(request, self.template_name, {"templates": templates})


# login user view
class Loginview(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html")


# logout user view
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
