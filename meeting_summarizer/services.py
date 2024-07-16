import assemblyai as aai
import os
import environ
from pathlib import Path
import time
from .models import Recording, Transcript

# participant_count, file_name='sales-partner-sample-meeting-data-[AudioTrimmer.com].mp3'
def get_script(audio_file_path):
    BASE_DIR = Path(__file__).resolve().parent.parent
    env = environ.Env(DEBUG=(bool, True))
    environ.Env.read_env(
        env_file=os.path.join(BASE_DIR, '.env')
    )

    aai.settings.api_key = env('ASSEMBLY_KEY')
    # audio_url = "/Users/imgyuseong/Downloads/sales-partner-sample-meeting-data-[AudioTrimmer.com].mp3"
    audio_url = audio_file_path
    config = aai.TranscriptionConfig(
        language_code="ko",
        speaker_labels=True,
        speakers_expected=3
    )
    # STT API 호출
    print("STT 변환중....")
    res = aai.Transcriber().transcribe(audio_url, config)
    print("STT 변환완료....")

    if res.status == "completed":
        return res.utterances
    else:
        print("!!!stt 변환 에러!!!")
        return False
def parse_transcript(utterances, recording):
    # 예시 텍스트를 파싱하여 Transcript 객체 배열로 변환
    for utterance in utterances:
        Transcript.objects.create(recording=recording, speaker=utterance.speaker, text=utterance.text)

def transcribe_audio(recording):
    audio_file_path = recording.audio_file.path
    result = get_script(audio_file_path)
    if result != False:
        parse_transcript(result, recording)


# class RecordingService:
#     @staticmethod
#     def transcribe_audio(recording):
#         BASE_DIR = Path(__file__).resolve().parent.parent
#         env = environ.Env(DEBUG=(bool, True))
#         environ.Env.read_env(
#             env_file=os.path.join(BASE_DIR, '.env')
#         )
#
#         # STT API 호출
#         aai.settings.api_key = env('ASSEMBLY_KEY')
#         audio_url = recording.audio_file.path
#         config = aai.TranscriptionConfig(
#             language_code="ko",
#             speaker_labels=True,
#             speakers_expected=3
#         )
#
#         start = time.time()
#         res = aai.Transcriber().transcribe(audio_url, config)
#         print(res)
#         print('spendTime', end='')
#         print(time.time() - start)
#         # WITH SPEAKER LABEL
#         # for utterance in transcript.utterances:
#         #     print(f"Speaker {utterance.speaker}: {utterance.text}")
#
#         # if response.status_code == 200:
#         #     transcript_id = response.json()['id']
#         #     result_url = f"{api_url}/{transcript_id}"
#         #     while True:
#         #         result_response = requests.get(result_url, headers=headers)
#         #         if result_response.status_code == 200 and result_response.json()['status'] == 'completed':
#         #             transcript_text = result_response.json()['text']
#         #             recording.transcript = transcript_text
#         #             recording.save()
#         #             break
#         #         elif result_response.status_code == 200 and result_response.json()['status'] == 'failed':
#         #             break
#





# ONLY SCRIPT
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

if __name__ == '__main__':
    get_script()

