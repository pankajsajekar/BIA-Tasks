from django.http import HttpResponse
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, vfx
from rest_framework.views import APIView
from rest_framework.response import Response
from task5.serializers import UploadedVideoSerializer
from rest_framework.parsers import MultiPartParser
import os
import io
from django.conf import settings

# Generate Video View
class UploadVideoView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        serializer = UploadedVideoSerializer(data=request.data)
        if serializer.is_valid():
            video = serializer.validated_data['video']
            
            # uploaded video using MoviePy
            video_clip = VideoFileClip(video.temporary_file_path()).subclip(0,6).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
            txt_clip = TextClip('Hello From Pankaj', fontsize=170, color='black')
            txt_clip = txt_clip.set_position('center').set_duration(video_clip.duration)
            
            video_with_text = CompositeVideoClip([video_clip, txt_clip])
            
            edited_video_path = video.name.split('.')[0] + '_edited.mp4'
            edited_video_path = os.path.join( settings.MEDIA_ROOT , edited_video_path)
            video_with_text.write_videofile(edited_video_path, codec='libx264', fps=24)
            
            serializer.save(edited_video=video_with_text)
            
            # Return the edited video as a downloadable file
            with open(edited_video_path, 'rb') as output_file:
                output_video_io = io.BytesIO(output_file.read())

            response = HttpResponse(output_video_io.getvalue(), content_type='video/mp4')
            response['Content-Disposition'] = 'inline; filename=output.mp4'
            return response
        return Response(serializer.errors, status=400)
