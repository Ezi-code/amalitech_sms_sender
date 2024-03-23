from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View, CreateView
from .send_sms import sms_instance
from django.contrib.auth import logout, authenticate, login
from sms_messenger.forms import LoginForm, MessagesForm, TemplatesForm
from .models import Messages, Templates


# Create your views here.
def send_sms(request, content, recipients):
    recipients = list(recipients.split(" "))
    sms_instance.send(message=content, recipients=recipients)
    return redirect("home")


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            # SMS.send()
            return render(request, "home.html")
        else:
            return redirect("login")


class SendBulkSms(View):
    def get(self, request):
        form = MessagesForm()
        return render(request, "create_sms_form.html", {"form": form})

    def post(self, request):
        content = request.POST["content"]
        recipients = request.POST["recipients"]
        title = request.POST["title"]
        new_sms = Messages.objects.create(
            recipients=recipients, content=content, title=title
        )
        new_sms.full_clean()
        send_sms(request, content=content, recipients=recipients)
        new_sms.save()
        return redirect("history")


class MessageHistoryView(View):
    def get(self, request):
        sms_messages = Messages.objects.all()
        return render(request, "sms_history.html", {"sms_messages": sms_messages})

    def post(self, request):
        # message = request.POST
        # recipients = request.POST["recipients"]
        # SMS.send(message, recipients)
        print(request.POST)
        return HttpResponse("Message Sent")


class TemplatesView(CreateView):
    def get(self, request):
        form = TemplatesForm()
        return render(request, "create_template.html", {"form": form})

    def post(self, request):
        form = TemplatesForm(request.POST)
        if form.is_valid():
            form.full_clean()
            form.save()
            return redirect("templates")


class EditSMSView(View):
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


class EditTemplateView(View):
    def get(self, request, pk):
        template = Templates.objects.get(id=pk)
        form = TemplatesForm(instance=template)
        return render(request, "create_template.html", {"form": form})

    def post(self, request, pk):
        template = Templates.objects.get(id=pk)
        form = TemplatesForm(request.POST, instance=template)
        if form.is_valid():
            form.full_clean()
            form.save()
            return redirect("templates")


class TemplatesListView(View):
    template_name = "templates_list.html"
    model = Templates

    def get(self, request):
        templates = self.model.objects.all().order_by("-created_at")
        return render(request, self.template_name, {"templates": templates})


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


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
