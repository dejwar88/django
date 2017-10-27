from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404

from guestbookapp.models import Entry
from guestbookapp.forms import EntryForm

def index (request):

    if request.method == 'POST':
        form = EntryForm (request.POST)

        if form.is_valid ():
            form.save (commit = True)
        else:
            print (form.errors ())

    context = {}

    entry_list = Entry.objects.all ()
    context ['entries'] = entry_list

    form = EntryForm ()
    context ['form'] = form

    return render (request, 'guestbookapp/index.html', context)

def delete_entry (request, entry_id):

    Entry.objects.filter (id = entry_id).delete ()

    return redirect (reverse ('index'))

def update_entry (request, entry_id):

    entry = get_object_or_404 (Entry, pk = entry_id)

    context = {}

    context ['entries'] = Entry.objects.all ()

    if request.method ==  'POST':
        form = EntryForm (request.POST, instance = entry)

        if form.is_valid ():
            form.save (commit = True)
            print (form)
        else:
            print (form.errors())

        return redirect (reverse ('index'))

    if request.method == 'GET':
        context ['form'] = EntryForm (instance = entry)

        return render (request, 'guestbookapp/index.html', context)
