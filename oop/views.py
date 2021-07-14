from django.shortcuts import render

def geeks_view(request):
    # create a dictionary to pass
    # data to the template
    context ={
        "data":"Gfg is the best",
        "list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    # return response with template and context
    return render(request, "geeks.html", context)


def geeks_view1(request):
    # create a dictionary
    context = {
        "first_name" : "Naveen",
        "last_name"  : "Arora",
    }
    # return response
    return render(request, "geeks.html1", context)

def geeks_view2(request):
    # create a dictionary
    context = {
        "data" : 99,
    }
    # return response
    return render(request, "geeks.html2", context)


def geeks_view3(request):
  
    # return response
    return render(request, "extendedgeeks.html")
