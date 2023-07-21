from .models import App, Sdk, AppSdk
from .serializers import AppSerializer, SdkSerializer, AppSdkSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST,HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from rest_framework import viewsets
import json


# Create your views here.
class AppViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    queryset = App.objects.all()
    serializer_class = AppSerializer

# Create your views here.
class SdkViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    queryset = Sdk.objects.all()
    serializer_class = SdkSerializer


class AppSdkViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    queryset = AppSdk.objects.all()
    serializer_class = AppSdkSerializer


class CurrentSDKAppStatisticsViewSet(viewsets.ViewSet):

    def list(self, request):
        results = dict()

        # default
        sdk_ids = [33, 875, 2081]
        sdk_names = []
        sdk_slugs = []

        # collect payment gateways sdks name & slug
        for gateway in sdk_ids:
            item = Sdk.objects.get(id=gateway)
            if not item:
                return Response("Invalid payment gateway", HTTP_400_BAD_REQUEST)
            sdk_names.append(item.name)
            sdk_slugs.append(item.slug)
        print(sdk_names)

        # results["total"] = len(AppSdk.objects.filter(installed=1))

        # individual sdk's app count
        for indx1 in range(len(sdk_ids)):
            app_ids = AppSdk.objects.filter(sdk_id=sdk_ids[indx1], installed=1).values_list('app_id', flat=True).distinct()
            # print(len(app_ids))
            # print(app_ids[0])
            sub_res = dict()
            sum = 0

            # count each sdk's apps
            for indx2 in range(len(sdk_names)):
                apps = App.objects.filter(id__in=app_ids, seller_name__contains=sdk_slugs[indx2])
                apps = len(apps) if apps else 0
                sub_res[sdk_names[indx2]] = apps
                sum += apps
            sub_res["none"] = len(app_ids)-sum

            # add to the result
            results[sdk_names[indx1]] = sub_res

        # for none
        app_ids = AppSdk.objects.exclude(sdk_id__in=sdk_ids, installed=1).values_list('app_id', flat=True).distinct()
        # print(len(app_ids))
        # print(app_ids[0])
        sub_res = dict()

        sum = 0
        for indx1 in range(len(sdk_names)):
            apps = App.objects.filter(id__in=app_ids, seller_name__contains=sdk_slugs[indx1])
            apps = len(apps) if apps else 0
            sub_res[sdk_names[indx1]] = apps
            sum += apps
        sub_res["none"] = len(app_ids) - sum

        # add to the results
        results["none"] = sub_res
        print(results)
        return Response(json.dumps(results), status=HTTP_200_OK)

    def retrieve(self, request, pk=None):
        # store sdk ids
        sdk_ids = []
        if len(pk.split("_")) > 0:
            for id in pk.split("_"):
                sdk_ids.append(int(id))
            print(sdk_ids)

        # none sdk's apps view
        if len(sdk_ids) > 1:
            # for none
            ids = AppSdk.objects.exclude(sdk_id__in=sdk_ids, installed=1).values_list('app_id', flat=True).distinct()
            print(len(ids))
            apps = App.objects.filter(id__in=ids)
            serializer = AppSerializer(apps, many=True)
            return Response(serializer.data, status=HTTP_200_OK)

        # single sdk's apps view
        elif len(sdk_ids) == 1:
            ids = AppSdk.objects.filter(sdk_id=int(sdk_ids[0]), installed=1).values_list('app_id', flat=True).distinct()
            print(len(ids))
            apps = App.objects.filter(id__in=ids)
            serializer = AppSerializer(apps, many=True)
            return Response(serializer.data, status=HTTP_200_OK)

        # invalid sdk id
        else:
            return Response("Invalid url", status=HTTP_404_NOT_FOUND)

    def post(self, request):
        # response
        results = dict()

        sdk_ids = request.data.get("sdk_ids")
        print(sdk_ids)

        if len(sdk_ids) == 0:
            return Response({}, status=HTTP_400_BAD_REQUEST)

        sdk_names = []
        sdk_slugs = []
        for gateway in sdk_ids:
            item = Sdk.objects.get(id=gateway)
            if not item:
                return Response("Invalid payment gateway", HTTP_400_BAD_REQUEST)
            sdk_names.append(item.name)
            sdk_slugs.append(item.slug)
        print(sdk_names)

        for indx1 in range(len(sdk_ids)):
            obj = Sdk.objects.get(id=gateway).name
            app_ids = AppSdk.objects.filter(sdk_id=sdk_ids[indx1], installed=1).values_list('app_id', flat=True).distinct()
            print(len(app_ids))
            print(app_ids[0])
            sub_res = dict()
            sum = 0
            for indx2 in range(len(sdk_names)):
                apps = App.objects.filter(id__in=app_ids, seller_name__contains=sdk_slugs[indx2])
                apps = len(apps) if apps else 0
                sub_res[sdk_names[indx2]] = apps
                sum += apps
            sub_res["none"] = len(app_ids) - sum
            results[sdk_names[indx1]] = sub_res

        # for none
        app_ids = AppSdk.objects.exclude(sdk_id__in=sdk_ids, installed=1).values_list('app_id', flat=True).distinct()
        sub_res = dict()
        for indx1 in range(len(sdk_names)):
            apps = App.objects.filter(id__in=app_ids, seller_name__contains=sdk_slugs[indx1])
            apps = len(apps) if apps else 0
            sub_res[sdk_names[indx1]] = apps
            sum += apps
        sub_res["none"] = len(app_ids) - sum
        results["none"] = sub_res
        print(results)
        return Response(json.dumps(results), status=HTTP_200_OK)
