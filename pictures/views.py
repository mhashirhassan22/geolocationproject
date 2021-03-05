from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View,ListView
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from pictures.models import Favorites,Location
import flickrapi
import json
from pprint import pprint
# Create your views here.

api_key = u'f1f545c2cf2b245c7cce729033afbc4b'
api_secret = u'72b7c483273a7af8'
flickr = flickrapi.FlickrAPI(api_key, api_secret,format='parsed-json')


class index(View):

    def get(self,request):
        user_loc = None
        if self.request.user.is_authenticated:
            user_loc = Location.objects.filter(user=self.request.user)
        context = {
            'locations':user_loc
        }
        return render(request,'index.html',context)

    @method_decorator(login_required(), name="dispatch")
    def post(self,request):
        lat = json.loads(request.POST.get("lat"))
        longitude = json.loads(request.POST.get("long"))
        name = json.loads(request.POST.get("name"))
        user_id = self.request.user
        new_location = Location.objects.filter(latitude=lat,longitude=longitude,name=name,user=user_id)
        if new_location:
            return JsonResponse({"status": "present"})
        else:
            new_location = Location(latitude=lat,longitude=longitude,name=name,user=user_id)
            new_location.save()
            return JsonResponse({"status": "added"})


@method_decorator(login_required(), name="dispatch")
class View_Favorites(View):

     def get(self,request):
        user_favorites = Favorites.objects.filter(user=self.request.user)
        context = {
            'favorites':user_favorites
        }
        return render(request,'favorites.html',context)


class pictures(View):

    def get(self,request): # new
        lat = self.request.GET.get('lat')
        longitude = self.request.GET.get('long')
        if lat and longitude:
            try:
                pics = flickr.photos.search(lat=lat,lon=longitude)
            except :
                raise ValidationError('Invalid value')
            photos = pics["photos"]
            context = {
                'photos':photos
            }
            return render(request,'pictures.html',context)
        else:
            return HttpResponseRedirect(reverse('pictures:index'))


class add_or_remove_favorite(View):

    def post(self,request):
        if self.request.user.is_authenticated:
            server = json.loads(request.POST.get("server"))
            photo_id = json.loads(request.POST.get("id"))
            secret = json.loads(request.POST.get("secret"))
            user_id = self.request.user

            fav_photo = Favorites.objects.filter(server=server,photo_id=photo_id,secret=secret,user=user_id)
            if fav_photo:
                fav_photo.delete()
                return JsonResponse({"status": "removed"})
            else:
                fav_photo = Favorites(user = user_id,server=server,photo_id=photo_id,secret=secret)
                fav_photo.save()
                return JsonResponse({"status": "added"})
        else:
            return JsonResponse({"status": "not authenticated"})
