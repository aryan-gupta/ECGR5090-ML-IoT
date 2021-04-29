from audiomentations import Compose, AddGaussianNoise, TimeStretch, PitchShift, Shift
from audiomentations.core.audio_loading_utils import load_sound_file

people_filenames = tf.io.gfile.glob('./training/people/*')
length = len(people_filenames)

files_ds = tf.data.Dataset.from_tensor_slices(people_filenames)
files_ds = files_ds.shuffle(len(people_filenames))
waveform_ds = files_ds.map(get_waveform_and_label, num_parallel_calls=AUTOTUNE)

augment = Compose([
    AddGaussianNoise(min_amplitude=0.05, max_amplitude=0.05, p=0.5),
])

for sound_file_path in people_filenames:
    samples, sample_rate = load_sound_file(sound_file_path, sample_rate=16000, mono=True)
    samples = augmenter(samples=samples, sample_rate=SAMPLE_RATE)

# PitchShift(min_semitones=-4, max_semitones=4, p=0.5)