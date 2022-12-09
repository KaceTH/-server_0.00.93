from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Timetable.models import TableCell, TimeTable


class SimpleTimeCellSerializer(ModelSerializer):
    class Meta:
        model = TableCell
        fields = [
            'subject',
            'location',
            'teacher',
            'number'
        ]


class ReadSimpleScedule(ModelSerializer):
    sun = SimpleTimeCellSerializer(read_only=True, many=True)
    mon = SimpleTimeCellSerializer(read_only=True, many=True)
    tue = SimpleTimeCellSerializer(read_only=True, many=True)
    wed = SimpleTimeCellSerializer(read_only=True, many=True)
    thu = SimpleTimeCellSerializer(read_only=True, many=True)
    fri = SimpleTimeCellSerializer(read_only=True, many=True)
    set = SimpleTimeCellSerializer(read_only=True, many=True)

    class Meta:
        model = TimeTable
        fields = '__all__'
