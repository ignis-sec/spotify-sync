from .modules.rgb_keyboard.audio_loopback import AudioController
import pyaudio
import asyncio
class SharedAudioController(AudioController):
    def __init__(self, aud_format=pyaudio.paInt16, channels=2, rate=48000, device_name="CABLE Output", dampen=13, frame_delay=0):
        super().__init__(aud_format=aud_format, channels=channels, rate=rate, device_name=device_name, dampen=dampen)
        self.audio_data = self.rawRead()
        self.frame_delay = frame_delay

    def store_read(self):
        self.audio_data = self.rawRead()

    def readOnce(self,count,reduction,top=100):
        return self.process_audio(self.audio_data,count,reduction)

    async def refresh_loop(self):
        while True:
            self.store_read()
            await asyncio.sleep(self.frame_delay)