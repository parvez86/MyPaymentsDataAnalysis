from .models import App, Sdk, AppSdk
from .serializers import AppSerializer, SdkSerializer, AppSdkSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
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
        # normal stats
        results1 = dict()

        # norm stats
        results2 = dict()

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

        # results1["total"] = len(AppSdk.objects.filter(installed=1))

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
            results1[sdk_names[indx1]] = sub_res

            # add norm results
            sub_res2 = dict()
            for indx in sub_res:
                sub_res2[indx] = round(sub_res[indx]/len(app_ids)*100, 3)
            results2[sdk_names[indx1]] = sub_res2

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
        results1["none"] = sub_res

        # add norm results
        sub_res2 = dict()
        for indx in sub_res:
            sub_res2[indx] = round(sub_res[indx] / len(app_ids) * 100, 3)
        results2["none"] = sub_res2

        print("normal: ", results1)
        print("norm: ", results2)

        return Response(json.dumps({
            "original": results1,
            "norm": results2
        }), status=HTTP_200_OK)

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
        # original sdk stats
        results1 = dict()

        # norm sdk stats
        results2 = dict()

        sdk_ids = request.data.get("sdk_ids")
        print("sdk_ids: ", sdk_ids)

        if len(sdk_ids) == 0:
            return Response({}, status=HTTP_400_BAD_REQUEST)

        sdk_names = []
        sdk_slugs = []
        for gateway in sdk_ids:
            try:
                item = Sdk.objects.get(id=gateway)
            except (Exception | ValueError) as err:
                return Response({"error": err}, status=HTTP_400_BAD_REQUEST)
            if not item:
                return Response({"error": "Invalid payment gateway"}, HTTP_400_BAD_REQUEST)
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
            results1[sdk_names[indx1]] = sub_res

            # add norm results
            sub_res2 = dict()
            for indx in sub_res:
                sub_res2[indx] = round(sub_res[indx] / len(app_ids) * 100, 3)
            results2[sdk_names[indx1]] = sub_res2

        # for none
        app_ids = AppSdk.objects.exclude(sdk_id__in=sdk_ids, installed=1).values_list('app_id', flat=True).distinct()
        sub_res = dict()
        for indx1 in range(len(sdk_names)):
            apps = App.objects.filter(id__in=app_ids, seller_name__contains=sdk_slugs[indx1])
            apps = len(apps) if apps else 0
            sub_res[sdk_names[indx1]] = apps
            sum += apps
        sub_res["none"] = len(app_ids) - sum
        results1["none"] = sub_res

        # add norm results
        sub_res2 = dict()
        for indx in sub_res:
            sub_res2[indx] = round(sub_res[indx] / len(app_ids) * 100, 3)
        results2["none"] = sub_res2

        print(results1)
        return Response(json.dumps({
            "original": results1,
            "norm": results2
        }), status=HTTP_200_OK)


class SDKAppListViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({}, status=HTTP_200_OK)

    def post(self, request):
        # original sdk stats
        results1 = dict()
        ids1 = request.data.get("ids1")
        ids2 = request.data.get("ids2")
        print("ids1: ", ids1)
        print("ids2: ", ids2)

        if len(ids1) == 0 or len(ids2) == 0:
            return Response({}, status=HTTP_400_BAD_REQUEST)

        app_ids = []
        if len(ids1) == 1:
            app_ids = app_ids = AppSdk.objects.filter(sdk_id=ids1[0], installed=1).values_list('app_id', flat=True).distinct()
        else:
            app_ids = AppSdk.objects.exclude(sdk_id__in=ids1, installed=1).values_list('app_id', flat=True).distinct()

        print("apps ids: ", len(app_ids))
        apps = []
        if len(ids2) == 1:
            seller_name = Sdk.objects.get(id=ids2[0])
            seller_name = seller_name.slug
            apps = App.objects.filter(id__in=app_ids, seller_name__contains=seller_name)

        else:
            seller_names = Sdk.objects.filter(id__in=ids2).values_list('slug', flat=True)
            print(seller_names)
            apps = App.objects.exclude(seller_name__contains=seller_names).filter(id__in=app_ids)

        print(len(apps))

        serializer = AppSerializer(apps, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
