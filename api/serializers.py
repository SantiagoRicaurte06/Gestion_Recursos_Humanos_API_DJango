from rest_framework import serializers
from .models import (
    Genero, EstadoCivil, TipoDocumento, NivelCargo, TipoContrato, Estado,
    ModalidadCapacitacion, TipoEvaluacion, ResultadoEvaluacion,
    Departamentos, Cargos, Empleados, Contratos, Nomina, Vacaciones,
    Capacitaciones, Evaluaciones
)

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'


class EstadoCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = '__all__'


class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'


class NivelCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelCargo
        fields = '__all__'


class TipoContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContrato
        fields = '__all__'


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'


class ModalidadCapacitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModalidadCapacitacion
        fields = '__all__'


class TipoEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEvaluacion
        fields = '__all__'


class ResultadoEvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoEvaluacion
        fields = '__all__'

class DepartamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamentos
        fields = '__all__'


class CargosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargos
        fields = '__all__'


class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'


class ContratosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contratos
        fields = '__all__'


class NominaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomina
        fields = '__all__'


class VacacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacaciones
        fields = '__all__'


class CapacitacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capacitaciones
        fields = '__all__'


class EvaluacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluaciones
        fields = '__all__'
