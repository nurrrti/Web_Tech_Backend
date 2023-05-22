from django.db.models import Q, CharField, TextField
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *


class IndexView(ListView):
    template_name = "books/base.html"
    context_object_name = "latest_books"
    queryset = Book.objects.order_by('-book_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_books'] = Book.objects.filter(
            book_num_of_views__gt=100).order_by('-book_num_of_views')[:4]
        context['categories'] = Book.objects.values(
            "book_category").distinct()
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book.html"
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        book = Book.objects.get(pk=kwargs['object'].id)
        book.increase_view_num()
        book.save()
        context = super().get_context_data(**kwargs)
        context["latest_books"] = Book.objects.order_by('-book_date')
        context['popular_books'] = Book.objects.filter(
            book_num_of_views__gt=100).order_by('-book_num_of_views')[:4]
        bk_category = kwargs['object'].book_category
        context['related_books'] = Book.objects.filter(
            book_category=bk_category).order_by('-book_num_of_views')[:8]
        context['form'] = CommentForm()
        context['comments_on_book'] = Comment.objects.filter(
            comment_on_book=kwargs['object'].id)
        context['categories'] = Book.objects.values(
            "book_category").distinct()
        return context

    def post(self, request):
        if request.method == 'POST':
            book_rate = request.POST.get('book_rate')
            book = Book.objects.get(id=request.POST.get('book_id'))
            book.book_rate(float(book_rate))
            book.save()
            return redirect("bookapp:get_book_by_id",
                            pk=request.POST.get('book_id'))


class SearchView(View):
    paginated_by = 5

    def post(self, request):
        try:
            if request.method == "POST" and len(request.POST.get("search_field")) > 0:
                searching_text = request.POST.get("search_field")
                return redirect("bookapp:search_success", text=searching_text)
            else:
                return render(request, "books/search.html",
                              {"empty_res": "There is no book"})
        except Exception as e:
            print(e)
            return render(request, "books/search.html",
                          {"empty_res": f"No book have been found by {request.POST.get('search_field')}"})


class SearchSuccessView(View):

    def get(self, request, text):
        fields = [field for field in Book._meta.fields if isinstance(
            field, CharField) or isinstance(field, TextField)]

        queries = [Q(**{field.name + "__icontains": text}) for field in fields]
        qs = Q()
        for query in queries:
            qs = qs | query

        search_res = Book.objects.filter(qs)
        return render(request, "books/search.html",
                      {"search_res": search_res, "empty_res": "There is no book"})


class ArchiveView(ListView):
    template_name = 'books/archive.html'
    context_object_name = "archive_books"
    queryset = Book.objects.all()[:100]  # 2235
    paginate_by = 10


class ContactsView(TemplateView):
    template_name = "books/contacts.html"


class ProfileView(TemplateView):
    template_name = "books/user_page.html"


class ProfileChangeView(FormView):
    template_name = "books/user_change_page.html"
    form_class = CustomUserChangeForm


class registerView(CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy('login')
    template_name = 'books/registration.html'


class LeaveCommentView(View):

    def post(self, request):
        if request.method == 'POST':
            comment_on_book = request.POST.get('comment_on_book')
            new_comment = Comment(comment_text=request.POST.get('comment_text'),
                                  comment_owner=CustomUser.objects.get(
                                      id=request.user.id),
                                  comment_on_book=Book.objects.get(id=comment_on_book))
            new_comment.save()
            return redirect("bookapp:get_book_by_id",
                            pk=request.POST.get('comment_on_book'))


class CommentLikeView(View):
    def post(self, request):
        if request.method == 'POST':
            comment_rate = request.POST.get('comment_rate')
            comment_obj = Comment.objects.get(
                id=request.POST.get('comment_id'))
            comment_obj.rate_comment(float(comment_rate))
            comment_obj.save()
            return redirect("bookapp:get_book_by_id",
                            pk=request.POST.get('book_id'))
