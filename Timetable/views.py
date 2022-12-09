from django.http import JsonResponse

from Timetable.models import TimeTable
from Timetable.serializer import ReadSimpleScedule

# Create your views here.

def schedule(request):
    if request.method == 'GET':

        try: gradecode = request.GET['gradecode']
        except: gradecode = 1
        try: classcode = request.GET['classcode']
        except: classcode = 1
        try: user_id = request.GET['user_id'] 
        except: user_id = None
        try:
            timetable = TimeTable.objects.get(grade_number=gradecode, class_number=classcode)
        except:
            return JsonResponse({
                "code" : "01201",
                "message" : "시간표가 존재하지 않습니다.",
                "status" : 400
            })
        serializer = ReadSimpleScedule(timetable, read_only=True)
        
        return JsonResponse({
            "code" : "11201",
            "message" : "시간표를 불러 왔습니다.",
            "status" : 200,
            "info": serializer.data
        }, status=200)

    if request.method == 'POST':
        return JsonResponse({
        })