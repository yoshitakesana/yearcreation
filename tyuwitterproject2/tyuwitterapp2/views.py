from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from .models import Post
from django.views.generic import FormView
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class IndexView(ListView):
    template_name='index.html'
    context_object_name='orderby_records' #テンプレートに渡す変数名を指定
    queryset =Post.objects.order_by('-posted_at') #表示するデータを取得するメソッドを指定
@method_decorator(login_required,'dispatch')

class HomeView(TemplateView):
    template_name='index.html'

@method_decorator(login_required,'dispatch')#ここでツイートのビュー
class CreateView(CreateView):
    form_class=PostForm
    template_name='tui-to.html' #使用するhtmlファイルの名前を記述
    success_url=reverse_lazy('tyuwitterapp2:post_done') #送信完了後にリダイレクトするURLを指定
    def form_valid(self,form):
        postdata=form.save(commit=False)
        postdata.user=self.request.user
        postdata.save()
        return super().form_valid(form)

class PostDoneView(TemplateView):
    template_name='tui-to_success.html' #使用するhtmlファイルの名前を記述

class ProfileView(TemplateView):
    template_name='profile.html' #使用するhtmlファイルの名前を記述
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['date_joined'] = user.date_joined
        return context

class SearchView(TemplateView):
    template_name='search.html' #使用するhtmlファイルの名前を記述


class SettingView(TemplateView):
    template_name='setting.html' #使用するhtmlファイルの名前を記述

class DMView(TemplateView):
    template_name = 'dm.html'  # 使用するhtmlファイルの名前を記述


class NoticeView(TemplateView):
    template_name = 'notice.html'  # 使用するhtmlファイルの名前を記述

class PostDetailView(DetailView):
    template_name = 'post.html'#一件のデータを表示するためのテンプレートファイルを指定
    model = Post

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('tyuwitterapp2:contact')

    def form_valid(self, form):
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']
        subject = 'お問い合わせ : {}'.format(title)
        message = \
        '送信者名 : {0}\nメールアドレス : {1}\n タイトル : {2}\n メッセージ : {3}'.format(name,email,title,message)
        from_email = 'fko2447057@stu.o-hara.ac.jp'
        to_list = ['fko2447057@stu.o-hara.ac.jp']
        message=EmailMessage(subject=subject,
                            body=message,
                            from_email=from_email,
                            to=to_list,
                            )
        message.send()
        messages.success(
            self.request,'お問い合わせメールは正常に送信されました！')
        return super().form_valid(form)


# class SignupView(TemplateView):
#     template_name = 'signup.html'

# class FollowView(TemplateView):
#     template_name = 'follow.html'

# class FollowerView(TemplateView):
#     template_name = 'follower.html'

# class DetailView(TemplateView):
#     template_name = 'detail.html'

# class LoginView(TemplateView):
#     template_name = 'login.html'

# class CreateDoneView(TemplateView):
#     template_name = 'create_done.html'