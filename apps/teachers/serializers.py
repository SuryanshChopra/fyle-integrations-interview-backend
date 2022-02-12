from attr import attr
from rest_framework import serializers
from apps.students.models import Assignment


class TeacherAssignmentSerializer(serializers.ModelSerializer):
    """
    Teacher Assignment serializer
    """
    class Meta:
        model = Assignment
        fields = '__all__'

    def validate(self, attrs):

        # if 'state' in attrs:
        #     if attrs['state'] == 'DRAFT':
        #         raise serializers.ValidationError('SUBMITTED assignments can only be graded')
        #     if attrs['state'] == 'GRADED':
        #         if 'grade' in attrs and attrs['grade']:
        #             raise serializers.ValidationError('GRADED assignments cannot be graded again')
        #         # else:
        #         #     raise serializers.ValidationError('')
                
        #     if attrs['state'] == 'SUBMITTED':
        #         if not ('teacher' in attrs and attrs['teacher']):
        #             raise serializers.ValidationError('Teacher cannot change the content of the assignment')
        #         else:
        #             pass

        # if 'grade' in attrs and attrs['grade']:
        #     raise serializers.ValidationError('SUBMITTED assignments can only be graded')

        if 'grade' in attrs and attrs['grade']:
            if 'state' in attrs:
                if attrs['state'] == 'DRAFT':
                    raise serializers.ValidationError('SUBMITTED assignments can only be graded')
            


        if 'state' in attrs:
            if attrs['state'] == 'DRAFT' and ('grade' in attrs and attrs['grade']):
                raise serializers.ValidationError('SUBMITTED assignments can only be graded')
            if attrs['state'] == 'GRADED':
                raise serializers.ValidationError('GRADED assignments cannot be graded again')
            if attrs['state'] == 'SUBMITTED' and not ('teacher' in attrs and attrs['teacher']):
                raise serializers.ValidationError('Teacher cannot change the student who submitted the assignment')


        

        
        
        if self.partial:
            return attrs

        return super().validate(attrs)
