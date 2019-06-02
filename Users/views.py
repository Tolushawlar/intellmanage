from django.shortcuts import render, get_object_or_404
from .models import Project, Expense, Category
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from .forms import ExpenseForm
from django.views.generic import CreateView
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import json
# Create your views here.


def project_list(request):
    project_list = Project.objects.all()
    context = {
        'project_list': project_list
    }
    return render(request, "Users/project-list.html", context)

    """
	project_list = Projects.objects.all()
	context = {
		'project_list': project_list,
	}
    return render(request, "Users/project-list.html", context)
    """



def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    expense_list = project.expenses.all() 
    
    
    if request.method =='GET':
        category_list = Category.objects.filter(project=project)
        context = {
            'project': project,
            'expense_list' : expense_list,
            'category_list': category_list,
        }
        return render(request, "Users/project-detail.html", context)
    
    elif request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            category_name = form.cleaned_data['category']

            category = get_object_or_404(Category, project=project, name=category_name)

            Expense.objects.create(
                project=project,
                title=title,
                amount=amount,
                category=category
            ).save()
    
    elif request.method == "DELETE":
        id = json.loads(request.body)['id']
        expense = get_object_or_404(Expense, id=id)
        expense.delete()

        return HttpReponse('')
        
    return HttpResponseRedirect("/")



class ProjectCreateView(CreateView):
    model = Project
    template_name = "Users/add-project.html"
    fields = ('name', 'budget')

    def form_valid(self, form): 
        self.object = form.save(commit=False)
        self.object.save()

        category = self.request.POST['category-input']
        cat_list = []
        cat_list.append(category)
        for cat in cat_list:
            Category.objects.create(
                project = Project.objects.get(id=self.object.id),
                name = category
             ).save()

        return HttpResponseRedirect(self.get_success_url())
    

    def get_success_url(self):
        return slugify(self.request.POST['name'])


def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect("Login")
    else:
        form = UserRegister()

    context = {
        'form':form,
    }

    return render(request, "Users/register.html", context)

