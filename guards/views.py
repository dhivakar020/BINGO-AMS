from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance
from .forms import AttendanceForm


@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST, request.FILES)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.guard = request.user
            attendance.save()
            return redirect('attendance_success')
    else:
        form = AttendanceForm()
    return render(request, 'guards/mark_attendance.html', {'form': form})


def attendance_success(request):
    return render(request, 'guards/attendance_success.html')


@login_required
def view_attendance_report(request):
    attendances = Attendance.objects.all().order_by('-timestamp')
    return render(request, 'guards/attendance_report.html', {'attendances': attendances})
