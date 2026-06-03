from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Genero, EstadoCivil, TipoDocumento, NivelCargo, TipoContrato, Estado,
    ModalidadCapacitacion, TipoEvaluacion, ResultadoEvaluacion,
    Departamentos, Cargos, Empleados, Contratos, Nomina, Vacaciones,
    Capacitaciones, Evaluaciones
)
from .serializers import (
    GeneroSerializer, EstadoCivilSerializer, TipoDocumentoSerializer,
    NivelCargoSerializer, TipoContratoSerializer, EstadoSerializer,
    ModalidadCapacitacionSerializer, TipoEvaluacionSerializer,
    ResultadoEvaluacionSerializer, DepartamentosSerializer, CargosSerializer,
    EmpleadosSerializer, ContratosSerializer, NominaSerializer,
    VacacionesSerializer, CapacitacionesSerializer, EvaluacionesSerializer
)
from .filters import (
    GeneroFilter, EstadoCivilFilter, TipoDocumentoFilter, NivelCargoFilter,
    TipoContratoFilter, EstadoFilter, ModalidadCapacitacionFilter,
    TipoEvaluacionFilter, ResultadoEvaluacionFilter, DepartamentosFilter,
    CargosFilter, EmpleadosFilter, ContratosFilter, NominaFilter,
    VacacionesFilter, CapacitacionesFilter, EvaluacionesFilter
)

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GeneroFilter
    ordering_fields = '__all__'


class EstadoCivilViewSet(viewsets.ModelViewSet):
    queryset = EstadoCivil.objects.all()
    serializer_class = EstadoCivilSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EstadoCivilFilter
    ordering_fields = '__all__'


class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TipoDocumentoFilter
    ordering_fields = '__all__'


class NivelCargoViewSet(viewsets.ModelViewSet):
    queryset = NivelCargo.objects.all()
    serializer_class = NivelCargoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NivelCargoFilter
    ordering_fields = '__all__'


class TipoContratoViewSet(viewsets.ModelViewSet):
    queryset = TipoContrato.objects.all()
    serializer_class = TipoContratoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TipoContratoFilter
    ordering_fields = '__all__'


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EstadoFilter
    ordering_fields = '__all__'


class ModalidadCapacitacionViewSet(viewsets.ModelViewSet):
    queryset = ModalidadCapacitacion.objects.all()
    serializer_class = ModalidadCapacitacionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ModalidadCapacitacionFilter
    ordering_fields = '__all__'


class TipoEvaluacionViewSet(viewsets.ModelViewSet):
    queryset = TipoEvaluacion.objects.all()
    serializer_class = TipoEvaluacionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TipoEvaluacionFilter
    ordering_fields = '__all__'


class ResultadoEvaluacionViewSet(viewsets.ModelViewSet):
    queryset = ResultadoEvaluacion.objects.all()
    serializer_class = ResultadoEvaluacionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ResultadoEvaluacionFilter
    ordering_fields = '__all__'

class DepartamentosViewSet(viewsets.ModelViewSet):
    queryset = Departamentos.objects.all()
    serializer_class = DepartamentosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DepartamentosFilter
    ordering_fields = '__all__'


class CargosViewSet(viewsets.ModelViewSet):
    queryset = Cargos.objects.all()
    serializer_class = CargosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CargosFilter
    ordering_fields = '__all__'


class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmpleadosFilter
    ordering_fields = '__all__'


class ContratosViewSet(viewsets.ModelViewSet):
    queryset = Contratos.objects.all()
    serializer_class = ContratosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContratosFilter
    ordering_fields = '__all__'


class NominaViewSet(viewsets.ModelViewSet):
    queryset = Nomina.objects.all()
    serializer_class = NominaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NominaFilter
    ordering_fields = '__all__'


class VacacionesViewSet(viewsets.ModelViewSet):
    queryset = Vacaciones.objects.all()
    serializer_class = VacacionesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VacacionesFilter
    ordering_fields = '__all__'


class CapacitacionesViewSet(viewsets.ModelViewSet):
    queryset = Capacitaciones.objects.all()
    serializer_class = CapacitacionesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CapacitacionesFilter
    ordering_fields = '__all__'


class EvaluacionesViewSet(viewsets.ModelViewSet):
    queryset = Evaluaciones.objects.all()
    serializer_class = EvaluacionesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EvaluacionesFilter
    ordering_fields = '__all__'
