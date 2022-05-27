from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from field.models import Field, FieldDetails
from field.serializers import FieldSerializer, FieldDetailsSerializer


class FieldViewSet(ModelViewSet):
    queryset = Field.objects.all().order_by('pk')
    serializer_class = FieldSerializer

    @action(methods=["GET"], detail=False)
    def search_spec(self, request):
        name_spec = request.GET.get('name', None)
        sensitive_data_spec = request.GET.get('sensitive_data', None)

        if name_spec:
            self.queryset = self.queryset.filter(name__contains=name_spec)

        if sensitive_data_spec:
            self.queryset = self.queryset.filter(sensitive_data__iexact=sensitive_data_spec)

        return self.list(request)


class FieldDetailViewSet(ModelViewSet):
    queryset = FieldDetails.objects.all().order_by('pk')
    serializer_class = FieldDetailsSerializer
