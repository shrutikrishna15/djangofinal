
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from home.forms import HomeForm,CommentForm
from home.models import Post,Friend,Comment
from django.http import HttpResponse



class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self,request):
        form = HomeForm()
        posts = Post.objects.all()
        #users = User.objects.exclude(id=request.user.id)
        args = {'form':form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('/home')

        args = {'form': form, 'text':text }
        return render (request, self.template_name,args)



class CommentView(TemplateView):
    template_name = 'home/comment.html'

    def get(self,request):
        form = CommentForm()
        comments = Comment.objects.all()

        #users = User.objects.exclude(id=request.user.id)
        args = {'form':form,'comments':comments}
        return render(request, self.template_name, args)

    def post(self, request):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = request.user
            #post.comment = request.comment
            post.save()


            text = form.cleaned_data['post']
            form = CommentForm()
            return redirect('/home')

        args = {'form': form, 'text':text }
        return render (request, self.template_name,args)
