# import pyaudio
# import wave

# from vosk import Model, KaldiRecognizer, SetLogLevel
# from pydub import AudioSegment
# import subprocess
# import json
# import os
# import io
# import os
# import json
# import pyaudio
# import wave
# import librosa
# import librosa.display

# from vosk import Model, KaldiRecognizer, SetLogLevel
# from pydub import AudioSegment
# import subprocess

# - - - - - - - - - - - - - - - - - - - 

# ОПРЕДЕЛЕНИЕ ИНДЕКСА МИКРОФОНА input_device_index в зависимости от устройства
# в моем случае это 0
# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     print(i, p.get_device_info_by_index(i)['name'])

# - - - - - - - - - - - - - - - - - - - 

# def analyze_audio_blob(audio_blob):

#     # Загрузка аудио из blob данных
#     y, sr = librosa.load(audio_blob)

#     # Параметры аудио
#     duration = librosa.get_duration(y=y, sr=sr)  # Длительность аудио
#     sample_rate = sr  # Частота дискретизации
#     num_channels = 1 if len(y.shape) == 1 else y.shape[0]  # Количество каналов

#     return duration, sample_rate, num_channels

# # Пример использования
# audio_blob = "./media/blob"
# duration, sample_rate, num_channels = analyze_audio_blob(audio_blob)

# print("Длительность аудио:", duration, "секунд")
# print("Частота дискретизации:", sample_rate, "Гц")
# print("Количество каналов:", num_channels)

# - - - - - - - - - - - - - - - - - - - 
# МУСОРКА
# - - - - - - - - - - - - - - - - - - - -

# class RecordAudioView(APIView):
#     def post(self, request):

        # serializer = AudioFileSerializer(data=request.FILES)
        # if serializer.is_valid():
        #     audio_file = serializer.validated_data['audio_file']
            
#             # Обработка аудиофайла, например, сохранение на сервере
#             file_path = os.path.join(settings.MEDIA_ROOT, audio_file.name)
#             # with open(file_path, 'wb') as f:
#             #     for chunk in audio_file.chunks():
#             #        f.write(chunk)

#             # Открываем WAV-файл и записываем в него данные аудио
#             with wave.open(file_path, 'wb') as wf:
                
#                 wf.setnchannels(1)  # Устанавливаем количество каналов
#                 wf.setsampwidth(2)  # Устанавливаем ширину образа
#                 wf.setframerate(22050)  # Устанавливаем частоту дискретизации
#                 wf.writeframes(audio_file.read())  # Записываем данные аудиофайла в WAV-файл
            
#             # Возвращаем ответ об успешной загрузке
#             return Response({'message': 'Аудиофайл успешно загружен'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Открываем файл с аудио (замените 'audio_file.wav' на путь к вашему файлу)
#             audio_file_path = 'audio_file.wav'
#             wf = wave.open(audio_file_path, 'rb')

#             # Создаем экземпляр PyAudio
#             p = pyaudio.PyAudio()

#             # Открываем поток для воспроизведения
#             stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                             channels=wf.getnchannels(),
#                             rate=wf.getframerate(),
#                             output=True)

#             # Читаем и воспроизводим аудио
#             data = wf.readframes(1024)
#             while data:
#                 stream.write(data)
#                 data = wf.readframes(1024)

#             # Останавливаем поток
#             stream.stop_stream()
#             stream.close()

#             # Закрываем PyAudio
#             p.terminate()

# - - - - - - - - - - - - - - - - - - - -
# import os
# import wave
# from django.conf import settings
# from django.shortcuts import render
# import pyaudio
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from transcription.serializers import AudioSerializer

# # views.py
# from django.http import JsonResponse

# def record_audio(request):
#     if request.method == 'POST' and request.FILES.get('audio_file'):
#         audio_file = request.FILES['audio_file']
#         # Обработка и сохранение файла audio_file

#         # Сохранение файла аудио на сервере
#         # file_path = os.path.join(settings.MEDIA_ROOT, audio_file.name)
#         file_path = f'./transcription/static/sound/sound.wav'
#         with open(file_path, 'wb') as file:
#             for chunk in audio_file.chunks():
#                 file.write(chunk)

#         chunk = 2048  # Запись кусками по 2048 сэмпла 
#         sample_format = pyaudio.paInt16  # 16 бит на выборку
#         channels = 2
#         rate = 44100  # Запись со скоростью 44100 выборок(samples) в секунду
#         seconds = 10  # Запись 10 секунд
#         filename = "output_sound.wav"
#         p = pyaudio.PyAudio()  # Создать интерфейс для PortAudio

#         print('Recording...')

#         stream = p.open(format=sample_format,
#                         channels=channels,
#                         rate=rate,
#                         frames_per_buffer=chunk,
#                         input_device_index=0,  # индекс устройства с которого будет идти запись звука
#                         input=True)

#         frames = []  # Инициализировать массив для хранения кадров

#         # Хранить данные в блоках в течение n секунд
#         for i in range(0, int(rate / chunk * seconds)):
#             data = stream.read(chunk)
#             frames.append(data)

#         # Остановить и закрыть поток
#         stream.stop_stream()
#         stream.close()

#         # Завершить интерфейс PortAudio
#         p.terminate()

#         msg_finished = 'Finished recording!'

#         # Сохранить записанные данные в виде файла WAV
#         wf = wave.open(f'./transcription/static/sound/{filename}', 'wb')
#         wf.setnchannels(channels)
#         wf.setsampwidth(p.get_sample_size(sample_format))
#         wf.setframerate(rate)  # Исправлено на переменную "rate"
#         wf.writeframes(b''.join(frames))
#         wf.close()

#         print('YESS')
#         return JsonResponse({'success': True})

#     else:
#         return render(request, 'record_audio.html', {'success': False})

# - - - - - - - - - - - - - - - - - - - 
# def in_sound(request):
#     '''
#     Запись звука по материалам "Python. Используем PyAudio для записи звука"
#     https://blog-programmista.ru/post/103-python-ispolzuem-pyaudio-dla-zapisi-zvuka.html
#     '''
#     

    # chunk = 2048  # Запись кусками по 2048 сэмпла 
    # sample_format = pyaudio.paInt16  # 16 бит на выборку
    # channels = 2
    # rate = 44100  # Запись со скоростью 44100 выборок(samples) в секунду
    # seconds = 10
    # filename = "output_sound.wav"
    # p = pyaudio.PyAudio()  # Создать интерфейс для PortAudio

    # print('Recording...')

    # # ОПРЕДЕЛЕНИЕ ИНДЕКСА МИКРОФОНА input_device_index в зависимости от устройства
    # # в моем случае это 0
    # # p = pyaudio.PyAudio()
    # # for i in range(p.get_device_count()):
    # #     print(i, p.get_device_info_by_index(i)['name'])

    # stream = p.open(format=sample_format,
    #                 channels=channels,
    #                 rate=rate,
    #                 frames_per_buffer=chunk,
    #                 input_device_index=0,  # индекс устройства с которого будет идти запись звука
    #                 input=True)

    # frames = []  # Инициализировать массив для хранения кадров

    # # Хранить данные в блоках в течение n секунд
    # for i in range(0, int(rate / chunk * seconds)):
    #     # Добавим проверку на доступность данных в потоке для чтения
    #     # if stream.get_read_available() >= chunk:
    #     data = stream.read(chunk)
    #     # else:
    #     #     break  # Прерываем цикл, чтобы избежать переполнения ввода
    #     frames.append(data)

    # # Остановить и закрыть поток
    # stream.stop_stream()
    # stream.close()

    # # Завершить интерфейс PortAudio
    # p.terminate()

    # msg_finished = 'Finished recording!'

    # # Сохранить записанные данные в виде файла WAV
    # wf = wave.open(f'./transcription/static/sound/{filename}', 'wb')
    # wf.setnchannels(channels)
    # wf.setsampwidth(p.get_sample_size(sample_format))
    # wf.setframerate(rate)  # Исправлено на переменную "rate"
    # wf.writeframes(b''.join(frames))
    # wf.close()
    # return HttpResponse(msg_finished)

# - - - - - - - - - - - - - - - - - - - 
# # Конвертор wav в mp3
#     def convert_wav_to_mp3(wav_file_path, mp3_file_path):
#         sound = AudioSegment.from_wav(wav_file_path)
#         sound.export(mp3_file_path, format="mp3")

#     # Пример использования:
#     wav_file_path = './transcription/static/sound/output_sound.wav'
#     mp3_file_path = './transcription/static/sound/output_sound.mp3'
#     convert_wav_to_mp3(wav_file_path, mp3_file_path)


# - - - - - - - - - - - - - - - - - - -
# # Транскрибация
# def sound_in_text(request):
#     '''
#     По материалам "Решаем задачу перевода русской речи в текст с помощью Python и библиотеки Vosk" 
#     https://proglib.io/p/reshaem-zadachu-perevoda-russkoy-rechi-v-tekst-s-pomoshchyu-python-i-biblioteki-vosk-2022-06-30
#     (при установке в конду использовать conda install -c conda-forge ffmpeg)
#     Открытые модели для распознавания русской речи:
#     https://alphacephei.com/nsh/2023/01/15/russian-models.html
#     '''
    
#     SetLogLevel(0)  # Логирование

#     # Задаем путь к статике и медиа
#     static_path = os.path.join(settings.STATICFILES_DIRS[0])
#     media_path = os.path.join(settings.MEDIA_ROOT)

#     # Проверяем наличие модели в текущей рабочей директории
#     if not os.path.exists(static_path + "/speech/model"):
#         print("Пожалуйста, загрузите модель с https://alphacephei.com/vosk/models и разархивируйте как 'model' в текущей папке.")
#         # преждевременное завершение программы из-за отсутствия модели, необходимой для работы дальнейших инструкций.
#         exit(1)

#     # Устанавливаем Frame Rate
#     FRAME_RATE = 16000
#     CHANNELS = 1

#     model = Model(static_path + "/speech/model")
#     rec = KaldiRecognizer(model, FRAME_RATE)
#     rec.SetWords(True)

#     # Используя библиотеку pydub делаем предобработку аудио
#     mp3 = AudioSegment.from_mp3('./media/recorded_audio.mp3')
#     mp3 = mp3.set_channels(CHANNELS)
#     mp3 = mp3.set_frame_rate(FRAME_RATE)

#     # Преобразуем вывод строки json "{\n  \"text\" : \"\"\n}" в словарь Python
#     rec.AcceptWaveform(mp3.raw_data)
#     result = rec.Result()
#     text = json.loads(result)["text"]

#     # Сохраняем результат в файл JSON
#     with open(static_path + '/speech/result.json', 'w', encoding='utf-8') as f:
#         json.dump(text, f, ensure_ascii=False, indent=4)

#     # Добавляем пунктуацию (требует наличия ядер CUDA)
#     # cased = subprocess.check_output('python3 ./transcription/static/speech/recasepunc/recasepunc.py predict ./transcription/static/speech/recasepunc/checkpoint', shell=True, text=True, input=text)

#     # with open(static_path + '/speech/data.txt', 'w') as f:
#     #    json.dump(cased, f, ensure_ascii=False, indent=4)

#     return HttpResponse('Finished transcription!')

# - - - - - - - - - - - - - - - - - - -
# # Добавление полнотекстового поиска
# def search(request):
#     '''
#     Поиск по нескольким полям
#     Выделение основ слов 
#     Ранжирование результатов
#     Удаление стоп-слов на разных языках
#     Взвешивание запросов

#     '''
#     query = 'да подтвердить операцию' 
#     searchresult = []
#     search_vector = SearchVector('commands', weight='A', config='russian') + \
#                     SearchVector('confirmation', weight='B', config='russian')
#     search_query = SearchQuery(query, config='russian')
#     searchresult = Commands.objects.annotate(
#                     search=search_vector,
#                     rank=SearchRank(search_vector, search_query)
#                     ).filter(rank__gte=0.3).order_by('-rank') 
#     if [searchresult for searchresult in searchresult] == []:   
#         return HttpResponse('Извините я Вас не поняла, переключаю на оператора')
#     return HttpResponse(searchresult)

# # Поиск по триграммному сходству 
# # (требует дополнительного расширения postgresql pg_trgm)
# def trgm_search(request):
#     '''
#     Поиск по триграммному сходству
#     Дополнительные настройки расширений postgresql:
#     psql admin
#     CREATE EXTENSION pg_trgm;
#     '''
#     query = 'да подтвердить операцию' 
#     searchresult = []
#     searhfld = ['commands', 'confirmation']
#     for allresult in searhfld:
#         searchresult = Commands.objects.annotate(
#                         similarity=TrigramSimilarity(allresult, query),
#                         ).filter(similarity__gt=0.1).order_by('-similarity')
#     if [searchresult for searchresult in searchresult] == []:   
#         return HttpResponse('Извините я Вас не поняла, переключаю на оператора')
#     return HttpResponse(searchresult) # ПЕРЕНАПРАВИТЬ НА МИКРОФОН



# Эндпоинт для сохранения и постобработки audioBlob
# class CreateAudioView(APIView):
    
#     def post(self, request):
#         serializer = AudioFileSerializer(data=request.FILES)
#         if serializer.is_valid():
#             audio_file = serializer.validated_data['audio']
#             # Сохранение аудиофайла в папке media
#             media_path = os.path.join(settings.MEDIA_ROOT, audio_file.name)
#             audio_segment = AudioSegment.from_file(audio_file)
#             audio_file_mp3 = audio_segment.export(media_path, format="mp3") # Поменять здесь и на фронте audioBlob, 
#             # Выполняем функцию транскрибации
#             convert_text = sound_in_text(audio_file_mp3) 
#             # Выполняем функцию триграммного поиска соответствий в модели БД Commands 
#             search_text = trgm_search(convert_text)

#             command = [command.slug for command in Commands.objects.filter(commands=search_text)]
             
#             if (convert_text and search_text): 
#                 if (convert_text and search_text == 'Да'): # Извлечь запись из БД
#                     # Перейти по slug-адресу функции и выполнить ее
#                     context = {
#                         'convert_text': convert_text,
#                         'search_text': 'Выполняю операцию.'
#                     } 
#                     print(command)
#                 elif (convert_text and search_text == 'Нет'): # Извлечь запись из БД
#                     context = {
#                         'convert_text': convert_text,
#                         'search_text': 'Отменяю операцию. Пока!'
#                     } 
#                     print('Пока!') 
#                 else:
#                     # Если текст распознан и команда найдена, включаем в тело ответа context
#                     context = {
#                         'convert_text': convert_text,
#                         'search_text': f'Вы ввели команду {search_text}. Подтверждаете? Ответьте да, нет.' 
#                     }                
#                     # Если текст распознан и команда найдена возвращаем значение поля slug (он будет содержать url функции)
#                     # command = [command.slug for command in Commands.objects.filter(commands=search_text)] 
#                     # print(command)
#             # elif (convert_text and search_text == 'Да'): # Извлечь запись из БД
#             #     # Перейти по slug-адресу функции и выполнить ее
#             #     context = {
#             #         'convert_text': convert_text,
#             #         'search_text': 'Выполняю операцию.'
#             #     } 
#             #     print(command)
#             # elif (convert_text and search_text == 'Нет'): # Извлечь запись из БД
#             #     context = {
#             #         'convert_text': convert_text,
#             #         'search_text': 'Отменяю операцию. Пока!'
#             #     } 
#             #     print('Пока!')
#             else:
#                 # Если текст не распознан, то команда будет не найдена. Включаем в тело ответа context
#                 context = {
#                     'convert_text': convert_text,
#                     'search_text': search_text # Извините я Вас не поняла, переключаю на оператора
#                 } 
#                 print(context)
            
#             # if search_text:
#             #     command = [command.slug for command in Commands.objects.filter(commands=search_text)] 
#             #     print(command)
                                                 
#             return Response(context, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Если звук с микрафона присутствует и распознана команда
        #     if convert_text and search_text: 
        #         if convert_text and search_text == 'Да': # Извлечь запись из БД
        #             # Перейти по slug-адресу функции и выполнить ее
        #             context = {
        #                 'convert_text': convert_text,
        #                 'search_text': 'Выполняю операцию.'
        #             } 
        #             print(command)
        #         elif convert_text and search_text == 'Нет': # Извлечь запись из БД
        #             # Никуда не переходить и сказать пока
        #             context = {
        #                 'convert_text': convert_text,
        #                 'search_text': 'Отменяю операцию. Пока!'
        #             } 
        #             print('Пока!')
        #         else:
        #             # Если текст распознан и команда найдена, включаем в тело ответа такой context
        #             context = {
        #                 'convert_text': convert_text,
        #                 'search_text': f'Вы ввели команду {search_text}. Подтверждаете? Ответьте да, нет.' 
        #             }  
        #     else:
        #         # Если текст не распознан, то команда будет не найдена. Включаем в тело ответа context
        #         context = {
        #             'convert_text': convert_text,
        #             'search_text': search_text # Извините я Вас не поняла, переключаю на оператора
        #         } 
        #         print(context)
                           
        #     return Response(context, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Использование функции handle_command
            # context = handle_command(convert_text, search_text)
            # print(context)
            # # Если звук с микрафона присутствует и распознана команда
            # # if convert_text: 
            # #     if search_text:
            # #         # Если текст распознан и команда найдена, включаем в тело ответа такой context
            # #         context = {
            # #             'convert_text': convert_text,
            # #             'search_text': f'Вы ввели команду {search_text}. Подтверждаете? Ответьте да, нет.' 
            # #         } 
            # #         # По найденному search_text ищем адрес функции в поле слаг 
            # #         func = [command.slug for command in Commands.objects.filter(commands=search_text)]
            # #         with open(settings.STATICFILES_DIRS[0] + '/command.json', 'w', encoding='utf-8') as infile:
            # #             json.dump(func, infile)
                    
            # #         if search_text == 'Да': # Извлечь запись из БД
            # #             # Перейти по slug-адресу функции и выполнить ее
            # #             context = {
            # #                 'convert_text': convert_text,
            # #                 'search_text': 'Выполняю операцию.'
            # #             } 
            # #             with open(settings.STATICFILES_DIRS[0] + '/command.json', 'r', encoding='utf-8') as outfile:
            # #                 data = json.load(outfile)
            # #                 print(data)  # Здесь вы можете использовать данные, загруженные из файла

            # #             # print(validpoint)
            # #         elif search_text == 'Нет': # Извлечь запись из БД
            # #             # Никуда не переходить и сказать пока
            # #             context = {
            # #                 'convert_text': convert_text,
            # #                 'search_text': 'Отменяю операцию. Пока!'
            # #             }    
            # #             print('Пока!')
            # #     else:
            # #         context = {
            # #         'convert_text': convert_text,
            # #         'search_text': 'Извините я Вас не поняла, переключаю на оператора' # Извините я Вас не поняла, переключаю на оператора
            # #         } 
            # #         print(context)
                 
            # # else:
            # #     # Если текст не распознан, то команда будет не найдена. Включаем в тело ответа context
            # #     context = {
            # #         'convert_text': convert_text,
            # #         'search_text': 'Извините я Вас не поняла, переключаю на оператора' # Извините я Вас не поняла, переключаю на оператора
            # #     } 
            # #     print(context)




# def handle_command(convert_text, search_text):
#     context = {}
    
#     if convert_text and search_text:
#         command = Commands.objects.filter(commands=search_text).first()
#         if command:
#             context['convert_text'] = convert_text
#             context['search_text'] = f'Вы ввели команду {search_text}. Подтверждаете? Ответьте да, нет.'
            
#             with open(settings.STATICFILES_DIRS[0] + '/command.json', 'a', encoding='utf-8') as infile:  # Открываем файл для добавления данных
#                 infile.write(command.slug + '\n')  # Добавляем slug в файл
                
#             if search_text == 'Да':
#                 execute_command(context)
#             elif search_text == 'Нет':
#                 context['search_text'] = 'Отменяю операцию. Пока!'
#         else:
#             context['search_text'] = 'Извините, я Вас не поняла. Переключаю на оператора'
#     else:
#         context['convert_text'] = convert_text
#         context['search_text'] = 'Извините, я Вас не поняла. Переключаю на оператора'

#     return context

# def execute_command(context):
#     # Перейти по slug-адресу функции и выполнить ее
#     context['search_text'] = 'Выполняю операцию.'
#     with open(settings.STATICFILES_DIRS[0] + '/command.json', 'r', encoding='utf-8') as outfile:
#         data = json.load(outfile)
#         print(data)  # Здесь вы можете использовать данные, загруженные из файла








# # Функция проверки баланса
# def check_balance(request, slug):
#     print('Функция проверки баланса')
#     return HttpResponse('Функция проверки баланса')

# # Функция отправки платежа
# def send_money(request, slug):
#     print('Функция отправки платежа')
#     return HttpResponse('Функция отправки платежа')


# Для осуществления перехода по ссылке "http://127.0.0.1:8000/transcription/otpravit/" внутри вызываемой функции, вы можете использовать библиотеку requests для отправки GET-запроса по указанной URL.

# Вот пример кода, позволяющего осуществить переход по данной ссылке внутри вашей функции:

# import requests

# def execute_command(context, command, comment):
#     '''
#     context - словарь используемый для ответа на POST-запрос
#     command - слаг исполняемой по команде функции
#     comment - ключевые слова запроса (см. базу данных)
#     '''
#     # Осуществление GET-запроса по указанной URL
#     response = requests.get('http://127.0.0.1:8000/transcription/' + command + '/')

#     # Проверка статуса ответа
#     if response.status_code == 200:
#         # Если запрос выполнен успешно, можно продолжить с использованием полученных данных
#         # Например, вы можете получить содержимое ответа и использовать его в дальнейшей логике вашей функции
#         response_content = response.content
#     else:
#         # В случае возникновения ошибки обработайте её соответствующим образом
#         context['search_text'] = 'Ошибка: Не удалось осуществить переход по ссылке'
# Этот код отправляет GET-запрос по указанной URL и проверяет статус ответа. В случае успешного выполнения запроса, он может использовать полученное содержимое для продолжения дальнейшей логики функции. Если ответ содержит ошибку, вы можете обработать её в соответствии с вашими потребностями.

# Обратите внимание, что вы должны проверить и обработать любые возможные ошибки, которые могут возникнуть при выполнении GET-запроса.


# Конечно, вот пример кода для отправки POST-запроса на указанный URL с использованием библиотеки requests в Python:

# import requests

# def execute_command(context, command, comment):
#     '''
#     context - словарь используемый для ответа на POST-запрос
#     command - слаг исполняемой по команде функции
#     comment - ключевые слова запроса (см. базу данных)
#     '''
#     # Данные для отправки в POST-запросе
#     data = {
#         'key1': 'value1',
#         'key2': 'value2'
#         # Добавьте другие необходимые данные
#     }

#     # Отправка POST-запроса на указанный URL
#     response = requests.post('http://127.0.0.1:8000/transcription/' + command + '/', data=data)

#     # Проверка статуса ответа
#     if response.status_code == 200:
#         # Если запрос выполнен успешно, можно продолжить с использованием полученных данных
#         response_content = response.content
#         # Добавьте логику обработки полученных данных
#     else:
#         # В случае возникновения ошибки обработайте её соответствующим образом
#         context['search_text'] = 'Ошибка: Не удалось выполнить POST-запрос'





# пример кода с добавлением логики отправки данных из базы данных при обработке POST-запроса:
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import YourModel  # Замените YourModel на реальное имя вашей модели
# from.serializers import YourSerializer  # Замените YourSerializer на реальный сериализатор

# СДЕЛАЙ НА ЭТОМ ПРИМЕРЕ ДВЕ АПИШКИ 
# ИЗ ЭТОЙ
# # Функция проверки баланса
# def check_balance(request, slug):
#     print('Функция проверки баланса')
#     return HttpResponse('Функция проверки баланса')


# И ИЗ ЭТОЙ
# # Функция отправки платежа
# def send_money(request, slug):
#     print('Функция отправки платежа')
#     return HttpResponse('Функция отправки платежа')
# ФУНКЦИЙ

# class SendMoneyAPIView(APIView):
#     def get(self, request, slug):
#         # Логика обработки GET-запроса
#         print('Функция проверки баланса')

#         # Получение данных из базы данных
#         data_from_db = YourModel.objects.get(slug=slug)  # Замените это на ваш фактический запрос к базе данных

#         # Сериализация данных
#         serializer = YourSerializer(data_from_db)  # Замените на ваш сериализатор и модель

#         # Отправка данных в ответе
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, slug):
#         # Логика обработки POST-запроса
#         print('Функция отправки платежа')

#         # Создание новой записи в базе данных
#         new_entry = YourModel.objects.create(name='New Entry')  # Пример добавления новой записи в базу данных

#         # Получение данных из базы данных
#         data_from_db = YourModel.objects.all()  # Получить все записи, замените это на ваш запрос к базе данных

#         # Сериализация данных
#         serializer = YourSerializer(data_from_db, many=True)  # Замените на ваш сериализатор и модель

#         # Отправка данных в ответе
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# Не забудьте прописать соответствующий маршрут в файле urls.py вашего приложения, чтобы связать этот APIView с URL-адресом, соответствующим вашим требованиям.



# # API проверки баланса
# class CheckBalanceAPIView(APIView):
#     def get(self, request, slug):
        
#         # Здесь логика обработки GET-запроса
        
#         content = 'Ваш баланс 2000 рублей.'
#         return Response(content, status=status.HTTP_200_OK)

#     def post(self, request, slug):

#         # Здесь логика обработки POST-запроса
       
#         content = 'Ваш баланс 2000 рублей.'
#         return Response(content, status=status.HTTP_201_CREATED)

# # API отправки платежа
# class SendMoneyAPIView(APIView):
#     def get(self, request, slug):
        
#         # Здесь логика обработки GET-запроса
        
#         content = 'Ваш платеж на сумму 500 рублей отправлен.'
#         return Response(content, status=status.HTTP_200_OK)

#     def post(self, request, slug):
        
#         # Здесь логика обработки POST-запроса
       
#         content = 'Ваш платеж на сумму 500 рублей отправлен.'
#         return Response(content, status=status.HTTP_201_CREATED)



# - - - - DEPLOY - - - - - - -


# import os
# from pathlib import Path

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# # BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-64&9d##dfbc6_zt(w$_gd0#%bsb6g1q6iuj*t4=@e&ne4=2&uz'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv('DEBUG')

# ALLOWED_HOSTS = [
#         '95.163.234.106',
# ]


# # Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework', # DRF
#     'corsheaders', # CORS
#     'django.contrib.postgres', # Операции полнотекстового поиска стр.177
    
#     'transcription', # Наше приложение 
# ]

# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware', # CORS
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'iiassistant.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'iiassistant.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME'),
#         'HOST': os.getenv('DB_HOST'),
#         # 'PORT': os.getenv('DB_PORT'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD')
#     }
# }

# # Password validation
# # https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_URL = '/static/'

# # Статику расположим внутри приложения 'transcription' 
# #STATICFILES_DIRS = [
# #    os.path.join(BASE_DIR, 'transcription', 'static'),
# #]

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# # Указание MEDIA_URL для доступа к медиа-файлам через URL
# MEDIA_URL = '/media/'

# # Путь к папке, в которой будут сохраняться загруженные файлы (например, аудиозаписи)
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# # Default primary key field type
# # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS_ALLOW_CREDENTIALS = True # This allows CORS requests to go in and out

# CORS_ALLOW_HEADERS = (
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# )

# CORS_ALLOWED_ORIGINS = [
#     "http://95.163.234.106:8000",
# ]
