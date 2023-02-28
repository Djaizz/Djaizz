"""Djaizz Pre-Trained Hugging Face Question Answerer Model class."""


from sys import version_info
from typing import List   # Py3.9+: use generic types
from typing import Union

from django.utils.functional import classproperty

from gradio.interface import Interface
from gradio.inputs import (Textbox as TextboxInput,
                           Number as NumberInput,
                           Checkbox as CheckboxInput)
from gradio.outputs import JSON as JSONOutput   # noqa: N811

from djaizz.model.apps import DjaizzModelModuleConfig
from djaizz.util import PGSQL_IDENTIFIER_MAX_LEN

from .base import PreTrainedHuggingFaceTransformer

if version_info >= (3, 9):
    from collections.abc import Sequence
else:
    from typing import Sequence   # pylint: disable=ungrouped-imports


__all__: Sequence[str] = ('PreTrainedHuggingFaceQuestionAnswerer',)


QuestionAnswerInputType = str
QuestionAnswerOutputType = dict


class PreTrainedHuggingFaceQuestionAnswerer(PreTrainedHuggingFaceTransformer):
    # pylint: disable=abstract-method,too-many-ancestors
    """Djaizz Pre-Trained Hugging Face Question Answerer Model class."""

    class Meta(PreTrainedHuggingFaceTransformer.Meta):
        # pylint: disable=too-few-public-methods
        """Django Model Class Metadata."""

        verbose_name: str = 'Pre-Trained Hugging Face Question Answerer'
        verbose_name_plural: str = \
            'Pre-Trained Hugging Face Question Answerers'

        db_table: str = (f'{DjaizzModelModuleConfig.label}_'
                         f"{__qualname__.split(sep='.', maxsplit=1)[0]}")
        assert len(db_table) <= PGSQL_IDENTIFIER_MAX_LEN, \
            ValueError(f'*** "{db_table}" DB TABLE NAME TOO LONG ***')

        default_related_name = 'pretrained_hugging_face_question_answerers'

    def predict(self,
                question: Union[QuestionAnswerInputType,
                                Sequence[QuestionAnswerInputType]],
                context: Union[QuestionAnswerInputType,
                               Sequence[QuestionAnswerInputType]],
                top_k: int = 1,
                doc_stride: int = 128,
                max_answer_len: int = 15,
                max_seq_len: int = 384,
                max_question_len: int = 64,
                handle_impossible_answer: bool = False) \
            -> Union[QuestionAnswerOutputType, List[QuestionAnswerOutputType]]:
        # pylint: disable=arguments-differ,too-many-arguments
        """Answer Question(s) based on Text(s)."""
        if not isinstance(question, (str, list)):
            question: List[QuestionAnswerInputType] = list(question)

        if not isinstance(context, (str, list)):
            context: List[QuestionAnswerInputType] = list(context)

        self.load()

        return self.native_obj(
            question=question, context=context, top_k=top_k,
            doc_stride=doc_stride,
            max_answer_len=max_answer_len,
            max_seq_len=max_seq_len,
            max_question_len=max_question_len,
            handle_impossible_answer=handle_impossible_answer)

    @classproperty
    def gradio_ui(cls) -> Interface:   # noqa: N805
        # pylint: disable=no-self-argument
        """Gradio Interface."""
        return Interface(
            fn=lambda self, question, context, top_k,
            doc_stride, max_answer_len, max_seq_len,
            max_question_len, handle_impossible_answer:
                cls.predict(self,
                            question=question, context=context,
                            top_k=int(top_k),
                            doc_stride=int(doc_stride),
                            max_answer_len=int(max_answer_len),
                            max_seq_len=int(max_seq_len),
                            max_question_len=int(max_question_len),
                            handle_impossible_answer=handle_impossible_answer),
            # (Callable) - the function to wrap an interface around.

            inputs=[TextboxInput(lines=2,
                                 placeholder='Question',
                                 default='',
                                 numeric=False,
                                 type='str',
                                 label='Question'),

                    TextboxInput(lines=10,
                                 placeholder='Context',
                                 default='',
                                 numeric=False,
                                 type='str',
                                 label='Context'),

                    NumberInput(default=1, label='Top K'),

                    NumberInput(default=128, label='Doc Stride'),

                    NumberInput(default=15, label='Max Answer Length'),

                    NumberInput(default=384, label='Max Sequence Length'),

                    NumberInput(default=64, label='Max Question Length'),

                    CheckboxInput(default=False,
                                  label='Handle Impossible Answer?')],

            # (Union[str, List[Union[str, InputComponent]]]) -
            # a single Gradio input component,
            # or list of Gradio input components.
            # Components can either be passed as instantiated objects,
            # or referred to by their string shortcuts.
            # The number of input components should match
            # the number of parameters in fn.

            outputs=JSONOutput(label='Likely Answer(s)'),
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

            description=('A pre-trained Hugging Face model '
                         'for extractive question answering'),
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
