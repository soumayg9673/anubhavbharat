from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from business import models as BModel


class OrgTypesSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model = BModel.OrgType
        fields = ['id','entity','doc','desc']


class AddOrgSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    reg_no = serializers.CharField(write_only=True,
            validators=[UniqueValidator(queryset=BModel.Org.objects.all())])
    doc = serializers.FileField(write_only=True)
    class Meta:
        model = BModel.Org
        exclude = ['is_active','is_verified','created_at','updated_at']

    def create(self, validated_data):
        org = super().create(validated_data)
        # add associated user as manager in org
        org_emp = BModel.OrgEmp.objects.create(
            org = org,
            user = self.context.get('user'),
            is_manager = True
        )
        org_emp.save
        return org


class OrgListSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    class Meta:
        model = BModel.Org
        exclude = ['type','reg_no','doc','created_at','updated_at']


class OrgInfoSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    type = serializers.CharField()
    emp = serializers.SerializerMethodField()
    class Meta:
        model = BModel.Org
        fields = ['id','name','type','emp']
    
    def get_emp(self, instance):
        return BModel.OrgEmp.objects.filter(org=instance).count()


class AddOrgEmpSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False, read_only=True)
    user = serializers.CharField()
    class Meta:
        model = BModel.OrgEmp
        exclude = ['created_at','updated_at','is_delete']

    def create(self, validated_data):
        org_emp = BModel.OrgEmp.objects.create(
            org = validated_data['org'],
            user = self.context.get('user'),
            is_manager = validated_data['is_manager']
        )
        org_emp.save
        return org_emp
