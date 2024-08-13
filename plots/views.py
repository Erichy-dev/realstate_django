from django.shortcuts import get_object_or_404

from .models import Plot, PlotPic
from .serializers import PlotSerializer, PlotPicSerializer, PlotOccupantSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(["GET"])
def get_plots(request):
    try:
        plots = Plot.objects.all()
        serialized_plots = PlotSerializer(plots, many=True)
        return Response({'plots': serialized_plots.data})
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def get_plot(request, plot_number):
    try:
        plot = Plot.objects.get(plot_number=plot_number)
        serialized_plot = PlotSerializer(plot)
        return Response({'plot': serialized_plot.data})
    except Plot.DoesNotExist:
        return Response({'message': 'Plot not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(["GET"])
def get_plot_pics(request, plot_number):
    try:
        plot = get_object_or_404(Plot, plot_number=plot_number)
        plot_pics = PlotPic.objects.filter(plot_number=plot)
        serialized_pics = PlotPicSerializer(plot_pics, many=True)
        return Response({'plot_pics': serialized_pics.data}, status=status.HTTP_200_OK)

    except Plot.DoesNotExist:
        return Response({'message': 'Plot not found'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def create_plot_pics(request):
    try:
        plot_pics_data = request.data.get('plot_pics', [])

        created_pics = []
        for pic_data in plot_pics_data:
            plot_number = pic_data.get('plot_number')
            plot = get_object_or_404(Plot, plot_number=plot_number)

            serializer = PlotPicSerializer(data=pic_data)
            if serializer.is_valid():
                serializer.save(plot_number=plot)
                created_pics.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'plot_pics': created_pics}, status=status.HTTP_201_CREATED)

    except Plot.DoesNotExist:
        return Response({'message': 'Plot not found'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(["GET"])
def get_plot_caretakers(request, plot_number):
    try:
        plot = get_object_or_404(Plot, plot_number=plot_number)
        caretakers = plot.plotoccupant_set.filter(plot_occupant_class='caretaker')
        serialized_caretakers = PlotOccupantSerializer(caretakers, many=True)
        return Response({'caretakers': serialized_caretakers.data})

    except Plot.DoesNotExist:
        return Response({'message': 'Plot not found'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def create_plot_occupant(request):
    try:
        plot_number = request.POST.get('plot_number')
        plot = get_object_or_404(Plot, plot_number=plot_number)

        serializer = PlotOccupantSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save(plot_number=plot)
            return Response({'occupant': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Plot.DoesNotExist:
        return Response({'message': 'Plot not found'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    