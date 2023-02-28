"""Djaizz Pre-Trained Keras Image Classification Model class."""


from io import BytesIO
from sys import version_info
from typing import Union
from typing import Dict, List   # Py3.9+: use generic types

from django.db.models.fields import CharField
from django.utils.functional import classproperty

from gradio.interface import Interface
from gradio.inputs import Image as ImageInput, Slider as SliderInput
from gradio.outputs import Label as LabelOutput

import numpy
from PIL import Image, ImageOps
from tensorflow.keras.applications.imagenet_utils import \
    decode_predictions   # pylint: disable=no-name-in-module

from djaizz.model.apps import DjaizzModelModuleConfig
from djaizz.util import PGSQL_IDENTIFIER_MAX_LEN, import_obj

from ....base import _PreTrainedMLModelABC

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence   # pylint: disable=ungrouped-imports


__all__: Sequence[str] = ('PreTrainedKerasImageNetClassifier',)


ImageClassificationInputType = Union[str, BytesIO, Image.Image, numpy.ndarray]
ImageClassificationOutputType = Dict[str, float]


class PreTrainedKerasImageNetClassifier(_PreTrainedMLModelABC):
    # pylint: disable=abstract-method,too-many-ancestors
    """Djaizz Pre-Trained Keras Image Classification Model class."""

    preprocessor_module_and_qualname: CharField = \
        CharField(
            verbose_name='Preprocessor (module.dot.qualname)',
            help_text='Preprocessor (module.dot.qualname)',

            max_length=255,

            null=False,
            blank=False,
            choices=None,
            db_column=None,
            db_index=True,
            db_tablespace=None,
            default=None,
            editable=True,
            # error_messages={},
            primary_key=False,
            unique=False,
            unique_for_date=None, unique_for_month=None, unique_for_year=None,
            # validators=None
        )

    class Meta(_PreTrainedMLModelABC.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        verbose_name: str = 'Pre-Trained Keras ImageNet Classifier'
        verbose_name_plural: str = 'Pre-Trained Keras ImageNet Classifiers'

        db_table: str = (f'{DjaizzModelModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name: str = 'pretrained_keras_imagenet_classifiers'

    @property
    def img_dim_size(self) -> int:
        """(Square) Image Dimension Size."""
        return self.params[   # pylint: disable=unsubscriptable-object
            'img_dim_size']

    def _image_to_4d_array(self, image: ImageClassificationInputType) \
            -> numpy.ndarray:
        # if file-like or string file path, then load from file
        if isinstance(image, (str, BytesIO)):
            image: Image.Image = Image.open(fp=image, mode='r', formats=None)

        # if PIL.Image.Image instance,
        # then fit to size model expects and then convert to NumPy array
        if isinstance(image, Image.Image):
            img_dim_size: int = self.img_dim_size
            image: numpy.ndarray = \
                numpy.asarray(ImageOps.fit(image=image,
                                           size=(img_dim_size, img_dim_size),
                                           method=Image.BICUBIC,
                                           bleed=0,
                                           centering=(0.5, 0.5)),
                              dtype=int,
                              order=None)

        assert isinstance(image, numpy.ndarray), \
            TypeError(f'*** {image} not a NumPy Array ***')

        # convert to batch of 1 3D NumPy array
        return numpy.expand_dims(image, axis=0)

    @property
    def preprocessor(self) -> callable:
        """Image Preprocessor method."""
        return import_obj(self.preprocessor_module_and_qualname)

    def predict(self,
                image_or_images: Union[ImageClassificationInputType,
                                       Sequence[ImageClassificationInputType]],
                n_labels: int = 5) \
            -> Union[ImageClassificationOutputType,
                     List[ImageClassificationOutputType]]:
        # pylint: disable=arguments-differ
        """Classify Image(s)."""
        single_img: bool = isinstance(image_or_images, (str, BytesIO,
                                                        Image.Image,
                                                        numpy.ndarray))

        imgs: List[ImageClassificationInputType] = ([image_or_images]
                                                    if single_img
                                                    else image_or_images)

        # construct 4D array of images' data fitted into standardized size
        fitted_img_batch_arr: numpy.ndarray = \
            numpy.vstack([self._image_to_4d_array(image=img) for img in imgs])

        # preprocess
        preprocessed_fitted_img_batch_arr: numpy.ndarray = \
            self.preprocessor(fitted_img_batch_arr)

        # load native model object & predict
        self.load()

        pred_prob_arr: numpy.ndarray = \
            self.native_obj.predict(x=preprocessed_fitted_img_batch_arr)

        # decode predictions & return JSON-serializable dict
        decoded_preds: List[Dict[str, float]] = [{tup[1]: float(tup[2])
                                                  for tup in decoded_pred}
                                                 for decoded_pred in
                                                 decode_predictions(
                                                     preds=pred_prob_arr,
                                                     top=n_labels)]

        return decoded_preds[0] if single_img else decoded_preds

    @classproperty
    def gradio_ui(cls) -> Interface:   # noqa: N805
        # pylint: disable=no-self-argument
        """Gradio Interface."""
        return Interface(
            fn=cls.predict,
            # (Callable) - the function to wrap an interface around.

            inputs=[ImageInput(shape=None,
                               image_mode='RGB',
                               invert_colors=False,
                               source='upload',
                               tool='editor',
                               type='pil',
                               label='Upload an Image to Classify',
                               optional=False),

                    SliderInput(minimum=3, maximum=10, step=1, default=5,
                                label=('No. of ImageNet Labels to Return'))],
            # (Union[str, List[Union[str, InputComponent]]]) -
            # a single Gradio input component,
            # or list of Gradio input components.
            # Components can either be passed as instantiated objects,
            # or referred to by their string shortcuts.
            # The number of input components should match
            # the number of parameters in fn.

            outputs=LabelOutput(num_top_classes=10,
                                type='auto',
                                label='Likely ImageNet Labels'),
            # (Union[str, List[Union[str, OutputComponent]]]) -
            # a single Gradio output component,
            # or list of Gradio output components.
            # Components can either be passed as instantiated objects,
            # or referred to by their string shortcuts.
            # The number of output components should match
            # the number of values returned by fn.

            verbose=True,
            # (bool) - whether to print detailed information during launch.

            examples=None,
            # (Union[List[List[Any]], str]) - sample inputs for the function;
            # if provided, appears below the UI components and can be used
            # to populate the interface.
            # Should be nested list, in which the outer list consists of
            # samples and each inner list consists of an input
            # corresponding to each input component.
            # A string path to a directory of examples can also be provided.
            # If there are multiple input components and a directory
            # is provided, a log.csv file must be present in the directory
            # to link corresponding inputs.

            examples_per_page=10,
            # (int) - If examples are provided, how many to display per page.

            live=False,
            # (bool) - should the interface automatically reload on change?

            layout='unaligned',
            # (str) - Layout of input and output panels.
            # - "horizontal" arranges them as two columns of equal height,
            # - "unaligned" arranges them as two columns of unequal height, and
            # - "vertical" arranges them vertically.

            show_input=True,
            show_output=True,

            capture_session=False,
            # (bool) - if True, captures the default graph and session
            # (needed for Tensorflow 1.x)

            interpretation='default',
            # (Union[Callable, str]) - function that provides interpretation
            # explaining prediction output.
            # Pass "default" to use built-in interpreter.

            num_shap=2.0,
            # (float) - a multiplier that determines how many examples
            # are computed for shap-based interpretation.
            # Increasing this value will increase shap runtime,
            # but improve results.

            theme='default',
            # (str) - Theme to use - one of
            # - "default",
            # - "huggingface",
            # - "grass",
            # - "peach".
            # Add "dark" prefix, e.g. "darkpeach" or "darkdefault"
            # for darktheme.

            repeat_outputs_per_model=True,

            title=cls._meta.verbose_name,
            # (str) - a title for the interface;
            # if provided, appears above the input and output components.

            description='A Keras model trained to classify ImageNet data',
            # (str) - a description for the interface;
            # if provided, appears above the input and output components.

            article=None,
            # (str) - an expanded article explaining the interface;
            # if provided, appears below the input and output components.
            # Accepts Markdown and HTML content.

            thumbnail=None,
            # (str) - path to image or src to use as display picture for models
            # listed in gradio.app/hub

            css=None,
            # (str) - custom css or path to custom css file
            # to use with interface.

            server_port=None,
            # (int) - will start gradio app on this port (if available)

            # server_name=networking.LOCALHOST_NAME,
            # (str) - to make app accessible on local network set to "0.0.0.0".

            height=500,
            width=900,

            allow_screenshot=True,
            # (bool) - if False, users will not see a button
            # to take a screenshot of the interface.

            allow_flagging=False,
            # (bool) - if False, users will not see a button
            # to flag an input and output.

            flagging_options=None,
            # (List[str]) - if not None, provides options a user must select
            # when flagging.

            encrypt=False,
            # (bool) - If True, flagged data will be encrypted
            # by key provided by creator at launch

            show_tips=False,
            # (bool) - if True, will occasionally show tips
            # about new Gradio features

            flagging_dir='flagged',
            # (str) - what to name the dir where flagged data is stored.

            analytics_enabled=True,

            enable_queue=False,
            # (bool) - if True, inference requests will be served through
            # a queue instead of with parallel threads.
            # Required for longer inference times (> 1min) to prevent timeout.
        )
