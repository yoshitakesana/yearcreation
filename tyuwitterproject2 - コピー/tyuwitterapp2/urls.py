from django.urls import path
from . import views

app_name='tyuwitterapp2' #URLconfを逆引き参照できるようにアプリ名を登録

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'), #トップ
    path('index/',views.IndexView.as_view(),name='index'), #トップ#ホームのアイコンを押された時　※一回分しかまだできていない
    path('profile/',views.ProfileView.as_view(),name='profile'), #プロフィール
    path('search/',views.SearchView.as_view(),name='search'), #検索
    path('setting/',views.SettingView.as_view(),name='setting'), #設定
    path('dm/', views.DMView.as_view(), name='dm'),  # ダイレクトメッセージページ
    path('notice/', views.NoticeView.as_view(), name='notice'),  # 通知ページ
    path('post/', views.CreateView.as_view(), name='post'),  # 投稿するページ
    #path('signup/',views.SignupView.as_view(),name='signup'), #サインアップ
    #path('follow/',views.FollowView.as_view(),name='follow'), #フォロー
    #path('follower/',views.FollowerView.as_view(),name='follower'), #フォロワー
    #path('detail/<int:pk>/',views.DetailView.as_view(),name='detail'), #詳細
    #path('login/',views.LoginView.as_view(),name='login'), #ログイン
    path('post_done/',views.PostDoneView.as_view(),name='post_done'), #投稿完了ページ
    path(
        'Post-detail/<int:pk>/',
        views.PostDetailView.as_view(),#投稿詳細がこっち
        name='detail'
    ),
    path('contact/', views.ContactView.as_view(), name='contact'),  # お問い合
    path('search_results/', views.SearchResultsView.as_view(), name='search_results'),
]