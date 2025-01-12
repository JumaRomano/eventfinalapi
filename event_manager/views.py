from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm
from django.http import JsonResponse
from django.contrib import messages
from .serializers import EventSerializer
from rest_framework import viewsets


# List view for events
def event_list(request):
    events = Event.objects.all().order_by('-created_at')
    return render(request, 'event_manager/event_list.html', {'events': events})

# Detail view for a single event
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_manager/event_detail.html', {'event': event})

# Create view for a new event
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'event_manager/create_event.html', {'form': form})

# Update view for an existing event
def update_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'event_manager/update_event.html', {'form': form})

# Delete view for an existing event
def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('event_list')
    return render(request, 'event_manager/delete_event.html', {'event': event})

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer