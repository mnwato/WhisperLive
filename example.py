from whisper_live.client import TranscriptionClient
client = TranscriptionClient(
  "localhost",
  9090,
  # lang="fa",
  translate=False,
  # model="large",
  use_vad=False,
)

client("assets/jfk.flac")
# client("assets/1403.ogg")
# client("assets/passage.ogg")