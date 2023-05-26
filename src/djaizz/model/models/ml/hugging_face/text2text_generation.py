"""Djaizz Pre-Trained Hugging Face Text-to-Text Generator Model class."""


from sys import version_info
from typing import Union

from django.utils.functional import classproperty

from gradio.interface import Interface
from gradio.inputs import (Textbox as TextboxInput,
                           Checkbox as CheckboxInput)
from gradio.outputs import JSON as JSONOutput   # noqa: N811

from djaizz.model.apps import DjaizzModelModuleConfig
from djaizz.util import PGSQL_IDENTIFIER_MAX_LEN

from .base import PreTrainedHuggingFaceTransformer

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence   # pylint: disable=ungrouped-imports


__all__: Sequence[str] = ('PreTrainedHuggingFaceText2TextGenerator',)


Text2TextGenerationInputType = str
Text2TextGenerationOutputType = Union[str, list[int]]


class PreTrainedHuggingFaceText2TextGenerator(
        PreTrainedHuggingFaceTransformer):
    # pylint: disable=abstract-method,too-many-ancestors
    """Djaizz Pre-Trained Hugging Face Text-to-Text Generator Model class."""

    class Meta(PreTrainedHuggingFaceTransformer.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        verbose_name: str = 'Pre-Trained Hugging Face Text-to-Text Generator'
        verbose_name_plural: str = \
            'Pre-Trained Hugging Face Text-to-Text Generators'

        db_table: str = (f'{DjaizzModelModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'pretrained_hugging_face_text2text_generators'

    def predict(self,
                text_or_texts: Union[Text2TextGenerationInputType,
                                     Sequence[Text2TextGenerationInputType]],
                return_tensors: bool = False,
                return_text: bool = True,
                clean_up_tokenization_spaces: bool = True,
                **generate_kwargs) \
            -> Union[Text2TextGenerationOutputType,
                     list[Text2TextGenerationOutputType]]:
        # pylint: disable=arguments-differ
        """Generate Text-to-Text."""
        single_text: bool = isinstance(text_or_texts, str)

        if not (single_text or isinstance(text_or_texts, list)):
            text_or_texts: list[Text2TextGenerationInputType] = \
                list(text_or_texts)

        self.load()

        output = self.native_obj(
            text_or_texts,
            return_tensors=return_tensors,
            return_text=return_text,
            clean_up_tokenization_spaces=clean_up_tokenization_spaces,
            truncation=None,
            **generate_kwargs)

        if return_tensors:
            return ((output[0]['generated_token_ids']['output_ids']
                     .flatten().tolist())
                    if single_text
                    else [(result['generated_token_ids']['output_ids']
                           .flatten().tolist())
                          for result in output])

        assert return_text, \
            '*** EITHER return_tensors OR return_text MUST BE TRUE ***'

        return (output[0]['generated_text']
                if single_text
                else [result['generated_text'] for result in output])

    @classproperty
    def gradio_ui(cls) -> Interface:   # noqa: N805
        # pylint: disable=no-self-argument
        """Gradio Interface."""
        return Interface(
            fn=cls.predict,
            # (Callable) - the function to wrap an interface around.

            inputs=[TextboxInput(lines=10,
                                 placeholder='Text to Generate from',
                                 default='',
                                 numeric=False,
                                 type='str',
                                 label='Text to Generate from'),

                    CheckboxInput(default=False, label='Return Tensors?'),

                    CheckboxInput(default=True, label='Return Text?')],
            # (Union[str, list[Union[str, InputComponent]]]) -
            # a single Gradio input component,
            # or list of Gradio input components.
            # Components can either be passed as instantiated objects,
            # or referred to by their string shortcuts.
            # The number of input components should match
            # the number of parameters in fn.

            outputs=JSONOutput(label='Generated Text'),
            # (Union[str, list[Union[str, OutputComponent]]]) -
            # a single Gradio output component,
            # or list of Gradio output components.
            # Components can either be passed as instantiated objects,
            # or referred to by their string shortcuts.
            # The number of output components should match
            # the number of values returned by fn.

            verbose=True,
            # (bool) - whether to print detailed information during launch.

            examples=None,
            # (Union[list[list[Any]], str]) - sample inputs for the function;
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

            description=('A pre-trained Hugging Face model '
                         'for Text-to-Text Generation'),
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
            # (list[str]) - if not None, provides options a user must select
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
