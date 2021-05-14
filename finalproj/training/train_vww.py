# Lint as: python3
"""Training for the visual wakewords person detection model.

The visual wakewords person detection model is a core model for the TinyMLPerf
benchmark suite. This script provides source for how the reference model was
created and trained, and can be used as a starting point for open submissions
using re-training.
"""

import os

from absl import app
from vww_model import mobilenet_v1

import tensorflow as tf
assert tf.__version__.startswith('2')

IMAGE_SIZE = 96
BATCH_SIZE = 128
EPOCHS = [ 35, 15, 15, 35 ]
PATIENCE = 7

BASE_DIR = os.path.join(os.getcwd(), 'dataset')


def main(argv):
  if len(argv) >= 2:
    model = tf.keras.models.load_model(argv[1])
  else:
    model = mobilenet_v1()

  model.summary()

  batch_size = 50
  validation_split = 0.1

  datagen = tf.keras.preprocessing.image.ImageDataGenerator(
      rotation_range=10,
      width_shift_range=0.05,
      height_shift_range=0.05,
      zoom_range=.1,
      horizontal_flip=True,
      validation_split=validation_split,
      rescale=1. / 255)
  train_generator = datagen.flow_from_directory(
      BASE_DIR,
      target_size=(IMAGE_SIZE, IMAGE_SIZE),
      batch_size=BATCH_SIZE,
      subset='training',
      shuffle=True,
      color_mode='rgb')
  val_generator = datagen.flow_from_directory(
      BASE_DIR,
      target_size=(IMAGE_SIZE, IMAGE_SIZE),
      batch_size=BATCH_SIZE,
      subset='validation',
      shuffle=True,
      color_mode='rgb')
  print(train_generator.class_indices)

  # WARNING: These are Google Colab specific
  model = train_epochs(model, train_generator, val_generator, EPOCHS[0], 0.01)
  model.save('/content/drive/MyDrive/ML_IoT/vww_96.s1.h5')
  model = train_epochs(model, train_generator, val_generator, EPOCHS[1], 0.001)
  model.save('/content/drive/MyDrive/ML_IoT/vww_96.s2.h5')
  model = train_epochs(model, train_generator, val_generator, EPOCHS[2], 0.0005)
  model.save('/content/drive/MyDrive/ML_IoT/vww_96.s3.h5')
  model = train_epochs(model, train_generator, val_generator, EPOCHS[3], 0.00025)
  model.save('/content/drive/MyDrive/ML_IoT/vww_96.s4.h5')

  # Save model HDF5
  if len(argv) >= 3:
    model.save(argv[2])
  else:
    model.save('trained_models/vww_96.h5')


def train_epochs(model, train_generator, val_generator, epoch_count,
                 learning_rate):
  model.compile(
      optimizer=tf.keras.optimizers.Adam(learning_rate),
      loss='categorical_crossentropy',
      metrics=['accuracy'])
  history_fine = model.fit(
      train_generator,
      steps_per_epoch=len(train_generator),
      epochs=epoch_count,
      validation_data=val_generator,
      validation_steps=len(val_generator),
      batch_size=BATCH_SIZE,
      callbacks=[
        tf.keras.callbacks.EarlyStopping(verbose=1, patience=PATIENCE),
        tf.keras.callbacks.ModelCheckpoint(
          filepath='/content/drive/MyDrive/ML_IoT/vww_96.best.h5',
          monitor='val_accuracy',
          mode='max',
          save_best_only=True
        )
      ]
    )
  return model


if __name__ == '__main__':
  app.run(main)
