"""Set up pre-trained Keras models."""


# pylint: disable=import-error,no-name-in-module,ungrouped-imports
from tensorflow.keras.applications.densenet import (
    DenseNet121, DenseNet169, DenseNet201,
    preprocess_input as densenet_preprocess_input)
from keras.applications.densenet import (
    DENSENET121_WEIGHT_PATH as DENSENET121_URL,
    DENSENET169_WEIGHT_PATH as DENSENET169_URL,
    DENSENET201_WEIGHT_PATH as DENSENET201_URL,
)
from tensorflow.keras.applications.efficientnet import (
    EfficientNetB0,
    EfficientNetB1,
    EfficientNetB2,
    EfficientNetB3,
    EfficientNetB4,
    EfficientNetB5,
    EfficientNetB6,
    EfficientNetB7,
    preprocess_input as efficientnet_preprocess_input)
from keras.applications.efficientnet import (
    BASE_WEIGHTS_PATH as EFFICIENTNET_BASE_URL,
)
from tensorflow.keras.applications.inception_v3 import (
    InceptionV3,
    preprocess_input as inception_preprocess_input)
from keras.applications.inception_v3 import (
    WEIGHTS_PATH as INCEPTION_URL,
)
from tensorflow.keras.applications.inception_resnet_v2 import (
    InceptionResNetV2,
    preprocess_input as inception_resnet_preprocess_input)
from keras.applications.inception_resnet_v2 import (
    BASE_WEIGHT_URL as INCEPTION_RESNET_BASE_URL,
)
from tensorflow.keras.applications.mobilenet import (
    MobileNet,
    preprocess_input as mobilenet_v1_preprocess_input)
from keras.applications.mobilenet import (
    BASE_WEIGHT_PATH as MOBILENET_V1_BASE_URL,
)
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input as mobilenet_v2_preprocess_input)
from keras.applications.mobilenet_v2 import (
    BASE_WEIGHT_PATH as MOBILENET_V2_BASE_URL,
)
from tensorflow.keras.applications.mobilenet_v3 import (
    preprocess_input as mobilenet_v3_preprocess_input)
from keras.applications.mobilenet_v3 import (
    MobileNetV3Large, MobileNetV3Small,
    BASE_WEIGHT_PATH as MOBILENET_V3_BASE_URL,
)
from tensorflow.keras.applications.nasnet import (
    NASNetLarge, NASNetMobile,
    preprocess_input as nasnet_preprocess_input)
from keras.applications.nasnet import (
    NASNET_LARGE_WEIGHT_PATH as NASNET_LARGE_URL,
    NASNET_MOBILE_WEIGHT_PATH as NASNET_MOBILE_URL,
)
from tensorflow.keras.applications.resnet import (
    ResNet50, ResNet101, ResNet152,
    preprocess_input as resnet_v1_preprocess_input)
from keras.applications.resnet import (
    BASE_WEIGHTS_PATH as RESNET_BASE_URL,
)
from tensorflow.keras.applications.resnet_v2 import (
    ResNet50V2, ResNet101V2, ResNet152V2,
    preprocess_input as resnet_v2_preprocess_input)
from tensorflow.keras.applications.vgg16 import (
    VGG16,
    preprocess_input as vgg_preprocess_input)
from keras.applications.vgg16 import (
    WEIGHTS_PATH as VGG16_URL,
)
from tensorflow.keras.applications.vgg19 import VGG19
from keras.applications.vgg19 import (
    WEIGHTS_PATH as VGG19_URL,
)
from tensorflow.keras.applications.xception import (
    Xception,
    preprocess_input as xception_preprocess_input)
from keras.applications.xception import (
    TF_WEIGHTS_PATH as XCEPTION_URL,
)

from djaizz.model.models.ml.keras import PreTrainedKerasImageNetClassifier
from djaizz.util import full_qual_name


MODEL_SPECS = (
    (DenseNet121, densenet_preprocess_input, 224,
     DENSENET121_URL,
     'densenet121_weights_tf_dim_ordering_tf_kernels.h5'),

    (DenseNet169, densenet_preprocess_input, 224,
     DENSENET169_URL,
     'densenet169_weights_tf_dim_ordering_tf_kernels.h5'),

    (DenseNet201, densenet_preprocess_input, 224,
     DENSENET201_URL,
     'densenet201_weights_tf_dim_ordering_tf_kernels.h5'),

    (EfficientNetB0, efficientnet_preprocess_input, 224,
     f'{EFFICIENTNET_BASE_URL}efficientnetb0.h5',
     'efficientnetb0.h5'),

    (EfficientNetB1, efficientnet_preprocess_input, 240,
     f'{EFFICIENTNET_BASE_URL}efficientnetb1.h5',
     'efficientnetb1.h5'),

    (EfficientNetB2, efficientnet_preprocess_input, 260,
     f'{EFFICIENTNET_BASE_URL}efficientnetb2.h5',
     'efficientnetb2.h5'),

    (EfficientNetB3, efficientnet_preprocess_input, 300,
     f'{EFFICIENTNET_BASE_URL}efficientnetb3.h5',
     'efficientnetb3.h5'),

    (EfficientNetB4, efficientnet_preprocess_input, 380,
     f'{EFFICIENTNET_BASE_URL}efficientnetb4.h5',
     'efficientnetb4.h5'),

    (EfficientNetB5, efficientnet_preprocess_input, 456,
     f'{EFFICIENTNET_BASE_URL}efficientnetb5.h5',
     'efficientnetb5.h5'),

    (EfficientNetB6, efficientnet_preprocess_input, 528,
     f'{EFFICIENTNET_BASE_URL}efficientnetb6.h5',
     'efficientnetb6.h5'),

    (EfficientNetB7, efficientnet_preprocess_input, 600,
     f'{EFFICIENTNET_BASE_URL}efficientnetb7.h5',
     'efficientnetb7.h5'),

    (InceptionV3, inception_preprocess_input, 299,
     INCEPTION_URL,
     'inception_v3_weights_tf_dim_ordering_tf_kernels.h5'),

    (InceptionResNetV2, inception_resnet_preprocess_input, 299,
     f'{INCEPTION_RESNET_BASE_URL}'
     'inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5',
     'inception_resnet_v2_weights_tf_dim_ordering_tf_kernels.h5'),

    (MobileNet, mobilenet_v1_preprocess_input, 224,
     f'{MOBILENET_V1_BASE_URL}mobilenet_1_0_224_tf.h5',
     'mobilenet_1_0_224_tf.h5'),

    (MobileNetV2, mobilenet_v2_preprocess_input, 224,
     f'{MOBILENET_V2_BASE_URL}'
     'mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224.h5',
     'mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224.h5'),

    (MobileNetV3Large, mobilenet_v3_preprocess_input, 224,
     f'{MOBILENET_V3_BASE_URL}weights_mobilenet_v3_large_224_1.0_float.h5',
     'weights_mobilenet_v3_large_224_1.0_float.h5'),

    (MobileNetV3Small, mobilenet_v3_preprocess_input, 224,
     f'{MOBILENET_V3_BASE_URL}weights_mobilenet_v3_small_224_1.0_float.h5',
     'weights_mobilenet_v3_small_224_1.0_float.h5'),

    (NASNetLarge, nasnet_preprocess_input, 331,
     NASNET_LARGE_URL,
     'nasnet_large.h5'),

    (NASNetMobile, nasnet_preprocess_input, 224,
     NASNET_MOBILE_URL,
     'nasnet_mobile.h5'),

    (ResNet50, resnet_v1_preprocess_input, 224,
     f'{RESNET_BASE_URL}resnet50_weights_tf_dim_ordering_tf_kernels.h5',
     'resnet50_weights_tf_dim_ordering_tf_kernels.h5'),

    (ResNet101, resnet_v1_preprocess_input, 224,
     f'{RESNET_BASE_URL}resnet101_weights_tf_dim_ordering_tf_kernels.h5',
     'resnet101_weights_tf_dim_ordering_tf_kernels.h5'),

    (ResNet152, resnet_v1_preprocess_input, 224,
     f'{RESNET_BASE_URL}resnet152_weights_tf_dim_ordering_tf_kernels.h5',
     'resnet152_weights_tf_dim_ordering_tf_kernels.h5'),

    (ResNet50V2, resnet_v2_preprocess_input, 224,
     f'{RESNET_BASE_URL}resnet50v2_weights_tf_dim_ordering_tf_kernels.h5',
     'resnet50v2_weights_tf_dim_ordering_tf_kernels.h5'),

    (ResNet101V2, resnet_v2_preprocess_input, 224,
     f'{RESNET_BASE_URL}resnet101v2_weights_tf_dim_ordering_tf_kernels.h5',
     'resnet101v2_weights_tf_dim_ordering_tf_kernels.h5'),

    (ResNet152V2, resnet_v2_preprocess_input, 224,
     f'{RESNET_BASE_URL}resnet152v2_weights_tf_dim_ordering_tf_kernels.h5',
     'resnet152v2_weights_tf_dim_ordering_tf_kernels.h5'),

    (VGG16, vgg_preprocess_input, 224,
     VGG16_URL,
     'vgg16_weights_tf_dim_ordering_tf_kernels.h5'),

    (VGG19, vgg_preprocess_input, 224,
     VGG19_URL,
     'vgg19_weights_tf_dim_ordering_tf_kernels.h5'),

    (Xception, xception_preprocess_input, 299,
     XCEPTION_URL,
     'xception_weights_tf_dim_ordering_tf_kernels.h5')
)


def run():
    """Run this script."""
    model_name_prefix = f'{PreTrainedKerasImageNetClassifier.__name__}-'

    for keras_loader, preproc, img_dim_size, global_url, local_file_name in \
            MODEL_SPECS:
        try:
            print(PreTrainedKerasImageNetClassifier.objects.update_or_create(
                name=model_name_prefix + keras_loader.__name__,
                defaults=dict(
                    loader_module_and_qualname=full_qual_name(keras_loader),
                    preprocessor_module_and_qualname=full_qual_name(preproc),
                    artifact_global_url=global_url,
                    artifact_local_path=f'~/.keras/models/{local_file_name}',
                    params=dict(img_dim_size=img_dim_size)))[0])

        except Exception as err:   # pylint: disable=broad-except
            print(f'{PreTrainedKerasImageNetClassifier.__name__} model '
                  f'not set up: {err}')
